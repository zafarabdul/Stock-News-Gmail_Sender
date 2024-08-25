import requests
import schedule
import time
import smtplib
from datetime import date
from NewsAlert.models import Holder
# list_stock=[]
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
def sendg(gmail,title,url,date):
    server.login('zafarabdul05@gmail.com','bvax fnhl djey uhkl')
    message = f"Subject: Latest News Update\n\nTitle: {title}\nURL: {url}\nPublished At: {date}"
    server.sendmail('zafarabdul05@gmail.com',gmail,message.encode('utf-8'))
    print('mail send to :',gmail)
def fetch_article(URL):
    try:
        response = requests.get(URL)
        response.raise_for_status()
        news_data = response.json()
        articles = news_data.get('articles', [])
        if articles:
            latest_article = articles[0]  # Get the most recent article
            published_at = latest_article.get('publishedAt')
            return {
                'title': latest_article.get('title'),
                'url': latest_article.get('url'),
                'published_at': published_at
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None
# see this
#sendg is commented
#see this and first correct it before giving email
def fetch_data(gmail,list):
    for i in list:
        API_KEY = '6f563599e1b844a1a8aee94b6fe7b571'
        QUERY = i
        URL = f'https://newsapi.org/v2/everything?q={QUERY}&sortBy=publishedAt&apiKey={API_KEY}'
        article = fetch_article(URL)
        if article:
            dateg=article['published_at']
            dategot = dateg.split('T')[0]
            today_date=date.today()
            today_date = today_date.strftime("%Y-%m-%d")
            if dategot is not today_date:
                sendg(gmail,article['title'],article['url'],article['published_at'])
            else:
                pass
        else :
            pass

def sendlist(list):
    l=[]
    if list['st1']!= None:
        l.append(list['st1'])
    if list['st2']!= None:
        l.append(list['st2'])
    if list['st3']!= None:
        l.append(list['st3'])
    if list['st4']!= None:
        l.append(list['st4'])
    if list['st5']!= None:
        l.append(list['st5'])
    fetch_data(list['gmail'],l)
def job():
    hold=Holder.objects.all()
    data_list = []
    for item in hold:
        data_list.append({
            'gmail': item.gmail,
            'st1': item.st1,
            'st2': item.st2,
            'st3': item.st3,
            'st4': item.st4,
            'st5': item.st5
        })
    for i in data_list:
        sendlist(i)
        print("one tuple completed")
    pass

def findstock():
    print('Fetching starts in 12hrs from now')
    schedule.every(5).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
