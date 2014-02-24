from django.shortcuts import render

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from ribbit_app.forms import AuthenticateForm, UserCreateForm, RibbitForm

# Create your views here.

def index(request,auth_form=None,user_form=None):
	#if logged in 
	if request.user.is_authenticated():
		ribbit_form = RibbitForm()
		user = request.user
		ribbit_self = Ribbit.objects.filter(user=user.id)
		ribbits_budddies = Ribbit.objects.filter(user__userprofile__in=user.profile.all)
		ribbits = ribbits_self | ribbits_budddies

		return render(request, 
					  'buddies.html',
					  {'ribbit_form':ribbit_form,'user':user,
					   'ribbits':ribbits,
					   'next_url':'/',})

	else:
		#User is not logged in
		auth_form = auth_form or AuthenticateForm()
		user_form = user_form or UserCreateForm()

		return render(request,'home.html',
					   {'auth_form':auth_form,'user_form':user_form, })


def login_view(request):
	if request.method == 'POST':
		form = AuthenticateForm(data=request.POST)
		if form.is_valid():
			login(request,form.get_user())
			#Success
			return redirect('/')
		else:
			#failure
			return index(request,auth_form=form)
	return redirect('/')


def logout_view(request):
	logout(request)
	return redirect('/')