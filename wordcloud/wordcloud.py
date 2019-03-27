import enchant
import matplotlib.pyplot as plt
import os
from os import path
import praw
import time
from collections import defaultdict, Counter
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import numpy as np


session = praw.Reddit(client_id=os.environ['REDDIT_CLIENT_ID'],
                      client_secret=os.environ['REDDIT_CLIENT_SECRET'],
                      user_agent=os.environ['REDDIT_USER_AGENT'],
                      username=os.environ['REDDIT_USER_NAME'],
                      password=os.environ['REDDIT_PASSWORD'])

stahp = set(STOPWORDS)


subreddit = session.subreddit('all')
seen_submissions = set()
dictionary = enchant.Dict("en_US")
word_dict = defaultdict(int)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
reddit_mask = np.array(Image.open(path.join(d, "reddit.png")))


for i in range(1):
    for submission in subreddit.top('hour', limit=10):
        if submission.fullname not in seen_submissions:
            seen_submissions.add(submission.fullname)
            for top_level_comment in submission.comments:
                for words in top_level_comment.body.split():
                    word = ''.join(e for e in words if e.isalnum() or e == "\'").lower()
                    if not word:
                        continue
                    if word not in stahp:
                        if dictionary.check(word):
                            if word in word_dict:
                                word_dict[word] += 1
                            else:
                                word_dict[word] = 1
    time.sleep(2)


wc = WordCloud(background_color="black",
               max_words=200,
               mask=reddit_mask,
               stopwords=stahp,
               contour_width=2,
               contour_color='blue')
               
wc.generate_from_frequencies(word_dict)

plt.imshow(wc, interpolation='bilinear')
plt.show()
