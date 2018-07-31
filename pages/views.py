from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from . models import Page

def index(request, pagename):
	#return HttpResponse("<h1>The Meandco Homepage</h1>")
	pagename = '/' + pagename
	#pg = Page.objects.get(permalink=pagename)
	pg = get_object_or_404(Page, permalink=pagename)
	context = {
		'title': pg.title,
		'content': pg.bodytext,
		'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
	}
	#assert False
	return render(request, 'pages/page.html', context)