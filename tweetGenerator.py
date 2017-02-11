from api import getAPI
from parser import list_of_words

tweet = "Trump's most used words:\n"

for i in range(len(list_of_words)):
	tweet += "{}: {} \n".format(list_of_words[i][0], list_of_words[i][1])

api = getAPI()
api.update_status(tweet)

print(tweet)
