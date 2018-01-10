curl https://www.bing.com >bing
egrep -o -e '"/az.*jpg"' bing >dest
head -1 dest > de
url=https://www.bing.com
echo $url>uri
cat de>>uri
tr -d '\n' <uri >urm
tr -d '"' <urm >ur
cat ur | xargs -0 curl >background.jpg
gsettings set org.gnome.desktop.background picture-uri file://$HOME/d.jpg
rm ur
rm urm
rm uri
rm de
rm dest
rm bing
