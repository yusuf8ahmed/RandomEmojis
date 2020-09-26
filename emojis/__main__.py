import sys
import click
import requests
from lxml import html

def random_emoji(number=1, no_url=False):
  # used for python scripting
  emojis_list = []
  emoji_url = []
  for x in range(number):
    url = "https://emojipedia.org/"
    r = requests.get("{}random/".format(url))
    root = html.fromstring(r.content)
    emoji = root.xpath('/html/body/div[3]/div[1]/article/h1/span/text()')[0]
    emojis_list.append(emoji)
    if no_url:
      emoji_url.append(r.url)
  if no_url:
    return [ emojis_list, emoji_url ]
  else:
    return emojis_list

def emoji_cli(number=1, link=False):
  # used in cli
  for x in range(number):
    url = "https://emojipedia.org/"
    r = requests.get("{}random/".format(url))
    root = html.fromstring(r.content)
    emoji = root.xpath('/html/body/div[3]/div[1]/article/h1/span/text()')[0]
    print(f"INFO: {len(emoji)}")
    if link:
        click.echo(f"|> {r.url} -> {emoji} <|")
    else:
        click.echo(f"|> {emoji} <|")

@click.command()
@click.argument('number', default=1)
@click.option('--link', '-l', is_flag=True, help="display generated emoji(s) url")
def main(number, link):
    """Emojis: generates random emojis duh"""
    print(f"INFO: Flag emojis might not be visible")
    emoji_cli(number=number, link=link)

if __name__ == '__main__':
    main()