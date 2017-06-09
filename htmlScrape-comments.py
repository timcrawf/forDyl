## I did this with python 2.7 like an idiot, but hopefully it makes sense
## Obviously this isn't the only way, I'm just trying to show that it's doable
## with much less overhead

import urllib #for getting the html from the link
import re #regular expression library. We'll talk about this later. But look it
          #up it's tight as shit.

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
        htmlReturn = urllib.urlopen(url) #Return the html object
        ## the object has a few different functions you can see using

        #method for method in dir(htmlReturn) if callable(getattr(htmlReturn, method))]

        #or read the docs

        ## this function .readlines() takes each line and and makes an array
        ## you can also do .read() to get a single string

        html =  htmlReturn.readlines()
        finalArray = []
        randomHTML=["&#39;", "&#39;", "&quot;"] # after getting the tweets parsed out I noticed
        # there was still some random junk, this is to pull those out
        for line in html:
            ## I dug around in twitters HTML and saw that every tweet belongs to
            ## the CSS class tweet-text so i used that to find and pull out the
            ## tweets
            if 'tweet-text' in line:
                lineWithoutHTML=re.sub(r'\<(.*?)\>', "", line) # this is the
                # regular expresion \<(.*?)\>'

                ## it finds and instance of any characters with <> around it
                ## this will remove all the html elements eg. <div></div>

                for randomCrap in randomHTML:
                    ## replacing all the random crap with nothing
                    noRandomCrap=lineWithoutHTML.replace(randomCrap, '')
                if noRandomCrap!='':
                    ## some empty items snuck
                    finalArray.append(noRandomCrap.strip())
        ## last stop get to remove empty items
        arrayToReturn=self.removeEmptyItems(finalArray)
        return arrayToReturn

def main():
    print "My Twitter"
    ## create Object
    timTwitter = TwitterPage("https://twitter.com/timcrawford88")
    ## call function to print tweets
    timTwitter.printTweets()

    print "Ashton's Twitter"
    ashtonTwitter = TwitterPage("https://twitter.com/aplusk")
    ashtonTwitter.printTweets()

## starts up the program

if __name__=="__main__":
    main()

## As I'm sure you can see, this is a mess, but I think it can get my point across
## A library could do this, sure, but unless you are going to use the api it will
## Be doing something exactly like this at the base level, but it will also have
## a bunch of other stuff that will add crazy over head to your program.
## All with 2 built in low level libraries
