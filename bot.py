# made by unofficialdxnny
# @unofficialdxnny on Instagram
# dont repost without giving credits (dont be noob)




from instapy import InstaPy
from selenium import webdriver;


browser= webdriver.Firefox(); # opens FireFox browser (you will neeed to install it if you haveent already)
browser.get('http://www.instagram.com');


session = InstaPy(username="<not email ok>", password="<password>") # insert your creedentials here
session.login()
session.like_by_tags(["javascript", "html", "css", "code", "java"], amount=5) # this is the tags(#) that the bot will search for
session.set_dont_like(["naked", "nsfw"])# the tags that will be ignored :)
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Cool"]) # the stuff the bot will comment
session.end() # ends the session :)
