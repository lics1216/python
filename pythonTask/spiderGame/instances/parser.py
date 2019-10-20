#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
parser.py by lcs
"""
import threading
from ..utils import ConstantEnum
from bs4 import BeautifulSoup
class Parser(threading.Thread):
    def __init__(self, name, pool):
        threading.Thread.__init__(self, name=name)
        self._pool = pool
    """
      这个run 方法应该一直执行的
    """
    def run(self):
        print("%s, 正在启动" %threading.current_thread().name)
        while True:
            # 从pool 里面调用parser_html任务，获取 html
            html = self._pool.get_a_task(ConstantEnum.Parse_Html)

            # parse页面
            soup = BeautifulSoup(html, "html.parser")
            data= {}
            # game_detail_url
            link = soup.find_all("link", attrs={"rel": "canonical"})[0].attrs['href']
            data['game_detail_url'] = link
            # game_id
            link = link.split('/')
            data['game_id'] = link[len(link) - 1]
            # game_name
            link = soup.find_all("h1", attrs={"itemprop": "name"})[0].get_text()
            data['game_name'] = link
            # game_logo_url
            link = soup.find_all("img", attrs={"itemprop": "image"})[0].attrs['src']
            data['game_logo_url'] = link
            # developer    得去试 for循坏遍历contents children 有区别的
            # developer div class="header-text-author"这个开发者会出问题, 厂商和开发商，放置没有规律，只能窜在一起
            try:
                link = soup.find_all("div", attrs={"class": "header-text-author"})[0]
                spans = (' ').join(x.get_text() for x in link.find_all('span'))
                data['developer'] = spans
            except:
                data['developer'] = ''

            # publisher class="info-item-content link"
            try:
                link = soup.find_all("a", attrs={"class": "info-item-content link"})[0].get_text()
                data['publisher'] = link
            except:
                data['publisher'] = ''
            # developer_speak id="developer-speak"
            try:
                link = soup.find_all("div", attrs={"id": "developer-speak"})[0].get_text()
                data['developer_speak'] = link
            except:
                data['developer_speak'] = ''

                # description   id="description"
            try:
                link = soup.find_all("div", attrs={"id": "description"})[0].get_text()
                data['description'] = link.strip()
            except:
                data['description'] = ''

                # comments  data-taptap-tab="review"
            try:
                link = soup.find_all("a", attrs={"data-taptap-tab": "review"})[0]
                data['comments'] = link.small.get_text()
            except:
                data['comments'] = ''

            # topics  data-taptap-tab="topic"
            try:
                link = soup.find_all("a", attrs={"data-taptap-tab": "topic"})[0]
                data['topics'] = link.find_all("small")[0].get_text()
            except:
                data['topics'] = ''

                # file_size_in_mb  file_size_in_mb  class="info-item-content"
            try:
                link = soup.find_all("span", attrs={"class": "info-item-content"})
                data['file_size_in_mb'] = link[0].get_text()
                data['latest_version'] = link[1].get_text()
                data['ate_published'] = link[2].get_text()
            except:
                data['file_size_in_mb'] = ""
                data['latest_version'] = ""
                data['ate_published'] = ""

                # score class="app-rating-score"
            try:
                link = soup.find_all("span", attrs={"class": "app-rating-score"})[0].get_text()
                data['score'] = link
            except:
                data['score'] = ''

                # download  span class="text-download-times"
            try:
                link = soup.find_all("span", attrs={"class": "text-download-times"})[0].get_text()
                data['download'] = link
            except:
                data['download'] = ''
                # tags id="appTag"
            try:
                link = soup.find_all("ul", attrs={"id": "appTag"})[0]
                tagA = link.find_all('a')
                length = 8 if len(tagA) > 7 else len(tagA)
                tags = ",".join(x.get_text().strip() for x in tagA[0:length])
                data['tags'] = tags
            except:
                data['tags'] = ''
                # latest_version_score    div class="clearfix recent-7-days"
            # 需要改进，有些没有 7天前的评分 ,j所以只得把这些写在一起
            try:
                link = soup.find_all("div", attrs={"class": "clearfix recent-7-days"})[0]
                spans = link.find_all('span')
                data['score_message'] = '/'.join(x.get_text() for x in spans)
            except:
                data['score_message'] = ''

            # 添加 save 任务，内容data
            self._pool.add_a_task(ConstantEnum.Save_Item, data)

            # 完成 取parse 和 添加任务, finnish parse
            self._pool.finish_a_task(ConstantEnum.Parse_Html)