from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'meandhim/index.html')

def quiz(request):
	username = request.GET.get('username')
	v = request.GET.get('v')
	print(v)
	print(username)
	return render(request, 'meandhim/quiz.html')
