from django.shortcuts import render, redirect
from .forms import userForm
from .models import user
from .models import question, response, anwser


s = 0

def index(request):
	val = request.POST.get('v')
	if request.method == "POST":
		form = userForm(request.POST)
		User = user()
		if form.is_valid():
			currentname = form.cleaned_data['username']
			User.name = currentname
			User.save()
			return redirect('meandhim:quiz',  name=User.name, val=val, id = 0)
	else:
		form = userForm()
	return render(request,'meandhim/index.html',
                      {'form' : form})


def result(request, name):
	userval = user.objects.filter(name=name)[:1].get()
	rep = response.objects.filter(user=userval).all()
	return render(request, 'meandhim/result.html', {'rep' : rep})

def share(request, name):
	return render(request, 'meandhim/share.html')


def quiz(request, name, val, id):
	global s
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
		else:
			Answer = anwser()

			userval = user.objects.filter(name=name)[:1].get()
			rep = response.objects.filter(user=userval)[:1].get()
			questval = quests
			choiceval = request.GET.get('answer','')
			Answer.user = userval
			Answer.question = questval
			Answer.choice = choiceval
			if rep.choice == choiceval:
				s = s + 1
			Answer.score = s 
			Answer.save()

	elif val == 'r':
		return redirect('meandhim:result' , name=name)
	else:
		return redirect('meandhim:share' , name=name)
	return render(request, 'meandhim/quiz.html', {'quests' : quests, 'name' : name , 'val' : val})

