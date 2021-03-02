import tweepy

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

userID = input("Give User ID:")
user = api.get_user(userID)

tweets = api.user_timeline(screen_name=userID,count=200,include_rts = False,tweet_mode = 'extended')

entiretext = []

for info in tweets[:10]:
    tmpinfo = info.full_text
    tmptxt = tmpinfo.split()
    entiretext.extend(tmptxt)

entiretext.sort(key=len)
print("the 5 shortest words are:")

for i in entiretext[:5]:
    print(i)

print("the 5 longest words are:")
for i in entiretext[-5:]:
    print(i)
