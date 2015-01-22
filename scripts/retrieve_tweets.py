from django.conf import settings
import twitter

api = twitter.Api(
        consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        access_token_key=settings.TWITTER_TOKEN,
        access_token_secret=settings.TWITTER_TOKEN_SECRET
)
statuses = api.GetUserTimeline(screen_name='MetroRailInfo')

print [s.text for s in statuses]
