from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from comment_react.models import Comments
from django.http import HttpResponse
import json
from django.http import QueryDict

@csrf_exempt
def home(request):
	queryDict = QueryDict()
	context_instance=RequestContext(request)
	if request.method == 'GET':
		return render_to_response('index.html')
	elif request.method == 'POST':
		data = request.POST.urlencode()
		comment = data.split('&')[0].split('=')[1]
		author = data.split('&')[1].split('=')[1]
		queryDict = request.POST
		queryDict_to_string = str(queryDict)
		#extracting the author name and comment out of the querydict
		a = qu.split(':')
		b = a[2].split("'")
		#c = a[3].split("'")
		#author = c[1]
		handle = b[1]
		p1 = Comments(user_id=author,
			post_id = '1',
			comment = handle)
		p1.save()
		return render_to_response('index.html')

@csrf_exempt
def getComments(request):
	data = Comments.objects.all()
	comments = []
	for obj in data:
		commentCurr = {
		"author": obj.user_id,
		"text": obj.comment.replace('+',' '),
		"post_id": obj.post_id,
		}
		comments.append(commentCurr)
	comments.append({ 'status_code' : 'success' })
	return HttpResponse(json.dumps(comments), content_type = "application/json")


