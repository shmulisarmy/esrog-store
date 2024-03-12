from django.shortcuts import render
from django.templatetags.static import static

# Create your views here.
def main(request):
    return render(request, 'main.html', {'stylesheet': static('main.css')})
