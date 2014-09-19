__author__ = 'yangh'

import pymongo

connection = pymongo.Connection('192.168.0.185',27017)

crawldb = connection.crawl
crawldb.add_user("crawl","crawl")
crawldb.authenticate("crawl", "crawl")

blog_item = crawldb.blog_item
blog_item.insert({'title':'','shortcontent':'','publishtime':'','readcount':'','pinglun':'','articleurl':'','pid':''})