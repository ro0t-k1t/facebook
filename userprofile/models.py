from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    rel_status = models.CharField(max_length=50)
    living = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    status = models.CharField(max_length=200)
    profimg = models.ImageField(upload_to='images', blank=True)

    """friends = models.ForeignKey("auth.User")

    statuses = models.ForeignKey(Status)

    request.user.friends.user_profile.statuses.all()"""

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])



class Status(models.Model):

    author = models.ForeignKey('auth.User')
    content = models.CharField(max_length=2000, blank=True, null=True)
    created_date = models.DateTimeField( default=timezone.now)
    published_date = models.DateTimeField( blank=True, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Friendship(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, related_name="friendship_creator_set")
    friend = models.ForeignKey(User, related_name="friend_set")

class Poke(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    initiator = models.ForeignKey(User, related_name="poke_initiator_set")
    receiver = models.ForeignKey(User, related_name="poke_receiver_set")


