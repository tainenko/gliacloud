'''
Counting
Given a list of urls, print out the top 3 frequent filenames.
ex.
Given
urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]
The program should print out
a.txt 3
b.txt 2
c.jpg 2
'''
import operator

def get_file_name(str):
    '''
    輸入str，回傳檔案string
    :param str:
    :return filename:
    '''
    return str.split('/')[-1]


def count_the_files(urls):
    '''
    統計url list中file出現次數，回傳dict
    :param urls:
    :return dict:
    '''
    dct={}
    for url in urls:
        file=get_file_name(url)
        dct[file]=dct.get(file,0)+1
    return dct

def get_top_3_file(dct,n=3):
    '''
    從統計的dct中取得出現次數前三筆的檔案字串
    :param dct:
    :return list:
    '''
    lst=[]

    for i in range(n):
        key=max(dct.items(), key=operator.itemgetter(1))[0]
        lst.append('{} {}'.format(key,dct[key]))
        del dct[key]
    return lst

if __name__=='__main__':
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]
    dct=count_the_files(urls)
    lst=get_top_3_file(dct)
    for l in lst:
        print(l)

