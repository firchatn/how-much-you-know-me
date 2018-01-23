from django.shortcuts import render, redirect
from .forms import userForm
from .models import user
from .models import question, response, anwser




def index(request):
	val = request.POST.get('v')
	if request.method == "POST":
		form = userForm(request.POST)
		User = user()
		if form.is_valid():
			User.name = form.cleaned_data['username']
			User.save()
			return redirect('meandhim:quiz',  name=User.name, val=val, id= 0)
	else:
		form = userForm()
	return render(request,'meandhim/index.html',
                      {'form' : form})


def quiz(request, name, val, id=None):
	"""
	if val == 'q':
		Response = response()
	else:
		Anwser = anwser()
	"""
	return render(request, 'meandhim/quiz.html')

