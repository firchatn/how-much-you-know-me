from django.shortcuts import render, redirect
from .forms import userForm
from .models import user
# Create your views here.



def index(request):
	val = request.POST.get('v')
	if request.method == "POST":
		form = userForm(request.POST)
		User = user()
		if form.is_valid():
			User.name = form.cleaned_data['username']
			User.save()
			return redirect('meandhim:quiz',  id=User.name)
	else:
		form = userForm()
	return render(request,'meandhim/index.html',
                      {'form' : form})


def quiz(request, id):
	return render(request, 'meandhim/quiz.html')

