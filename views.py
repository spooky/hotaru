from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def show(request, template):
    return render_to_response(template+'.html')