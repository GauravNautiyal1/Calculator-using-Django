from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):

 return render(request,"index.html")

def calculate(request):
    if request.method == "POST":
        expression = request.POST.get('expression')
        try:
            result = eval(expression)
        except Exception as e:
            result = "Error"
        return JsonResponse({'result': result})
