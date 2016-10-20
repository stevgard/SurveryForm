from django.shortcuts import render, redirect

def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0;
    else:
        request.session['count'] += 1
    return render(request, 'form/index.html')

def results(request):
    if request.method == 'POST':
        print request.method
        request.session['name'] = request.POST['name']
        request.session['dojo'] = request.POST['dojo']
        request.session['fav_language'] = request.POST['fav_language']
        request.session['Comment'] = request.POST['Comment']
        return render(request, 'form/result.html')

def reset(request):
    request.session['count'] = 1
    return render(request, 'form/index.html')
    
