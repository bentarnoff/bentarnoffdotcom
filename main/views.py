from django.shortcuts import render, render_to_response, HttpResponse
from django.core.mail import send_mail
from django.template.context_processors import csrf
from django.template import RequestContext
import models

def home(request):
	posts = models.BlogPost.objects.order_by('-pub_date')
	return render_to_response("base.html", {'posts': posts})

def blog(request, id, slug):
	posts = models.BlogPost.objects.filter(id=id)
	return render_to_response("single.html", {'post': posts[0]})

def books(request):
	return render_to_response("books.html")

def articles(request):
	return render_to_response("articles.html")
	
def interviews(request):
	interviews_video = models.Interview_video.objects.order_by('-pub_date')
	interviews_audio = models.Interview_audio.objects.order_by('-pub_date')
	interviews_text = models.Interview_text.objects.order_by('-pub_date')
	return render_to_response("interviews.html", {'interviews_video': interviews_video, 'interviews_audio': interviews_audio, 'interviews_text': interviews_text})

def projects(request):
	return render_to_response("projects.html")