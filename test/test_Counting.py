from part1.Counting import *

class TestCounting:
    def test_get_filename(self):
        url="http://www.google.com/a.txt"
        assert get_file_name(url) == 'a.txt'

    def test_count_the_files(self):
        urls=urls = [
            "http://www.google.com/a.txt",
            "http://www.google.com.tw/a.txt",
            "http://www.google.com/download/c.jpg",
            "http://www.google.co.jp/a.txt",
            "http://www.google.com/b.txt",
            "https://facebook.com/movie/b.txt",
            "http://yahoo.com/123/000/c.jpg",
            "http://gliacloud.com/haha.png",
            ]
        res=count_the_files(urls)
        assert isinstance(res,dict)
        assert 'haha.png' in res

    def test_get_top_3_file(self):
        dct={'a.txt':5,'b.img':1,'c.xml':6,'d.txt':1,'e.img':8}
        res=get_top_3_file(dct)
        assert isinstance(res,list)
        assert 'e.img 8'==res[0]
        assert 'b.img 1' not in res
        assert 'a.txt 5' in res