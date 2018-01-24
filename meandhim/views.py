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
			return redirect('meandhim:quiz',  name=User.name, val=val, id = 0)
	else:
		form = userForm()
	return render(request,'meandhim/index.html',
                      {'form' : form})


def result(request, name):
	return render(request, 'meandhim/result.html')

def share(request, name):
	return render(request, 'meandhim/share.html')


def quiz(request, name, val, id):
	x = int(id)
	x = x + 1 
	id = str(x)
	try:
		quests = question.objects.filter(id=id)[:1].get()
	except Exception:
		pass

	if x<=2:
		if val == 'r':
			Response = response()
			userval = user.objects.filter(name=name)[:1].get()
			quesval = quests
			choiceval = request.GET.get('answer','')
			Response.user = userval
			Response.question = quesval
			Response.choice = choiceval
			Response.save()
	elif val == 'r':
		return redirect('meandhim:result' , name=name)
	else:
		return redirect('meandhim:share' , name=name)
	return render(request, 'meandhim/quiz.html', {'quests' : quests, 'name' : name , 'val' : val})

