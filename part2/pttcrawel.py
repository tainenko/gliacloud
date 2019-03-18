'''
a) 請用 Python 寫出一個可以爬 ptt /reddit 任意看板（https://www.ptt.cc ）的爬蟲程式，可以使用任意 Python 套件
以下欄位為必要
• 日期
• 作者
• 標題
• 內文
• 看板名稱
'''
import requests
from bs4 import BeautifulSoup
import os

def get_content(url):
    response = requests.get(url,cookies={'over18': '1'})
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.find('div','bbs-screen').getText()

def ptt_crawel(board):
    #所要擷取的網站網址
    base_url='https://www.ptt.cc/'
    url = base_url+'bbs/{}/index.html'.format(board)
    print(url)
    #建立回應
    response = requests.get(url,cookies={'over18': '1'})

    #將原始碼做整理
    soup = BeautifulSoup(response.text, 'lxml')
    #使用find_all()找尋特定目標
    articles = soup.find_all('div', 'r-ent')

    filename=board+'.txt'
    content_file='content.txt'

    if os.path.isfile(content_file):
        open(content_file, 'w')
    #寫入檔案中
    with open(filename,'w') as f:
        f.write('看板名稱:'+board+'\n')
        f.write('日期 作者 標題 內文 \n')
        for article in articles:
            #去除掉冒號和左右的空白
            title = article.find('div','title').getText().replace(':','').strip()
            author = article.find('div','author').getText().replace(':','').strip()
            date = article.find('div','date').getText().replace(':','').strip()
            href = article.find('a').get('href')

            print(date,author,title,href)
            f.write('{} {} {} {}{} \n'.format(date,author,title,base_url,href))
            content = get_content(base_url + href)

            content_txt=open(content_file,'a')
            content_txt.write(content+'\n')

if __name__=='__main__':
    ptt_crawel('Gossiping')