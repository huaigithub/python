__author__ = 'yangh'
#coding=utf-8
import  sys, ConfigParser, os
import commands
import subprocess

try:
    configFile = open("config.ini","r")
except IOError:
    print "config.ini is not found"
    raw_input("")
    sys.exit()

config = ConfigParser.ConfigParser()
config.readfp(configFile)
configFile.close()


url     = config.get("INFO","baseurl")
user    = config.get("INFO","user")
passwd  = config.get("INFO","passwd")
'''
userpasswd = "  /cygdrive/d/xxx --username %s --password %s" % (user, passwd)

process = subprocess.Popen("svn checkout "+url+ userpasswd, stdout=subprocess.PIPE)

while True:
    next_line = process.stdout.readline().decode('utf-8')
    if next_line == '' and process.poll() != None:
        break
    sys.stdout.write(next_line)
'''
#svn diff --summarize -r 4097:4175 http://192.168.0.80:8443/svn/SYSWARE.EDC/main/trunk


process = subprocess.Popen("svn diff --summarize -r 4411:head http://192.168.0.80:8443/svn/SYSWARE.EDC/main/trunk", stdout=subprocess.PIPE)

patch = open("d:/patch",'w')
while True:
    next_line = process.stdout.readline().decode('utf-8')
    if next_line == '' and process.poll() != None:
        break
    patch.write(next_line)


    fileModify = next_line[0:1]
    rootDir = 'D:/svn-export/a'
    filepath = next_line
    clearUrl = next_line[1:]
    if clearUrl.endswith("\n"):
        clearUrl = clearUrl[0:len(clearUrl)-1]
    if next_line is not None and len(next_line)>0:
        filepath = filepath[1:]
        if 'D' != fileModify and not clearUrl.endswith('.java'):
            newFilepath = filepath.replace('http://192.168.0.80:8443/svn/SYSWARE.EDC/main/trunk', rootDir)
            index = newFilepath.rindex('/')
            svnDir = newFilepath[0:index]
            svnDir = svnDir.strip(" ")
            if not os.path.exists(svnDir):
                os.makedirs(svnDir)
            print clearUrl
            subprocess.Popen("svn export -q --force "+clearUrl +"  "+svnDir)

'''
def publish():
    pass

def patch():
    pass

if __name__ == '__main__':
    pass
'''