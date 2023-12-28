from django.template import loader
from django.http import HttpResponse

def members(request):
    template = loader.get_template('teste.html')
    return HttpResponse(template.render())

# Create your views here.
