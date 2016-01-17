# Overview
Music Library OCD fixer is a Python script that automatically fetches metadata for your music collection and renames files accordingly. It uses the <a href="http://rhythmsa.ga/">RhythSaga API</a> to fetch the metadata, a module called <a href="http://eyed3.nicfit.net/">eyeD3</a> to change ID3 tags for mp3 files, and a module called <a href="http://www.crummy.com/software/BeautifulSoup/">BeautifulSoup</a> to extract lyrics from a webpage.

**Inspiration- <a href="http://www.urbandictionary.com/define.php?term=iOCD">iOCD</a>**

# Usage
You must first install the eyeD3 and BeautifulSoup module using the following commands in a terminal:
```
pip install eyed3
pip install beautifulsoup4
```
Next, change directory to the location of `fix.py` and run the script using this: 
```
python fix.py [path to your music library]
```
An example-
```
cd /home/user/Music-Library-OCD-fixer/
```
```
python fix.py /home/user/Music/
```

# To-do
1. Add album art feature.
2. Make query used to fetch metadata smarter.
