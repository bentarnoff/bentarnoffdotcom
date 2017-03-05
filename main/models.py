from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
import views

class BlogPost(models.Model):
	pub_date = models.DateTimeField()
	title = models.CharField(max_length=200)
	description = models.TextField(default=None, blank=True, null=True, max_length=500)
	post = models.TextField()
	caption = models.TextField(default=None, blank=True, null=True, max_length=500)
	image_url = models.CharField(max_length=200, default=None, blank=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		slug = slugify(self.title)
		return reverse('main.views.blog', args=(), kwargs={"slug": slug, 'id': self.id,})

class Article(models.Model):
	pub_date = models.DateField()
	title = models.CharField(max_length=200)
	where = models.CharField(max_length=200)
	link = 	models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Interview_video(models.Model):
	pub_date = models.DateField()
	title = models.CharField(max_length=200)
	where = models.CharField(max_length=200)
	link = 	models.CharField(max_length=200)
	img_url = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Interview_audio(models.Model):
	pub_date = models.DateField()
	title = models.CharField(max_length=200)
	where = models.CharField(max_length=200)
	link = 	models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Interview_text(models.Model):
	pub_date = models.DateField()
	title = models.CharField(max_length=200)
	where = models.CharField(max_length=200)
	link = 	models.CharField(max_length=200)

	def __str__(self):
		return self.title



 