from django.db import models


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.TextField()

    def __str__(self):
        return self.content

    def update_counter(self):
        print(f"Counter updated")
