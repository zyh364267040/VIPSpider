# -*- coding = utf-8 -*-
# @Time: 2021/9/26 下午9:00
"""
1.提取页面源代码
2.解析页面源代码,提取数据
"""
import requests
from pyquery import PyQuery


# 提取页面源代码
def request_page_source(url):
    resp = requests.get(url)
    resp.encoding = 'gbk'
    return resp.text


# 解析页面源代码, 提取数据
def parse_data(html):
    p = PyQuery(html)
    mt_list = p(".mt-10").items()
    for mt in mt_list:
        if not mt("div > dl:nth-child(3) > dt:contains(购车经销商)"):
            mt("div > dl:nth-child(2)").after("""
            <dl class="choose-dl">
                        <dt>购车经销商</dt>
                        <dd>
                            <a href="https://dealer.autohome.com.cn/118370#pvareaid=102556" class="js-dearname" data-val="118370,45624" data-evalid="3817364" target="_blank">郑州大展红旗体验中心</a>
                        </dd>
                    </dl>
            """)
        chexing = mt("div > dl:nth-child(1) > dd").eq(0).text().replace('\n', '').replace(' ', '')
        didian = mt("div > dl:nth-child(2) > dd").text()
        shijian = mt("div > dl:nth-child(4) > dd").text()
        print(shijian)


def main():
    url = 'https://k.autohome.com.cn/5566/#pvareaid=3454440'
    # 提取页面源代码
    html = request_page_source(url)
    # 解析页面源代码, 提取数据
    parse_data(html)


if __name__ == '__main__':
    main()
