# Tweet-Count
A [twitter bot](https://twitter.com/SokasukiBot) that announces a user's most tweeted words.

## Usage
1. Run 'python3 tweetgenerator.py' and it will do all the work

## Notes
You'll need to [install tweepy](https://github.com/tweepy/tweepy), and put in [authentication info](https://www.digitalocean.com/community/tutorials/how-to-authenticate-a-python-application-with-twitter-using-tweepy-on-ubuntu-14-04) by putting your keys into twitterKeys.py 

## List of words I'm removing from the count:

'THE', 'TO', 'A', 'OF', 'IN', 'T', 'I', 'S', 'HTTPS', 'CO', 'FOR', 'AND',
'IS', 'IT', 'WILL', 'WITH', 'NOT', 'ON', 'BE', 'THAT', 'ARE', 'AT', 'YOU',
'HAVE', 'U', 'WAS', 'ALL', 'FROM', 'VERY', 'MY', 'THEY', 'WE', 'EVEN',
'OUR', 'SO', 'BY', 'AMP', 'THIS', 'ME', 'JUST', 'HE', 'NO', 'OR', 'BUT',
'SHOULD', 'HAS', 'DO', 'WHO', 'WHAT', 'AS', 'C', 'BEEN', 'WERE', 'AN', 'D',
'SAID', 'ABOUT', 'DID', 'MANY', 'INTO', 'WHEN', 'IF', 'ITS', 'THEIR', 'RT',
'AM', 'THAN', 'HAD', '00', 'M', 'MORE'
