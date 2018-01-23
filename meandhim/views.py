from django.shortcuts import render, redirect
from .forms import userForm
#from .models import user
# Create your views here.


def quiz(request):
	username = request.GET.get('username')
	v = request.GET.get('v')
	print(v)
	print(username)
	return render(request, 'meandhim/quiz.html')





# Create your views here.
def index(request):
        
	if request.method == "POST":
                        #v = request.GET.get('v')
                        #print(v)
			form = userForm(request.POST)
			#Task = task()
			"""
			#if form.is_valid():
				Task.myTask = form.cleaned_data['myTask']
				Task.save()
				return redirect('meandhim:index')
				"""
	else:
		form = userForm()
	return render(request,'meandhim/index.html',
                      {'form' : form})
