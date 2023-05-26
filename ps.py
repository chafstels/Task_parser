from bs4 import BeautifulSoup
import requests 
import csv

def write_to_csv(data):
    with open('news.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['datetime'], data['img'],data['description']])

def get_html(url):
    response  = requests.get(url).text
    return response

def getTitle(html):
    soup = BeautifulSoup(html, 'lxml')
    list_cat = soup.find('div', class_ = 'news__grid').find_all('div', class_ = 'news__item news__item__3')
    for cat in list_cat:
        title = cat.find('a', class_='news__item__title__link').text
        link = 'http://kenesh.kg' + cat.find('a', class_='news__item__title__link').get('href')
        datetime = cat.find('div', class_ = 'news__item__date').text
        try :
            img = 'http://kenesh.kg' + cat.find('img', class_ = 'news__item__image__img').get('src')
        except:
            img = None
        sop = BeautifulSoup(get_html(link), 'lxml')
        description = sop.find('div', class_ = 'ck-editor').find_all('p')
        page = ''.join([i.text for i in description])
       
        dict_ = {'title':title, 'datetime':datetime, 'img':img, 'description':page}
        write_to_csv(dict_)
        



        
def main():
    count = 1
    for i in range(20):
        news_url = f'http://kenesh.kg/ru/news/all/list?page={str(count)}'
        getTitle(get_html(news_url))
        count+=1
main()       


