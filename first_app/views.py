from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, './first_app/home.html',{"name" : "I am rahim","marks":86, "courses":[
        {
            "id":1,
        "course":"c",
        "teacher":"rahim"
        },
        {
            "id":2,
        "course":"c++",
        "teacher":"karim"
        },
        {
            "id":3,
        "course":"python",
        "teacher":"fahim"
        },
    ]})
    
def about(request):
    return render(request, './first_app/about.html', {'author': 'Holam raim'})
    