from django.db import models
from django.contrib.auth.models import User

class Memory(models.Model):
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    to = models.TextField()

    def __unicode__(self):
        return self.body
