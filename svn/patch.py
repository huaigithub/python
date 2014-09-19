#coding=utf-8
import subprocess
import commands
import sys, ConfigParser, os
import time
import util

svn_url = "http://192.168.0.80:8443/svn/SYSWARE.EDC/main/trunk"

#要过滤的后缀
exSuffer = ['.java','.classpath','.class','.log']

#比较两个版本差异命令
diff_line   = 'svn diff --summarize -r %s:%s %s'
#导出命令
export_line = 'svn export -q --force %s  %s'

#清洗路径（去掉换行符等）
def clearPath(path):
     clearUrl = path
     if path is not None:
         if path.endswith("\n"):
            clearUrl = path[0:len(path)-1]
     return clearUrl

#去除有svn标记的url
def clearSVNTag(url):
    clearSVNURL = clearPath(url)
    return clearSVNURL[1:]

#判断文件是否要导出(忽略一些文件)
def includeAble(url):
    clearUrl = clearPath(url)
    result = True
    for suffer in exSuffer:
        if clearUrl.endswith(suffer):
            result = False
            break
    return result

#判断svn是否要导出此文件（比如删除标记的文件就不需要导出了）
def svnIncludeAble(url):
    fileModify = url[0:1]
    if 'D' == fileModify:
        return False
    else:
        return True


def getVersion(url):
    process   = subprocess.Popen('svn info '+url,shell=True, stdout=subprocess.PIPE)
    while True:
        next_line = process.stdout.readline().decode('utf-8')

        if next_line == '' and process.poll() != None:
            break
        if next_line.startswith('Revision'):
            return next_line.replace('Revision:','').strip()

def getCurrentDate():
    return time.strftime("%Y%m%d", time.localtime(time.time()))


def getHistoryMaxVersion(filepath):
    filter = ['@R'];
    version = []
    list = util.GetFileList(filepath, filter)
    maxversion = -1
    for name in list:
        infin = name.rfind("-R")
        versionNumber = name[infin:].replace("-R",'')
        if versionNumber > maxversion:
            maxversion = versionNumber
    return maxversion


def exportDiffFile(svnUrl, lastVersion,rootDir):

    process = subprocess.Popen(diff_line % (lastVersion,'head',svnUrl),shell=True, stdout=subprocess.PIPE)

    patch = open(rootDir+'/differ.log' ,'w')

    while True:
        next_line = process.stdout.readline().decode('utf-8')
        if next_line == '' and process.poll() != None:
            break
        patch.write(next_line)

        clearUrl = clearSVNTag(next_line)

        sqlPath = rootDir+"/sql"

        if next_line is not None and len(next_line)>0:
            if svnIncludeAble(next_line) and includeAble(clearUrl):
                newFilepath = clearUrl.replace(svnUrl, rootDir)
                index = newFilepath.rindex('/')
                svnDir = newFilepath[0:index]
                filename = newFilepath[index+1:]
                svnDir = svnDir.strip(" ")
                if not os.path.exists(svnDir) and not clearUrl.endswith('.sql'):
                    os.makedirs(svnDir)
                if clearUrl.endswith('.sql'):
                    if not os.path.exists(sqlPath):
                        os.makedirs(sqlPath)
                    subprocess.Popen(export_line % (clearUrl, sqlPath+'/'+filename),shell=True)
                else:
                    subprocess.Popen(export_line % (clearUrl, svnDir+'/'+filename),shell=True)

def patch(svnUrl, pathPath):
    #获取给定svn的URL的最新版本号
    lastVersion = getVersion(svnUrl)

    #获取最后一次打补丁的最高版本号
    historyMaxVersion = getHistoryMaxVersion(pathPath)

    #如果从来没有用此程序打过补丁，那么就输入一个起始版本号
    if historyMaxVersion == -1:
        historyMaxVersion = raw_input()

    #拼出一个补丁目录的名称
    name = "main-"+getCurrentDate()+"@R"+historyMaxVersion+"-"+"R"+lastVersion
    patchFilePath = pathPath+"/"+name;

    if not os.path.exists(patchFilePath):
         os.makedirs(patchFilePath)
    exportDiffFile(svn_url, historyMaxVersion, patchFilePath)
    #subprocess.Popen('svn add %s' % (patchFilePath),shell=True)
   # subprocess.Popen('svn commit %s' % (patchFilePath),shell=True)

if __name__ == '__main__':
    #patch(svn_url, 'D:\sysware\main\patch')
    print getVersion(svn_url)

















