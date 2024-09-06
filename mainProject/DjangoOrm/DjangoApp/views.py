from django.http import HttpResponse
from django.template import loader
from DjangoApp.models import Task
# Create your views here.
def main_temp(request):
    # new = Task(
    #     name="Задание",
    #     description="Неизвестно"
    # )
    # new.save()
    tasks = Task.objects.all()
    template = loader.get_template('main.html')
    context = {
        'firstname': 'Linus',
        'tasks': tasks,
    }
    return HttpResponse(template.render(context, request))