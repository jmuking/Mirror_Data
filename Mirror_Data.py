#AUTHOR : Jeffrey King
#ORG : University of Missouri
#CLASS : ECE 3110
#DATE : 03/19/2017

import os
import json
import datetime
import urllib

#--
#First Time Setup - Comment this out if you've already ran this code once
#urllib.urlretrieve('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')
#os.system('python get-pip.py')
#os.system('pip install requests')
#--

import requests

class Mirror_Data:
    news_articles = 0
    idx = 0
    
    weather_simple = 0
    weather_main = 0
    weather_wind = 0

    def __init__(self, ID):
        self.idx = 0
        self.refreshWeather()
        self.refreshNews()
        return

    def getHour(self):
        return (datetime.datetime.now()).hour

    def getMinute(self):
        return (datetime.datetime.now()).minute

    def getSecond(self):
        return (datetime.datetime.now()).second

    def getMicrosecond(self):
        return (datetime.datetime.now()).microsecond

    def getDay(self):
        return (datetime.datetime.now()).day

    def getMonth(self):
        return (datetime.datetime.now()).month

    def getYear(self):
        return (datetime.datetime.now()).year

    def getTime(self):
        hour = self.getHour()
        minute = self.getMinute()
        
        if(self.getHour() <= 12):
            t = "%02d" % hour + ':%02d' % minute + ' AM'
        else:
            t = "%02d" % (hour%12) + ':%02d' % minute + ' PM'
        return t

    def getDate(self):
        d = "%02d" % self.getMonth() + '/%02d' % self.getDay() + '/%04d' % self.getYear()
        return d

    def refreshWeather(self):
        payload = {'q': 'Columbia,MO', 'APPID': 'e07ce0f12402f2cdff109e85d21fa1fd'}
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?', params=payload)
        j = json.loads(r.text)

        self.weather_simple = j['weather'][0]
        self.weather_main = j['main']
        self.weather_wind = j['wind']
        return

    def getTemp(self):
        temp = (float(self.weather_main['temp'])-273)*(9/5) + 32
        minTemp = (float(self.weather_main['temp_min'])-273)*(9/5) + 32
        maxTemp = (float(self.weather_main['temp_max'])-273)*(9/5) + 32

        temperature = [temp,minTemp,maxTemp]
        return temperature

    def getHumidity(self):
        humidity = float(self.weather_main['humidity'])
        return humidity

    def getWind(self):
        windSpeed = float(self.weather_wind['speed'])
        windDir = me.degToCompass(float(self.weather_wind['deg']))

        wind = [windDir,windSpeed]
        return wind

    def degToCompass(self, num):
        val = int((num/22.5)+.5)
        arr = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
        return arr[(val % 16)]

    def refreshNews(self):
        payload = {'source': 'google-news', 'apiKey': '4ad93627c6964fc798a75dc366049bed'}
        r = requests.get('https://newsapi.org/v1/articles?', params=payload)
        j = json.loads(r.text)

        self.articles = j['articles']
        return

    def nextArticle(self):
        title = self.articles[self.idx]['title']
        desc = self.articles[self.idx]['description']
        self.idx = (self.idx+1)%len(self.articles)

        hl = [title,desc]
        return hl
