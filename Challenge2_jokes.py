#Challenge2_jokes.py
import requests
import json

api = "https://icanhazdadjoke.com/"
payload = {}
headers = {
    'Accept':'application/json'
}
while True:
    topic = input('\nPlease enter the topic of your joke, press enter for a random one, or q to end: ')
    if topic == 'q':
        break

    if topic == '':
        joke = requests.get(api,headers=headers)
        jsonJoke = joke.json()
        print()
        print(jsonJoke['joke'])

    elif topic != '':
        joke = requests.get(api+'/search?term='+topic,headers=headers)
        jsonJoke = joke.json()
        print()
        for i in range(len(jsonJoke['results'])):
            #print(jsonJoke['results'][0]['joke'])
            print(jsonJoke['results'][i]['joke'])

    else:
        print('Sorry, no jokes on that topic.')