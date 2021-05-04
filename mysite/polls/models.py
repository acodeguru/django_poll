"""
Poll model configurations
"""
import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model


class Question(models.Model):
    """
    Question model configurations
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    ip_address = models.GenericIPAddressField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.question_text)

    def was_published_recently(self):
        """
        return recently published polls
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def user_can_vote(self, user):
        """
        Return False if user already voted
        """
        user_votes = user.vote_set.all()
        qs = user_votes.filter(question=self)
        if qs.exists():
            return False
        return True

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class UserQuestion(models.Model):
    """
    Question User relationship model configurations
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Choice(models.Model):
    """
    Choice model configurations
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)


class Vote(models.Model):
    """
    Vote model configurations
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.question_text[:15]} - ' \
               f'{self.choice.choice_text[:15]} - {self.user}'
