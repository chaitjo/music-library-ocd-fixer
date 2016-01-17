"""
Music Library OCD fixer by Chaitanya Joshi
"""

import os, sys, urllib2, eyed3, requests
from bs4 import BeautifulSoup


def getData(name):
	"""
	Method to make API queries using the name parameter, to fetch metadata.
	"""
	name = name.replace(' ', '+').replace('_', '+').lower()		#make name variable devoid of crap like [lyrics], [hd], etc.
	track_name = urllib2.urlopen("http://rhythmsa.ga/api.php?api=track_name&q={0}".format(name))
	artist_name = urllib2.urlopen("http://rhythmsa.ga/api.php?api=artist_name&q={0}".format(name))
	album_name = urllib2.urlopen("http://rhythmsa.ga/api.php?api=album_name&q={0}".format(name))
	track_lyrics = getLyrics(artist_name, track_name)		#Names should be properly formatted
	return ( unicode(track_name.read(),'utf-8'), unicode(artist_name.read(),'utf-8'), unicode(album_name.read(),'utf-8') )

def getLyrics(artistname, trackname):
	"""
	Method to extract lyrics of song from directlyrics.com
	"""
	artist_name = artistname
	track_name = trackname

	artistLi = artist_name.lower().split()
	trackLi = track_name.lower().split()

	link = "http://www.directlyrics.com/" 
	for el in range(0, len(artistLi)):
		link = link + artistLi[el] + "-" 
	for el in range(0, len(trackLi)):
		link = link + trackLi[el] + "-"
	link = link + "lyrics.html"

	r = requests.get("" + link)
	soup = BeautifulSoup(r.text,"html.parser")
	s = soup.get_text()

	startSearchString = artist_name + " \"" + track_name + "\"" " lyrics"
	endSearchString = "Suggest " + track_name + " lyrics corrections"
	adStartSearchString = "<!--"
	adEndSearchString = ">"
	indexStart = s.find(startSearchString)
	indexEnd = s.find(endSearchString)
	adStartIndex = s.find(adStartSearchString)
	adEndIndex = s.find(adEndSearchString)

	s = s[indexStart:adStartIndex] + s[adEndIndex +1:indexEnd]
	return s


def modify(folderPath):
	"""
	Method to update metadata and rename all mp3 files in folderPath.
	"""
	filesList = os.listdir(folderPath)
	pathsList = {}		#a dictionary mapping the name of a file to its complete path
	for file in filesList:
	    pathsList.update( {file[:-4] : folderPath+file} ) 

	for songName in pathsList.keys():
		song = eyed3.load(pathsList[songName])
		metadata = getData(songName)
		try:
			song.tag.title = metadata[0]
			song.tag.artist = metadata[1]
			song.tag.album = metadata[2]
			song.tag.save()
			os.rename(pathsList[songName], folderPath+song.tag.artist+' - '+song.tag.title+'.mp3')
			print("Updated '{0}'.".format(song.tag.artist+' - '+song.tag.title))
		except TypeError:
			print("No metadata found for '{0}'. Skipping it.".format(songName))
		except AttributeError:
			print("'{0}' is not an mp3 file. Skipping it.".format(songName))

if __name__=='__main__':
	print("\nHello! This script will fix your music collection and calm your iOCD down...\n")
	modify(sys.argv[1])
	print("\nAll done!\n")
