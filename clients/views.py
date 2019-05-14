from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from clients.models import Profile, RecentlyViewed
from clients.forms.profile_form import ProfileForm, RecentlyViewedForm
from properties.models import Properties
from datetime import datetime


# Create your views here.
def index(request):
	return render(request, 'clients/index.html')


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('clients-login')
	return render(request, 'clients/register.html', {
		'form': UserCreationForm()
	})


def profile(request):
	profile = Profile.objects.filter(user=request.user).first()
	if request.method == 'POST':
		form = ProfileForm(instance=profile, data=request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('clients-profile')
	return render(request, 'clients/profile.html', {
		'form': ProfileForm(instance=profile)
	})


def get_recently_viewed(request):
	the_user = request.user
	return RecentlyViewed.objects.filter(user=the_user).order_by(datetime)


def add_to_recently_viewed(request, the_id):
	# ToDo Finish!!!!
	if request.user.is_authenticated:
		the_user = Profile.objects.filter(user=request.user).first()
		prop = get_object_or_404(Properties, pk=the_id)
		this_user_recent_list = RecentlyViewed.objects.filter(user=the_user)
		print(len(this_user_recent_list))
		entry = this_user_recent_list.filter(property=prop)
		if len(entry) != 0:
			print("the entry ", entry)
		elif len(this_user_recent_list) >= 10:
			oldest = this_user_recent_list[0]
			RecentlyViewed.objects.filter(id=oldest.id).delete()
		form = RecentlyViewedForm(data=request.POST)
		recently_viewed = form.save(commit=False)
		recently_viewed.user = the_user
		recently_viewed.property = prop
		if form.is_valid():
			recently_viewed.save()
			print(recently_viewed)

			"""if len(this_user_recent_list) == 10:
				oldest = this_user_recent_list[0]
				RecentlyViewed.objects.filter(id=oldest.id).delete()"""