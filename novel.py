import requests
from parsel import Selector

def download_one_chapter(chap_url):
    response = requests.get(chap_url)
    response.encoding = response.apparent_encoding  #cancel nonsense code

    sel = Selector(response.text)
    title = sel.css('h1::text').get()

    #create new file
    f = open(title+'.txt', mode="w", encoding='utf-8')
    f.write(title)


    for line in sel.css('#content::text').getall():
        print(line.strip(), file=f)

    f.close()

first_chap_num = 2324752
last_chap_num = 2324835
for i in range(first_chap_num,last_chap_num):
    url_name = 'http://www.shuquge.com/txt/8659/'+ str(i) + '.html'
    download_one_chapter(url_name)

