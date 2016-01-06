import urllib2
import eyed3

def getData(name):
	name = name.replace(' ', '+').replace('_', '+').lower()

	track_name = urllib2.urlopen("http://rhythmsa.ga/api.php?api=track_name&q={0}".format(name))
	artist_name = urllib2.urlopen("http://rhythmsa.ga/api.php?api=artist_name&q={0}".format(name))
	album_name = urllib2.urlopen("http://rhythmsa.ga/api.php?api=album_name&q={0}".format(name))

	return ( unicode(track_name.read(),'utf-8'), unicode(artist_name.read(),'utf-8'), unicode(album_name.read(),'utf-8') )

data=getData("sexy back")
print(data)

path="/home/chait/Music/Sexy Back - Justin Timberlake.mp3"
song = eyed3.load(path)

song.tag.title = data[1]
song.tag.save()