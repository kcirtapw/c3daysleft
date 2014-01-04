#!/bin/env python3
import twitter
import bot_apikeys
import datetime
import random

OAUTH_FILE="account.oauth"
NEXTC3_DATE=datetime.date(2014,12,27)
TWEET_TEXTS=(
	"Only %s days left until #31C3",
#	"",
	)
TWEET_SPECIAL={
	356: "So, the first sunday after the #30C3. Is your sleep cycle still as fucked up as mine? We have 356 days to recover until the #31C3 starts :D",
	348: "Day 4 of the #30C3 is already two weeks ago! That leaves us only 355 days left until #31C3 \o/",
	341: "Oh yea, only b'101010101 days left until #31C3",
	}

if __name__ == "__main__":
    oauth=twitter.read_token_file(OAUTH_FILE)
    t=twitter.Twitter(auth=twitter.OAuth(oauth[0], oauth[1], 
	bot_apikeys.CONSUMER_KEY, bot_apikeys.CONSUMER_SECRET))
    daysleft = (NEXTC3_DATE - datetime.date.today()).days
    if daysleft in TWEET_SPECIAL:
        text = TWEET_SPECIAL[daysleft]
    else:
        text = TWEET_TEXTS[random.randint(0, len(TWEET_TEXTS) - 1)] % daysleft
    t.statuses.update(status=text)
