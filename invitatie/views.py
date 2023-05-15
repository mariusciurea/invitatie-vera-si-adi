from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Confirm

def home(request):
    context = {}
    CONFIRMARE = {'afirmativ': 'Abia astept', 'negativ': 'Nu pot veni'}
    if request.method == 'POST':
        name = request.POST.get('nume')
        persons = request.POST.get('numar')
        confirm = request.POST.get('confirmare')
        print(CONFIRMARE[confirm])
        Confirm(
            name=name,
            people=persons,
            confirm=CONFIRMARE[confirm]
        ).save()
        # messages.info(request, 'Iti multumim pentru raspuns!')
        return redirect('home')

    return render(request, 'invitatie/invitatie.html', context)


@login_required(login_url='home')
def confirmation(request):
    all_people = Confirm.objects.all()
    context = {'all_people': all_people}
    return render(request, 'invitatie/confirmation.html', context)