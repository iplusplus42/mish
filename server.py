'''
    mish - server.py
    Contains all functions for controlling Minecraft servers
'''

### sdl imports ###
import os
import sys
import json

### Minecraft imports ###
from mcstatus import MinecraftServer
import MCRcon.mcrcon as mcrcon

### Other imports ###
import psutil
import bitmath
import wget
import libtmux

class MCServerDL(object):
    def __init__(self, version):
        with open('mcservers.json', 'r') as fd:
            mcservers = json.load(fd)
            # if version in
            wget.download('https://s3.amazonaws.com/Minecraft.Download/versions/{version}/minecraft_server.{version}.jar'.format(version=version))


def server_dl(server, version):
    pass

def server_dl_configure(server, version):
    pass

def server_start(server, **kwargs):
    pass

def server_stop(server):
    pass

def server_rcon(server, cmd, **kwargs):
    pass

def server_plugins(server):
    pass

def server_plugin(server, plugin):
    pass
