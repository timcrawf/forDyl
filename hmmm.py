import htmlScrape


def main():
    print "My Twitter"
    timTwitter = htmlScrape.TwitterPage("https://twitter.com/timcrawford88")
    timTwitter.printTweets()

    print "Ashton's Twitter"
    ashtonTwitter = htmlScrape.TwitterPage("https://twitter.com/aplusk")
    ashtonTwitter.printTweets()

if __name__=="__main__":
    main()
