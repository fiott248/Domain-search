#!/usr/bin/python
import os, sys
from sys import argv
import re
from google_translate.google_translate import translate
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import idna
reload(sys)
sys.setdefaultencoding("utf-8")
script, domain = argv

languages = ["Croatian", "Czech", "Danish",
             "Dutch", "Estonian", "Filipino",
             "Finnish", "French", "Georgian", "German", "Greek",
             "Hungarian", "Icelandic", "Indonesian", "Irish",
             "Italian", "Japanese", "Korean", "Latin", "Latvian", "Lithuanian", 
             "Macedonian", "Maltese", "Norwegian",
             "Polish", "Portuguese", "Romanian",
             "Russian", "Serbian", "Slovak", "Slovenian", "Spanish",
             "Swedish", "Turkish",
             "Ukrainian", "Welsh"]

tld = [".com", ".org", ".net", ".be", ".fr", ".fi", ".eu", ".se", ".de", ".ru", ".jp", ".co.jp"]

def check_domain(name):
    words  = ['not found', 'No match', 'is free', 'AVAILABLE', 'nothing found', 'No entries found', 'NOT FOUND']
    fulltext = ""
    firstpart = 'https://www.who.is/whois/'
    myurl = firstpart + name
    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    check = page_soup.findAll("pre",{"style":"border:0px;"})
    for texts in check:
        fulltext = texts.text.strip()
    if not check:
        print "Sorry Mate Domain %s it`s  already Registered" %(name)
    if check:
        for word in words:
            if word in fulltext:
                print "This Domain %s it`s availabe" %(name)
                count = None
            if not word in fulltext:
                if word is "none":
                    print "Sorry Mate Domain %s it`s already Registered" %(name)


def looplang(name):
    for lang in languages:
        trans = translate(name, lang, "English")
        print lang + "                    %s " %(trans)
        transdom = trans.replace(" ","")
	transdom = transdom.replace("'","")
        doma = transdom+".com"
       
	try:
            doma.decode('UTF-8')
            check_domain(doma)
        except UnicodeError:
	    encodedoma = u'%s'%transdom
            idnadom = encodedoma.encode('idna')
            doma = idnadom+".com"
            print "Domain %s has been encoded %s"%(transdom, idnadom)
            check_domain(doma) 
	    time.sleep(0.5)

looplang(domain)

