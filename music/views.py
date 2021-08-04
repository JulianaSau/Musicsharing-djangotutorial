# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader # imports templates usefulin separating html code fro django backend

def index(request):
	all_albums=Album.objects.all() #imports all albums from the database
	# html = ''
	# for album in all_albums:
	# 	url = '/music/' + str(album.id) + '/'
	# 	html += '<a href="' + url + '">' + album.album_title + '</a><br>'
	template = loader.get_template('music/index.html')
	context = {
		'all_albums': all_albums,
	}

	return HttpResponse(template.render(context, request))


def detail(request, album_id):
	return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2> ")	