### reddit_comment_nuker/reddit.py

A quick python script I threw together that will nuke all of the comments on your account.
In order to use this script, you will need to do the following:

- Use the [following instructions and setup a Script Application to your Reddit account](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application)
- Install PRAW with `pip install praw`
- Set the following env vars 
  - `REDDIT_CLIENT_ID` - The id you get from setting up your script application
  - `REDDIT_CLIENT_SECRET` - The secret key that you get from setting up your script application
  - `REDDIT_USER_AGENT` - A description of your application 
  - `REDDIT_USER_NAME` - Your reddit username
  - `REDDIT_PASSWORD` - The password for your user account. 

If Everything is set, simply run `python reddit.py` and wait. The script doesn't output anything but if it is working you should begin to see sequential comments deleted from your account. 

### flashcards/flash.py

A flashcard application I made for myself when I was bored. It hits the google translate API and generates random flashcards for you. 

Setup Documentation coming when I have free time (which is never). 

### wordcloud/wordcloud.py

A wordcloud generator that I made when I was bored. It scrapes Reddit and grabs the most frequent words for the past hour from top level comments and then creates a wordcloud from that. 

Documentation for setup coming when I have free time (which is never). 

Eventually, I will get around to documenting the rest of this. I hope. 
