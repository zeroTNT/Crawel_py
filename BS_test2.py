import requests
from bs4 import BeautifulSoup as BS
import re

target = "【線上多元學習通識】生醫材料解密"
sign_up = "https://aps.ncue.edu.tw/sign_up/"
acticities_url = "https://apss.ncue.edu.tw/sign_up/index.php"
my_params = {"keyword" : target}
search = requests.get(acticities_url, params=my_params)

if search.status_code == requests.codes.ok:
    soup = BS(search.text, features="html.parser")
    #print(soup.prettify())

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
        fun = target_soup.find("script")
        fun = fun.text
        fun = fun.split("\'")
        #print(fun[1])
        personal_url = sign_up+fun[1]
        print(personal_url)
        personal_page =  requests.get(personal_url)
        if personal_page.status_code == requests.codes.ok:
            personal_soup = BS(personal_page.text, features="html.parser")
            bottom = personal_soup.find("img")
            #print(personal_soup.prettify())