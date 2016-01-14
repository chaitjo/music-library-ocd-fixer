# Overview
Music Library OCD fixer is a Python script that automatically fetches metadata for your music collection and renames files accordingly. It uses the <a href="http://rhythmsa.ga/">RhythSaga API</a> to fetch the metadata and <a href="http://eyed3.nicfit.net/">eyeD3</a> to change ID3 tags for mp3 files.

Inspiration- <a href="http://www.urbandictionary.com/define.php?term=iOCD">iOCD</a>

# Usage
You must first install the eyeD3 Python module using the following command in a terminal:
```
pip install eyed3
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
1. Add album art update feature.
2. Make query used to fetch metadata smarter.
