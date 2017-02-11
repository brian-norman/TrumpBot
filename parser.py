import json
import re
from collections import Counter

total_words = []
filter_words = ['THE', 'TO', 'A', 'OF', 'IN', 'T', 'I', 'S', 'HTTPS', 'CO', 'FOR', 'AND',
				'IS', 'IT', 'WILL', 'WITH', 'NOT', 'ON', 'BE', 'THAT', 'ARE', 'AT', 'YOU',
				'HAVE', 'U', 'WAS', 'ALL', 'FROM', 'VERY', 'MY', 'THEY', 'WE', 'EVEN',
				'OUR', 'SO', 'BY', 'AMP', 'THIS', 'ME', 'JUST', 'HE', 'NO', 'OR', 'BUT',
				'SHOULD', 'HAS', 'DO', 'WHO', 'WHAT', 'AS', 'C', 'BEEN', 'WERE', 'AN', 'D',
				'SAID', 'ABOUT', 'DID', 'MANY', 'INTO', 'WHEN', 'IF', 'ITS', 'THEIR', 'RT',
				'AM', 'THAN', 'HAD', '00', 'M', 'MORE']

with open('realDonaldTrumpTweets') as json_data:
	d = json.load(json_data)
	for i in range(len(d)):
		tweet = d[i]
		words = re.findall(r'\w+', tweet) #Finds words in sentence
		for word in words:
			total_words.append(word)

cap_words = [word.upper() for word in total_words] #Capitalizes all words
word_counts = Counter(cap_words) #Counts number of times word appears

for word in filter_words:
	word_counts[word] = 0

list_of_words = word_counts.most_common(10)

