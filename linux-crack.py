#!/usr/bin/python

#felipesi - 2020

import crypt
import sys

name = sys.argv[0]

if len(sys.argv) <= 2:
    print 'USAGE: %s shadow-file wordlist.txt' %name
    print 'EXAMPLE: %s /etc/shadow rockyou.txt' %name
    sys.exit(1)

fileshadow = sys.argv[1]
dic = sys.argv[2]

for line in open(fileshadow):
    line = line.rstrip()
    if '$' in line:
        senha = line.split(':')[1]
        id = line.split('$')[1]
        salt = '$' + id + '$' + line.split('$')[2]
        user = line.split(':')[0]

        f = open(dic, 'r')
        for x in f.readlines():
            x = x.rstrip()
            hash = crypt.crypt(x, salt)
            if (hash == senha):
                print 'PASSWORD FOUND ==> %s:%s' %(user,x)
                break
