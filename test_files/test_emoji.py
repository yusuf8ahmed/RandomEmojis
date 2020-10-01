import requests
from lxml import html

def test_emojipedia():
    url = "https://emojipedia.org/"
    r = requests.get("{}random/".format(url))
    root = html.fromstring(r.content)
    emoji = root.xpath('/html/body/div[2]/div[1]/article/h1/span/text()')[0]
    print(f">> {r.url} -> {emoji} <<")
    
test_emojipedia()