from django.shortcuts import render

from .models import Userinfo
# Create your views here.



def index(request):
	user = Userinfo.objects.all()

	return render(request, 'home/index.html', { 'user': user})
