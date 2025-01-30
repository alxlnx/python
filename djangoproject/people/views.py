from django.shortcuts import render
# Create your views here.
from .models import Person
from django.http import JsonResponse


def all(request):
    people = list(Person.objects.all().values())
   
    #return JsonResponse({'items': people})
    return render(request, template_name='all.html',
                  context={'people': people})

@csrf_exempt
def add(request):
    if request.method == 'POST':
        person = json.loads(request.body.decode())
        p = Person(name=person['name'],
                   age = person['age'],
                   group = person['group'])
        person = request.POST.get('person')