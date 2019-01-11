#Twitter api using textblob!


from textblob import TextBlob
import tweepy 

sent=TextBlob("i am a sad person")
print(sent.tags)#gives the parts of speech of each word
print(sent.words)#tokenize the text
print(sent.polarity)#more close to 1 then happy otherwise sad


#lets pull the tweets from twitter
#tweepy is for accessing the twitter api

consumer_api_key='fW9MFUMncimFX6cAxLTSu3pCx'
consumer_api_secret_key='r0accpkqaPmjarMORX0aZY89VEEDKaC6drnfDVu8lxd38nnOLz'

access_token_key='1007314556094279681-3SlZP3iDZHiFxr3m1ZGngYtfJTOniv'
access_token_secret_key='qd0sTo9Bjo0jKQhYMRpqylRCiDAKIih1DFhEwwonM0lm7'

auth=tweepy.OAuthHandler(consumer_api_key,consumer_api_secret_key)
auth.set_access_token(access_token_key,access_token_secret_key)

api=tweepy.API(auth)

#we can now create delete or update any tweets!

all_tweets=api.search('car')#gets all the tweets having car as a word

file=open("tweetdata.txt",'w')

for tweet in all_tweets:
	print(tweet.text)
	sent=TextBlob(tweet.text)
	data=(tweet.text).encode('utf-8')
	file.write(data)
	if sent.polarity > 0:
		file.write("good")
	else:
		file.write("bad")
	file.write("\n")


