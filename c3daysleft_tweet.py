#!/bin/env python3
import twitter
import bot_apikeys
import datetime
import random

OAUTH_FILE="account.oauth"
NEXTC3_DATE=datetime.date(2014,12,27)
TWEET_TEXTS=(
	"Goooood Mooooorning, Twietnaaam! On this lovely day, there are only %s days left until #31C3",
	"What a nice day! And wow, only %s days remain until #31C3 starts! #anticipation",
	"I'm very pleased to remind you that #31C3 will take place in only %s days!",
	"Bugged by all those strange people out there? Chin up, #31C3 will start in only %s days!! :)",
	"%s days remaining!! Wooohoooo :D #31C3",
	)
for i in range(20):
	TWEET_TEXTS.append("Only %s days left until #31C3")
TWEET_SPECIAL={
	356: "So, the first Sunday after #30C3. Is your sleep cycle still as out of whack as mine? We have 356 days to recover until #31C3 starts :D",
	348: "Day 4 of #30C3 was two weeks ago! That leaves only 355 days until #31C3 \o/",
	341: "Oh yea, only b'101010101 days left until #31C3",
	}
MIN_SLEEP=60*30
MAX_SLEEP=3600*23
LOGFILE="c3daysleft_tweet.log"

def mylog(msg):
    f = open(LOGFILE,"a+")
    f.write("%s: %s\n" % (datetime.datetime.now().strftime("%x %X"),msg) )
    f.close()

if __name__ == "__main__":
    if MIN_SLEEP and MAX_SLEEP and (MAX_SLEEP > MIN_SLEEP):
        from time import sleep
        sleeptime=random.randint(MIN_SLEEP,MAX_SLEEP)
        mylog("sleeping for %ss" % sleeptime)
        sleep(sleeptime)
    oauth=twitter.read_token_file(OAUTH_FILE)
    t=twitter.Twitter(auth=twitter.OAuth(oauth[0], oauth[1],
	bot_apikeys.CONSUMER_KEY, bot_apikeys.CONSUMER_SECRET))
    daysleft = (NEXTC3_DATE - datetime.date.today()).days
    if daysleft in TWEET_SPECIAL:
        text = TWEET_SPECIAL[daysleft]
    else:
        text = TWEET_TEXTS[random.randint(0, len(TWEET_TEXTS) - 1)] % daysleft
    mylog("tweeting: %s" % text)
    t.statuses.update(status=text)
