import json
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from models import Memory

def add(request):
    if request.method == 'POST':
        to = 'Hey ' + request.POST['to'].strip() + ','
        body = 'Remember that time ' + request.POST['body'].strip()

        mem = Memory.objects.create(author=request.user, body=body, to=to)
        mem.save()

        response_data = {}
        response_data['header'] = 'Memory stored!'
        response_data['message'] = {
            'to': mem.to,
            'body': mem.body,
            'from': mem.author.username,
            'date': int(mem.date.strftime('%s'))
        }
        return HttpResponse(json.dumps(response_data), content_type='application/json')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            # Invalid login
            return HttpResponse('Invalid login')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def index(request):
    if request.user.is_authenticated():
        return render(request, 'form.html',
            { "username": request.user.username })
    else:
        return render(request, 'index.html')

