from django.db import models

class Newsletter(models.Model):
	create_date = models.DateTimeField(editable=False, auto_now_add=True)
	title = models.CharField(max_length=100)
	update_date = models.DateTimeField(editable=False, auto_now=True)
	path = models.CharField(max_length=100)
	visible = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ("newsletter",[self.path])

	@property
	def is_visible(self):
		return self.visible

		

class Article(models.Model):
	create_date = models.DateTimeField(editable=False, auto_now_add=True)
	text = models.TextField()
	title = models.CharField(max_length=100)
	update_date = models.DateTimeField(editable=False, auto_now=True)
	path = models.CharField(max_length=100)
	publish_date = models.DateTimeField()
	visible = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ("newsletter", [self.path])

	@property
	def is_visible(self):
		return self.visible


