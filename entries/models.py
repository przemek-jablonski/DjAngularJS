from django.db import models

from authentication.models import UserAccount


class Entry(models.Model):
    # database modelling - posts belong to the UserAccount
    # and there can be many posts of given account
    # BRO TIP: now UserAccount is aware of Post(s), so we can call
    # 'UserAccount.post_set' to get them.
    author = models.ForeignKey(UserAccount)
    title = models.CharField(max_length=500)
    content = models.TextField()
    # content_short = models.TextField(default="asd")

    likes = models.IntegerField(default=1)
    saves = models.IntegerField(default=1)
    visits = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)
