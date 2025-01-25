import praw # Reddit API wrapper
import config # Configuration file
import time # Time module
import os # OS module

def bot_login(): #create a Reddit instance
    print("Logging in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "n0aheuw dog and cat comment responder v0.1")
    print("Logged in!")

    return r

def get_saved_comments(): #function to get the comments that have already been replied to

    if not os.path.isfile("replied_comments.txt"): #check if the file exists and if not create it
        with open("replied_comments.txt", 'x') as file:
            comments_replied_to = []
    else:
        with open("replied_comments.txt", "r") as file: #open the file in read mode and read the comments commented on
            comments_replied_to = file.read()
            comments_replied_to = comments_replied_to.split("\n")

    return comments_replied_to #return the list of comments replied to

#function to run the bot
def run_bot(r):

    print("Obtaining 10 comments...")
    for comment in r.subreddit('test').comments(limit=10): #check for comments in the subreddit

        if comment.id not in comments_replied_to and comment.author != r.user.me(): #check if the comment has already been replied to and if the comment is not made by the bot itself
            #check for different instances of cat and dog mentions
            if ("dog" in comment.body) & ("cat" in comment.body):
                print("String with \"dog\" \"cat\" found in comment " + comment.id)
                comment.reply("You summoned the cat and dog! [Here](https://i.imgur.com/XiyeGgN.jpeg) they are :)")
            elif "dog" in comment.body:
                print("String with \"dog\" found in comment " + comment.id)
                comment.reply("I love Goofy Dogs! [Here](https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fhappy-goofy-shiba-v0-pwuncz0g90jb1.jpg%3Fauto%3Dwebp%26s%3Db6d60128b3a2bc979b84ec372c4ab114730bbd9f) is an image of one :)")
            elif "cat" in comment.body:
                print("String with \"cat\" found in comment " + comment.id)
                comment.reply("Cat? Where? [Here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHz4zJFmNhrBqYd-tbdiw_og5CrCQcv207NQ&s) is a cat for you :)")
            
            #adds the comment id to the list of comments replied to
            comments_replied_to.append(comment.id)

            #write the comment id to the file
            with open("replied_comments.txt", "a") as file:
                file.write(comment.id + "\n")

    print ("Sleeping for 10 seconds...")
    #sleep for 10 seconds
    time.sleep(10)

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(r)
