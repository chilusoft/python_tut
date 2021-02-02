from django.db import models

# Create your models here.

class Userinfo(models.Model):

	username = models.CharField(max_length=255)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username
