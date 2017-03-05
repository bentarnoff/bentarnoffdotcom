from django.contrib.syndication.views import Feed
from models import BlogPost

class RSSFeed(Feed):
	title = "Ben Tarnoff's blog"
	link = "/"
	description_template = "templates/single.html"

	def items(self):
		return BlogPost.objects.order_by("-pub_date")[:5]

	def item_title(self, item):
		return item.title

	def item_pubdate(self, item):
		return item.pub_date

	def item_description(self, item):
		return item.post