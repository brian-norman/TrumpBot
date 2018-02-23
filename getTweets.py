from sys import argv
import time
import json

from api import getAPI

REQUEST_DELAY = 5
MAX_REQUESTS = 20 # multiply this number by 20 and thats the number of tweets in the past

def main():
    try:
        count = 0

        #arg = argv[1]
        arg = "realDonaldTrump"
        api = getAPI()
        tweetResults = []

        tweetIndex = api.user_timeline(screen_name=arg, count=1)[0].id
        time.sleep(REQUEST_DELAY)
        for request in range(MAX_REQUESTS):
            tweets = api.user_timeline(screen_name=arg, include_retweets=False, max_id=tweetIndex, tweet_mode='extended')
            for tweet in tweets:
                count += 1
                tweetResults.append(tweet.full_text)
                tweetIndex = tweet.id
            time.sleep(REQUEST_DELAY)
        print("Number of tweets {}".format(str(count)))
    except IndexError:
        print("Program Missing Arg. Twitter Handle")
    except Exception as e:
        print("Program Failure.  Error: {}".format(e))
    finally:
        with open("{}Tweets".format(arg), 'w') as saveFile:
            json.dump(tweetResults, saveFile)
            print("File Saved.")

if __name__ == '__main__':
    main()
