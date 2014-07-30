__author__ = 'd3non'

from c3daysleft import sleep, twitter, get_teweet, get_format
from c3daysleft import SLEEP_MAX, SLEEP_MIN, OAUTH_FILE

import bot_apikeys


if __name__ == "__main__":
    sleep(SLEEP_MIN, SLEEP_MAX)
    oauth = twitter.read_token_file(OAUTH_FILE)
    t = twitter.Twitter(auth=twitter.OAuth(oauth[0], oauth[1], bot_apikeys.CONSUMER_KEY, bot_apikeys.CONSUMER_SECRET))
    text = get_teweet().format(**get_format())
    print("tweeting: %s" % text)
    t.statuses.update(status=text)