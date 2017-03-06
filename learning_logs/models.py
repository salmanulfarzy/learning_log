from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    markdown_field = MarkdownxField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."
