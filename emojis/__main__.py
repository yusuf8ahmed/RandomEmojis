# Copyright 2020 chromazmoves
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import click
import requests
from lxml import html

# def random_emoji(number=1, no_url=False):
#   # used for python scripting
#   emojis_list = []
#   emoji_url = []
#   for x in range(number):
#     url = "https://emojipedia.org/"
#     r = requests.get("{}random/".format(url))
#     root = html.fromstring(r.content)
#     emoji = root.xpath('/html/body/div[3]/div[1]/article/h1/span/text()')[0]
#     emojis_list.append(emoji)
#     if no_url:
#       emoji_url.append(r.url)
#   if no_url:
#     return [ emojis_list, emoji_url ]
#   else:
#     return emojis_list


def emoji_cli(number=1, link=False, verbose=False):
    # used in cli
    for x in range(number):
        url = "https://emojipedia.org/"
        r = requests.get("{}random/".format(url))
        root = html.fromstring(r.content)
        emoji = root.xpath('/html/body/div[2]/div[1]/article/h1/span/text()')[0]
        if verbose:
            click.echo(f"INFO: {len(emoji)}")

        if link:
            click.echo(f">> {r.url} -> {emoji} <<")
        else:
            click.echo(f">> {emoji} <<")


@click.command()
@click.argument('number', default=1)
@click.option('--link', '-l', is_flag=True, help="display generated emoji(s) url")
@click.option('--verbose', '-v', is_flag=True, help="show verbose messages")
def cli(number, link, verbose):
    """Emojis: generates random emojis duh"""
    if verbose:
        click.echo(f"INFO: emojis might not be visible")
    emoji_cli(number=number, link=link, verbose=verbose)


if __name__ == '__main__':
    cli()
