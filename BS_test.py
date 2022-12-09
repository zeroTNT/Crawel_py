import requests
from bs4 import BeautifulSoup as BS
import re

sign_up = "https://aps.ncue.edu.tw/sign_up/"
# 以 request.get獲取網址
new_page = requests.get(sign_up)

"""
擷取title標籤, 並轉換成字串(去除標籤)
wb_title = soup.title
wb_title_str = wb_title.string
print(wb_title_str)
"""
if new_page.status_code == requests.codes.ok:
    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BS(new_page.text, features="html.parser")
    # 找到指定活動
    target = soup.find("a", string="【線上多元學習通識】生醫材料解密")#需更動目標活動
    """
    學校報名網站的固定格式為sign_up + NewWindow
    """
    #print(target.attrs)
    target_attrs_onclick = target['onclick']
    onclick_list =  target_attrs_onclick.split("\'")
    #print(onclick_list[1])
    target_url = sign_up + onclick_list[1]
    #print(target_url)

    #取得新網頁
    targer_page = requests.get(target_url)
    if targer_page.status_code == requests.codes.ok:
        target_soup = BS(targer_page.text, features="html.parser")
        #print(target_soup.prettify())
        