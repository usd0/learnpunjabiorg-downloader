# imports requests library to interact with web interfaces
import requests

# iterates from 1-500 to download every file 
for iterate in range(1, 501):
    # states url name, putting the iterate variable in using f-strings, to iterate from 1-500 in the url
    url = f'https://www.learnpunjabi.org/stat_sound/{iterate}.wav'
    # asks to GET file
    r = requests.get(url, allow_redirects=True)
    # open .wav and save to disk
    open(f'{iterate}.wav', 'wb').write(r.content)
