from os import system
from api import getAPI
from parser import list_of_words
import getTweets

tweet = "Trump's most used words:\n"

for i in range(len(list_of_words)):
	tweet += "{}: {} \n".format(list_of_words[i][0], list_of_words[i][1])

print("Updating log")
getTweets.main()

api = getAPI()
api.update_status(tweet)

print("Tweet printed")
