import requests
from lxml import etree
import random
from concurrent.futures import ThreadPoolExecutor, wait
import time


def get_responce(url, header):
    rsp = requests.get(url, headers=header)
    rsp.encoding = "gbk"
    # print(html.text)
    html = etree.HTML(rsp.text)
    name = html.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a')
    urls = []
    for i in name:
        href = i.xpath('./@href')[0]
        # print(title ,href,)
        ur = url + href
        urls.append(ur)
        print('获取url=={}'.format(ur))

    return urls


def get_book(url, header):
    try:
        body = requests.get(url, headers=header)
        body.encoding = "gbk"
        html = etree.HTML(body.text)
    except requests.exceptions.SSLError:
        pass

    title = html.xpath("//div[@class='content_read']/div/div[@class='bookname']/h1/text()")[0].strip('?').strip("'")
    book = html.xpath("//div[@class='content_read']/div/div[@id='content']/text()")
    book = "".join(book).replace(u"\xa0\xa0\xa0\xa0", "\r\n")
    # print(book)
    with open("./quanzhifas/'{}".format(title + '.txt'), 'w', encoding='gbk') as f:
        f.write(book)
        print(title, '下载完成')


if __name__ == '__main__':
    url = "https://www.booktxt.net/0_595/"
    UseAgent = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"]
    header = {
        'Use-Agent': random.choices(UseAgent)[0],
        'Referer': url
    }
    start = time.time()
    urls = get_responce(url, header)
    futers = []
    with ThreadPoolExecutor(max_workers=300) as p:
        for url in urls:
            tast = p.submit(get_book, url=url, header=header)
            futers.append(tast)

    wait(futers)
    end = time.time()
    print('下载完成,用时{}s'.format(end - start))
