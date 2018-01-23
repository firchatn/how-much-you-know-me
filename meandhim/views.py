from django.shortcuts import render, redirect
from .forms import userForm
from .models import user
# Create your views here.



def index(request):
	if request.method == "POST":
		print('ok1')
		form = userForm(request.POST)
		User = user()
		v = request.GET.get('v')
		if form.is_valid():
			print('ok2')
			User.name = form.cleaned_data['username']
			User.save()
			return redirect('meandhim:quiz')
	else:
		form = userForm()
	return render(request,'meandhim/index.html',
                      {'form' : form})


def quiz(request):
	username = request.GET.get('username')
	v = request.GET.get('v')
	print(v)
	print(username)
	return render(request, 'meandhim/quiz.html')

