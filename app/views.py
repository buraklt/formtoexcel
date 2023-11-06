from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
import csv

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {})

def display_form(request, form_id):
    if request.method == 'POST':
        post = request.POST

        responses = ""
        for i in range(0, 34):
            if i != 0:
                responses = responses + "&\n"

            if f'answ{i}' in post:
                responses = responses + "1"
            else:
                responses = responses + "0"
        
        new_respond = models.Responds.objects.create(name = post.get('ad'), surname = post.get('soyad'), num = post.get('okulno'), form = models.CustomForm.objects.get(id = 1),
                    responses = responses)
        new_respond.save()

        return redirect('/ad')
    return render(request, 'form.html', {'model': models.CustomForm.objects.get(id = form_id)} )

def export_to_excel(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if code != "riskanalizraporu" or not code:
            return redirect('.')
    else:
        return redirect('.')
        
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=responds.csv'

    writer = csv.writer(response)

    writer.writerow( ( ["Ad", "Soyad", "Okul No"] + models.CustomForm.objects.get(id = 1).questions.split('&') ) )
    for respond in models.Responds.objects.all():
        writer.writerow( ( [respond.name, respond.surname, respond.num] + respond.responses.split('&') ) )    

    return response