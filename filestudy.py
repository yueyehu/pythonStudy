import urllib

#conn = urllib.urlopen('http://thinkpython.com/secret.html')
conn = urllib.urlopen('http://docs.python.org/lib/module-urllib.html')
for line in conn:
    print line.strip()
