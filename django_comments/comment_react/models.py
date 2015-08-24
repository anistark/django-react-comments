from django.db import models

class Comments(models.Model):
	user_id = models.CharField(max_length=250)
	post_id = models.CharField(max_length=250)
	comment = models.CharField(max_length=500)
	
	def __str__(self):
		return "user_id="+self.user_id+","+"comment="+self.comment+","+"post_id="+self.post_id

	def save(self, *args, **kwargs):
		super(Comments, self).save(*args, **kwargs)
