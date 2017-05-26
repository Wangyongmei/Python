from bs4 import BeautifulSoup
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from coming.items import ComingItem
import re
class MoiveSpider(CrawlSpider):
    name = 'coming'
    #起始url
    start_urls = [
                  "https://movie.douban.com/coming"
                  ]
    #抓取规则
    rules = [
             Rule(LinkExtractor(allow=(r"https://movie.douban.com/subject/\d+/?$")),callback="parse_page"),
             ]
    #解析抓取到网页

    def parse_page(self,response):
        soup = BeautifulSoup(response.body, 'html.parser', from_encoding='utf-8')
        movie_name_tag = soup.find('div',id='content').findChild('h1')
        movie_name = movie_name_tag.findChildren()[0].get_text()+movie_name_tag.findChildren()[1].get_text()
        director = soup.find('a',rel='v:directedBy').get_text()
        poster=soup.find('div',id='mainpic').findChild('a').findChild('img').get('src')
        actor = '/'.join(star.text for star in soup.findAll('a',rel = 'v:starring'))
        type = '/'.join(genre.text for genre in soup.findAll('span',property='v:genre'))
        region = soup.find('span',text='制片国家/地区:').next_sibling
        length_tag = soup.find('span',property = 'v:runtime')
        if str(length_tag.next_sibling)!='<br/>':
            length = length_tag.text+str(length_tag.next_sibling)
        else:
            length = length_tag.text
        date = soup.find('span',property = 'v:initialReleaseDate').text
        introduction =re.sub(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020','',str(soup.find('span',property='v:summary').text))


        grade= soup.find('strong',property='v:average').text
        comment_amount=soup.find('span',property='v:votes').text
        herald=soup.find('a',class_='related-pic-video').get('href')
        herald_img=soup.find('a',class_='related-pic-video').findChild('img').get('src')
        images=soup.find('ul',class_='related-pic-bd').findAll('li')
        imagelist=[]
        for img in images:
           imagelist.append(img.findChild('a').findChild('img').get('src'))

        comments=soup.findAll('div',class_='comment')

        commenetlist=[]
        for  t in comments:
          com={}
          com['content']=re.sub(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020','',str(t.findChild('p').get_text()))
          com['people']=t.find('span',class_='comment-info').findChild('a').get_text()
          print(com)
          commenetlist.append(com)

        item = ComingItem()
        item['movie_name']=movie_name
        item['director']=director
        item['actor']=actor
        item['type']=type
        item['poster']=poster
        item['region']=region
        item['date']=date
        item['length']=length
        item['introduction']=introduction
        item['grade']=grade
        item['comment_amount']=comment_amount
        item['herald']=herald
        item['herald_img']=herald_img
        item['imagelist']=imagelist
        item['commentlist']=commenetlist




        return   item
