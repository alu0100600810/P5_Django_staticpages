from django.http import HttpResponse

def home(request):
	return HttpResponse("Buenos dias, estas en la pagina home")

def help(request):
        return HttpResponse("Buenos dias, estas en la pagina help")
def about(request):
        return HttpResponse("Buenos dias, estas en la pagina about")






# Create your views here.
