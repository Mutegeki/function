from django.shortcuts import render

# Create your views here.
def signup_view(request):
	#return HttpResponse('homepage')
	return render(request, 'accounts/signup.html')