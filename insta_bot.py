from instapy import InstaPy

session = InstaPy(username="chickenjunjj@gmail.com", password="Jojon524")
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)