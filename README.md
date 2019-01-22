# twot
_A very easy twitter robot for tweet generation_

---
This small python script fetches a number of tweets from a given username and trains a neural network to generate text based on those tweets.

Uses `twint` for fetching tweets and `textgenrnn` for the fancy neural network part.

Use example: `python3 twot.py Kristianthdahl 1000 5`:
- `Kristianthdahl` is the twitter handle
- `1000` is the number of tweets to fetch
- `5` is the number of epochs to train the model for

The last two can be omitted.
