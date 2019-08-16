#-*- coding: utf-8 -*-
import requests
import os,re,sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")


class main(object):

      def __init__(self):
          self.query = sys.argv[1]
          self.search = "https://soundcloud.com/search?q={}".format(self.query)

          print '[*] soundcloud-dl cli version by Hero (\033[96mardho ainullah\033[97m)'
          time.sleep(1)
          print '    [-] looking with query \033[92m%s\033[97m\n'%(self.query)


          from bs4 import BeautifulSoup
          with requests.Session() as self.reqs:
               self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'}
               self.source = self.reqs.get(re.sub(' ','%20',self.search),headers=self.header).text
               self.list = re.findall(r'<li><h2><a href="(.*?)">(.*?)</a></h2></li>',self.source)
               if len(self.list) == 0:sys.exit('       - info: \033[91mresult not found\033[97m')


          self.link = []
          self.var = 0
          for self.music in self.list:
              self.check_url = re.findall(r'/',str(self.music[0]))
              if len(self.check_url) == 1:pass
              else:
                   self.page = re.sub(r'&amp;','','        \033[94m%s\033[97m - %s'%(self.var,self.music[1]));print self.page
                   self.link.append(self.music[0])
                   self.var += 1

          self.select = raw_input('\n[?] input selection : ')
          print '[-] request content in url ~ \033[93mhttps://soundcloud.com'+self.link[int(self.select)],'\033[97m'
          self.url = 'https://soundcloud.com'+self.link[int(self.select)]


          with requests.Session() as self.done:
               self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                              'Content-type':'application/x-www-form-urlencoded',
                              'Host': 'sounddownmp3.com',}

               self.data = {'url':re.sub(':','%3A',re.sub(' ','%20',re.sub('/','%2F',self.url)))}
               self.post = self.done.post("https://www.sounddownmp3.com/down.php",headers=self.header,data=self.data).text
               self.name = re.sub('value=','',re.sub('"','',re.findall(r'value=".*?"',self.post)[0]))
               self.submit = re.findall(r'name="submit" value="(.*?)"',self.post)[0]
               self.data = {'sName':self.name,'submit':self.submit}

               try:
                    with open(raw_input('    [?] enter sound filename : ')+'.mp3','wb') as self.file:
                         print '    [*] please wait, downloading.'
                         self.file.write(self.done.post('https://www.sounddownmp3.com/down.php',data=self.data,headers=self.header).content)
                         self.file.close()
                         print '        - \033[92mfinish\033[97m'
               except Exception,a:
                      print a;pass




def looking():
    if len(sys.argv) < 2:
       sys.exit('''
!: codingend by Hero AKA muh4k3mos
!: python2 scloud.py {query} 
''')

    main()

if __name__=='__main__':
   looking()
