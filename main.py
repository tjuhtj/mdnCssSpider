# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
import os
import requests
import json
from bs4 import BeautifulSoup
import lxml


def getHtml(url):
    # Use a breakpoint in the code line below to debug your script.
    dict = {}
    requests_headers = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Referer": "https://developer.mozilla.org/en-US/docs/Web/CSS",
        "Connection": "keep-alive"
    }
    url_str = "https://developer.mozilla.org/en-US/docs/Web/CSS/{}".format(str(url))
    resp = requests.get(url=url_str, headers=requests_headers)
    status_code = resp.status_code
    if status_code == 200:
        html_text = resp.text
    else :
        return "none"
    soup = BeautifulSoup(html_text, 'lxml')  # html.parser/lxml
    direction = soup.select_one(".section-content").get_text()
    syntax = soup.select_one("#content > article > section:nth-child(8) > div > pre")
    if syntax != None:
        syntax = syntax.get_text()
    else:
        syntax = "none"
    valuesFrom = soup.find_all(name='dt')
    values = [0] * len(valuesFrom)
    for i in range(len(valuesFrom)):
        values[i] = valuesFrom[i].get_text()
    initial = soup.select_one("#content > article > section:nth-child(6) > div > div > table > tbody > tr:nth-child(1) > td")
    if initial != None:
        initial = initial.get_text()
    else:
        initial = "none"
    dict["description"] = direction
    dict["syntax"] = syntax
    dict["values"] = values
    dict["initial"] = initial
    dict["name"] = url
    dict["reference"] = [
        {
                    "name": "MDN Reference",
                    "url": url_str
                }
    ]
    return dict


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dict = []
    url_list = ["right",
  "bottom",
  "left",
  "word-spacing",
  "text-overflow",
  "max-lines",
  "border-color",
  "border-top-color",
  "border-right-color",
  "border-bottom-color",
  "border-left-color",
  "border-top-right-radius",
  "border-top-left-radius",
  "border-bottom-right-radius",
  "border-bottom-left-radius"]
    file = open('cssName.json', 'r', encoding='utf-8')
    root = json.load(file)
    root = root["lastCss"]
    file.close()
    url_list = root
    for url in url_list:
        dict.append(getHtml(url))
        time.sleep(5)
    file = open('result.json', 'w', encoding='utf-8')
    file.write(json.dumps(dict))
    file.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
