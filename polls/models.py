import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	"""docstring for Question"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('data published')


	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
	"""docstring for Choice"""
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.choice_text