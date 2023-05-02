#!/usr/bin/env python

import requests, os, argparse, shutil

from transmission_rpc import Client
from configparser import ConfigParser

config = ConfigParser()

# If there's no config file, clone example

if not os.path.isfile('config.ini'):
    shutil.copyfile('config.ini.example','config.ini')

# Open config
config.read('config.ini')

# Auth on server
client = Client(host=config['auth']['host'],\
                port=config['auth']['port'],\
                username=config['auth']['user'],\
                password=config['auth']['pass'])

# Functions
def list_all_torrents():
    torrents = client.get_torrents()
    for torrent in torrents:
        print(":: Information:")
        print(f" Hash  : {torrent.hashString}")
        print(f" Name  : {torrent.name[:40]}")
        print(f" Dir   : {torrent.download_dir}")
        print(f" Added : {torrent.added_date}")
        print(":: Properties:")
        print(f" Now   : {torrent.status}")
        print(f" Ratio : {torrent.ratio}")
        print(f" ID    : {torrent.id}")
        print(":: Limits:")
        print(f" Ratio Limit: {torrent.seed_ratio_limit}")
        print(f" Ratio Mode : {torrent.seed_ratio_mode}")
        print("--------------")

# Main parser
parser = argparse.ArgumentParser(
                    prog='Gearbox Lever',
                    description='Terminal utility to manage Transmission BitTorrent Client',
                    epilog="this program it's on alpha state")

parser.add_argument('list', action=list_all_torrents())

args = parser.parse_args()
