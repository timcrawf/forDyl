import urllib
import re

class TwitterPage:
    def __init__(self, url):
        self.url=url
        self.tweets=self.twitterToArray(self.url)

    def printTweets(self):
        totalTweets=0
        for i in self.tweets:
            totalTweets += 1
            print "Tweet #%d:" % totalTweets
            print i+'\n'

    def removeEmptyItems(self, badArray):
        arrayToReturn=[]
        for item in badArray:
            if item!='':
                arrayToReturn.append(item)
        return arrayToReturn

    def twitterToArray(self, url):
        url = url
        htmlReturn = urllib.urlopen(url)
        html =  htmlReturn.readlines()
        finalArray = []
        randomHTML=["&#39;", "&#39;", "&quot;"]
        for line in html:
            if 'tweet-text' in line:
                lineWithoutHTML=re.sub(r'\<(.*?)\>', "", line)
                for randomCrap in randomHTML:
                    noRandomCrap=lineWithoutHTML.replace(randomCrap, '')
                if noRandomCrap!='':
                    finalArray.append(noRandomCrap.strip())
        arrayToReturn=self.removeEmptyItems(finalArray)
        return arrayToReturn
