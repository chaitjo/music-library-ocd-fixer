import urllib2
import eyed3
import os
import sys

def getData(name):
	name = name.replace(' ', '+').replace('_', '+').lower()

	track_name = urllib2.urlopen("http://rhythmsa.ga/api.php?api=track_name&q={0}".format(name))
	artist_name = urllib2.urlopen("http://rhythmsa.ga/api.php?api=artist_name&q={0}".format(name))
	album_name = urllib2.urlopen("http://rhythmsa.ga/api.php?api=album_name&q={0}".format(name))

	return ( unicode(track_name.read(),'utf-8'), unicode(artist_name.read(),'utf-8'), unicode(album_name.read(),'utf-8') )

def modify(folderPath):
	filesList = os.listdir(folderPath)
	pathsList = {}
	for file in filesList:
	    pathsList.update( {file[:-4] : folderPath+file} ) 

	for songName in pathsList.keys():
		song = eyed3.load(pathsList[songName])
		metadata = getData(songName)

		song.tag.title = metadata[0]
		song.tag.artist = metadata[1]
		song.tag.album = metadata[2]
		song.tag.save()	
		os.rename(pathsList[songName], folderPath+song.tag.artist+' - '+song.tag.title+'.mp3')
		print("Updated '{0}'".format(song.tag.artist+' - '+song.tag.title))

if __name__=='__main__':
	print("\nHello! This script will fix your music collection and calm your iOCD down...\n")
	modify(sys.argv[1])
