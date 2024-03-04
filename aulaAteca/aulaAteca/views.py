from django.http import HttpResponse
from django.template import Template, Context

def index(request):
    template = open("aulaAteca/template/templateIndex.html")
    plantilla = Template(template.read())
    template.close()
    context=Context(
        {
            "titulo": "Aula Ateca",
        }
    )
    
    return HttpResponse(plantilla.render(context))