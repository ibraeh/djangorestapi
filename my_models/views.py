from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import ListView
from my_models.models import Publisher,User_Profile
from .forms import Profile_Form


def index(request):
	return render(request,'my_models/index.html')


def display(request):
	x=[]
	for i in range(10):
		x.append(i)
	return HttpResponse ("<h1> Dataflair Django Tutorial</h1> Numbers:{} ".format(x))


class PublisherListView(ListView):
	model=Publisher

#setting a session with the set_test_cookie method
def cookie_session(request):
	request.session.set_test_cookie()
	return HttpResponse("<h1> Dataflair <br>---setting Sessions</h1>")

#deleting a session using test_cookie_worked () and delete_test_cookie method
def cookie_delete(request):
	if request.session.test_cookie_worked(): #checking for presence of a session
		request.session.delete_test_cookie() #deleting the session
		response=HttpResponse("<h1>Dataflair <br> cookie deleted</h1>")
	else:
		response=HttpResponse("<h1>Dataflair <br> Your browser doesnot accept cookies / no cookies present</h1>")
	return response


#definig key-value pairs for creating, accessing and deleting sessions
def create_session(request):
	request.session['name']='username'
	request.session['password']='password@123'
	response=HttpResponse("<h1> Dataflair <br> the session is set</h1>")
	return response

def access_session(request):
	response="<h1>Welcome to Sessions of dataflair<h1> <br>"
	if request.session.get('name'):
		response+="Name: {0} <br>".format(request.session.get('name'))
		if request.session.get('password'):
			response+="Password: {0} <br>".format(request.session.get('password'))
		return HttpResponse(response)

	else:
		return redirect(reverse('create'))	

def delete_session(request):
	try:
		del request.session['name']
		del request.session['password']
	except KeyError:
		pass
	return HttpResponse("<h1>dataflair <br> Session Data cleared</h1>")

#profile maker views
IMAGE_FILE_TYPES=['png','jpg','jpeg']

def create_profile(request):
	form=Profile_Form()
	if request.method=='POST':
		form=Profile_Form(request.POST,request.FILES)
		if form.is_valid():
			user_pr=form.save(commit=False)
			user_pr.display_picture=request.FILES['display_picture']
			file_type=user_pr.display_picture.url.split('.')[-1]
			file_type.lower()
			if file_type not in IMAGE_FILE_TYPES:
				return render(request,'my_models/error.html')
			user_pr.save()
			return render(request, 'my_models/details.html', {'user_pr':user_pr})
	else:
		context={'form':form}
		return render(request, 'my_models/create.html', context)