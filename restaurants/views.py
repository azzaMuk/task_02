from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
	"msg": "hello, World!"
	}
	return render(request, 'hello.html',context)
