import sys
import os
import twint
from textgenrnn import textgenrnn

if len(sys.argv) > 1: username = sys.argv[1]
else:
    print("Please provide a twitter handle.\nExiting.")
    exit()

if len(sys.argv) > 2: tweet_limit = int(sys.argv[2])
else: tweet_limit = 1000

if len(sys.argv) > 3: num_epochs = int(sys.argv[3])
else: num_epochs = 5

temp_file = username + "_temp.csv"
print("Removing old tweet file.")
if os.path.exists(temp_file):
    os.remove(temp_file)

print("Fetching Tweets from " + username)
c = twint.Config()
c.Username = username
c.Store_csv = True
c.Custom["tweet"] = ["tweet"]
c.Output = temp_file
c.Limit = tweet_limit
c.Retweets = False
c.Replies = False
twint.run.Search(c)

print("\n\n\n\n-----------------------------------")
print(c.Limit, "tweets fetched from", username)

print("Training language model.")
textgen = textgenrnn()
textgen.train_from_file(temp_file, num_epochs=num_epochs)

print("\n\n\n\n-----------------------------------")
print("Generating some new tweets!")
textgen.generate(10)
