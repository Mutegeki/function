from django.http import HttpResponse
from django.shortcuts import render
from .models import Mycar
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/accounts/login/")
def article_list(request):
	#return HttpResponse('homepage')
	return render(request, 'articles/article_list.html')
