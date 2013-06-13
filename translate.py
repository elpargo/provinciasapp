#!/usr/bin/python
# vim: set fileencoding=UTF-8 :

replaces = {
'&aacute;':'á',
'&eacute;':'é',
'&iacute;':'í',
'&oacute;':'ó',
'&uacute;':'ú',
'&ntilde;':'ñ',
'&nbsp;':'', #we got some trailing spaces in the file
}

print "Processing provincias_dirty.json"
with open('provincias_dirty.json') as f:
    data = f.read()
    for src,dst in replaces.items():
        data = data.replace(src,dst)
    with open("provincias.json","w") as n:
        n.write(data)
        print "writting provincias.json"
