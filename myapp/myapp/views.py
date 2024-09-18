from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def N01(request):
	return render(request, '01.html')

def N02(request):
	return render(request, '02.html')
def N03(request):
	return render(request, '03.html')

def manager(request):
	return render(request, 'manager.html')