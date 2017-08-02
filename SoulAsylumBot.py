import praw
import pdb
import re
import os 

#We create a Reddit instance using the values we saved under bot1.
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))


for submission in subreddit.hot(limit=5):
	if submission.id not in posts_replied_to:
		if re.search("runaway train", submission.title, re.IGNORECASE):
			submission.reply('''SoulAsylumDefenseBot says:
			I think you should revisit some of Soul Asylum's early albums from the 80s.  They had a string of really
			increadible work, including several albums produced by Bob Mould of Husker Du. They were a dirty punk band
			for a decade before they made it big with Runaway Train. 
			''')
			print("Bot replying to : ", submission.title)
			posts_replied_to.append(submission.id)
			

with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id+"\n")