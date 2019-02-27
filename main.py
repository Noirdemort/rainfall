# command line tool for creating web app

import os
from templates.stub import *

print()
print("This is prototype platform, in nano stage!")

zest = input("Tell us your dream")

title = ''
tasks = []
zest = zest.split(' ')
for i in zest:
    if '#' in i:
        tasks.append(i.replace("#" ,''))
    if '@' in i:
        title = i.replace('@','')

print(tasks)
print(title)

os.system("mkdir {}".format(title))
os.system("mkdir {}/static".format(title))
for i in tasks:
    try:
        if i != 'server':
            with open("{}/static/{}.html".format(title, i), 'w') as f:
                touch = htmlTemplates[i]
                touch = touch.replace("{title}", title)
                f.write(touch)
        else:
            with open("{}/{}.js".format(title, i), 'a') as f:
                touch = server[i]
                touch = touch.replace("{title}", title)
                f.write(touch)
    except Exception:
        pass

if 'server' in tasks:
    tasks.remove('server')
    for i in tasks:
        with open('{}/server.js'.format(title), 'a') as f:
            f.write(server['add_page'].replace('{addHere}', i))


with open('{}/package.json'.format(title),'w') as f:
    package['name'] = title
    f.write("{")
    for i in package:
        f.write('"{}" : "{}",'.format(i, package[i]))
    f.write('"Author":""}')

