from instapy import InstaPy

session = InstaPy(username="-", password="-")
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
