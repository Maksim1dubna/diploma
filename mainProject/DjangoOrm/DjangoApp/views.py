from django.http import HttpResponse
from django.template import loader
from DjangoApp.models import Task
from django.shortcuts import render, redirect
# Create your views here.
from django import forms

class AddNewUpdate(forms.Form):
    id_cu = forms.IntegerField(label="Введите ID", required=True)
    name = forms.CharField(max_length=30, required=False, label="Введите название")
    description = forms.CharField(max_length=30, required=False, label="Введите описание")
class DeleteByid(forms.Form):
    id_d = forms.IntegerField(label="Введите ID на удаление", required=True)
def main_temp(request):
    error = ''
    tasks = Task.objects.all()
    print(tasks)
    print(type(tasks))
    template = loader.get_template('main.html')
    context = {
        'firstname': 'Linus',
        'tasks': tasks,
        'error': error
    }
    #------------------
    #new post
    tasks = Task.objects.values_list("id", flat=1)
    print(list(tasks))
    form_cu = AddNewUpdate(request.POST)
    if request.method == "POST" and form_cu.is_valid():
        print("\n\n\nFORM IS VALID\n\n\n")
        id = form_cu.cleaned_data['id_cu']
        name = form_cu.cleaned_data['name']
        description = form_cu.cleaned_data['description']
        if id in list(tasks):
            Task.objects.filter(id=id).update(name=name, description=description)
            error = f"Задание {id} ОБНОВЛЕНО"
            context['error'] = error
            return HttpResponse(template.render(context, request))
        Task.objects.create(id=id, name=name, description=description)
        print(f"\n\n\nADD\n\n\n-------------{id, name, description}---------")
        error = f"Задание {id} ДОБАВЛЕНО"
        context['error'] = error
        return HttpResponse(template.render(context, request))
    # ------------------
    # new post
    form_d = DeleteByid(request.POST)
    if request.method == "POST" and form_d.is_valid():
        id = form_d.cleaned_data['id_d']
        if id in list(tasks):
            Task.objects.filter(id=id).delete()
            error = f"Задание {id} УДАЛЕНО"
            context['error'] = error
        else:
            error = f"Задание {id} НЕ СУЩЕСТВУЕТ"
            context['error'] = error
            return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))