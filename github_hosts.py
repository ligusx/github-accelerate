#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import socket
import os
import sys


file_path = os.path.split(os.path.realpath(__file__))[0]

def get_ip(host):
    """
    Get ip of host.
    """
    try:
        host_ip = socket.gethostbyname(host)
        return host_ip
    except:
        print("Unable to get IP of Hostname")
        
def main():
    f = open('%s/hosts-tmp' % file_path,'w')
    f.write("github.com\n")
    f.write("gist.github.com\n")
    f.write("assets-cdn.github.com\n")
    f.write("raw.githubusercontent.com\n")
    f.write("gist.githubusercontent.com\n")
    f.write("cloud.githubusercontent.com\n")
    f.write("camo.githubusercontent.com\n")
    f.write("avatars0.githubusercontent.com\n")
    f.write("avatars1.githubusercontent.com\n")
    f.write("avatars2.githubusercontent.com\n")
    f.write("avatars3.githubusercontent.com\n")
    f.write("avatars4.githubusercontent.com\n")
    f.write("avatars5.githubusercontent.com\n")
    f.write("avatars6.githubusercontent.com\n")
    f.write("avatars7.githubusercontent.com\n")
    f.write("avatars8.githubusercontent.com\n")
    f.write("github.githubassets.com\n")
    f.write("github.global.ssl.fastly.net\n")
    f.write("documentcloud.github.com\n")
    f.write("gist.github.com\n")
    f.write("help.github.com\n")
    f.write("nodeload.github.com\n")
    f.write("codeload.github.com\n")
    f.write("status.github.com\n")
    f.write("training.github.com\n")
    f.close()

if __name__ == "__main__":
    main()

def main():
    f = open('%s/hosts' % file_path,'w')
    f.write("127.0.0.1 localhost\n")
    f.write("\n")
    f.write("#github accelerate\n")
    f.write("\n")
    f.write("# GitHub Start\n")
    f.close()

    with open("%s/hosts-tmp" % file_path, "r") as ins:
        for host in ins:
            ip=get_ip(host.strip())
            with open('%s/hosts' % file_path, 'a') as result:
                result.write(ip.strip('\n') + " " + host)

    f = open('%s/hosts' % file_path,'a')
    f.write("\n# GitHub End\n")
    f.close()

if __name__ == "__main__":
    main()