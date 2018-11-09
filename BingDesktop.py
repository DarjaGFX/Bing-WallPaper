import os
import re

os.system('curl https://www.bing.com/ > htm')
html = open('htm','r')
html = html.read()
pattern = r'"/az/.*jpg"'
imurl = (re.findall(pattern,html))[0].replace("\"","")
url = "http://bing.com"+imurl
os.system('wget '+url)
imurl = imurl.split('/')
FileName = imurl[-1]
pwd = os.getcwd()
pwd = pwd.replace('\n','').replace(' ','\ ')
os.system('gsettings set org.gnome.desktop.background picture-uri file://'+pwd+'/'+FileName)
os.system("rm htm")
