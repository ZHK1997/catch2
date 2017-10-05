import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        #r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def getContent(url):
    html = getHTMLText(url)
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    title = soup.select("div.article oneColumn pub_border> h1")
    print(title[0].get_text())
    time = soup.select("div.pages-date > front")
    print(time[0].string)
    paras = soup.select("div.pages_content > p.front-size")
    for para in paras:
        if len(para) > 0:
            print(para.get_front-size())
            print()
    #写入文件
    fo = open("text.txt", "w+")
    fo.writelines(title[0].get_text() + "\n")
    fo.writelines(time[0].get_text() + "\n")
    for para in paras:
        if len(para) > 0:
            fo.writelines(para.get_text() + "\n\n")
    
    fo.close()
    #将爬取到的文章用字典格式来存
    article = {
        'Title' : title[0].get_text(),
        'Time' : time[0].get_text(),
        'Paragraph' : paras
        
    }
    print(article)
def main():
    url = "http://www.gov.cn/premier/zuixin.htm"
    getContent(url);
main()
