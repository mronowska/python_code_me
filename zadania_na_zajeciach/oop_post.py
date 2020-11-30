import datetime


class Post:
    media = "facebook"

    def __init__(self, author, content, location, access_level="friends_only"):
        self.author = author
        self.date = datetime.datetime.now()
        self.content = content
        self.localization = location
        self.reactions = 0
        self.comments = []
        self.access_level = access_level
        self.is_published = False

    def edit(self, content):
        if content.strip() == "":
            raise ValueError("Nie możesz edytować posta na pusty")
        self.content = content

    def add_comment(self, comment_text):
        self.comments.append(comment_text)

    def add_like(self):
        self.likes += 1

    def send(self):
        self.is_published = True



first_post = Post("Monia", "To jest mój post", "Gdańsk")
sec_post = Post("Andrzej", "To mój poscik", "Montreal")
first_post.edit("hej hej zmiana posta zmiana treści")