from django.shortcuts import render, render_to_response

# # Create your views here.
# def index(request):
# 	print 'Hello'
# 	return render_to_response('index.html')

from django.http import HttpResponse

def index(request):
	return render_to_response('index.html')

