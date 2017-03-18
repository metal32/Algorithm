'''
Created on 18-Mar-2017

@author: ayush
'''
import requests
from bs4 import BeautifulSoup
import webbrowser
import re

def removeComments(string):
    string = re.sub(re.compile("<.*?>",re.DOTALL ) ,"" ,string) # (<--COMMENT -->) from string
    string = re.sub(re.compile("--->.*?",re.DOTALL ) ,"" ,string)
    return string

def trade_spider(maxpages):
    page=1
    dict={}
    desc={}
    while page<=maxpages:
        url='http://cyro.se/tvseries/index.php?&page='+str(page)
        sourcecode=requests.get(url)
        plain_text=sourcecode.text
        soup=BeautifulSoup(plain_text)
        for link in soup.find_all('td',{'class':'topic_content'}):
            href='http://cyro.se/tvseries/'+link.find('a')['href']
            name=link.find('a')['href'].split('-')
            title=' '.join(map(str,name[2:]))
            print title
            descr=link.find('div',{'class':'imgWrap'}).renderContents()
            final_descr= removeComments(descr).strip()
            print final_descr
            print 'The link for visiting the Tv-series is given below'
            print href
            print '\n\n'
            dict[title]=href
            desc[title]=final_descr
        page+=1
    return dict,desc

    

dict,desc= trade_spider(3)
print dict.keys()