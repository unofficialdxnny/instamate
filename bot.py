from instapy import InstaPy
from selenium import webdriver;


browser= webdriver.Firefox();
browser.get('http://www.instagram.com');


session = InstaPy(username="unofficialdxnny", password="husban1snaughtydaniadanial123321")
session.login()
session.like_by_tags(["javascript", "html", "css", "code", "java"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Cool"])
session.end()
