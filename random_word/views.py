from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 

def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] +=1
        request.session['random_word'] = get_random_string(length=14, allowed_chars='abcdefghijklmnopqrstuvwxyz ') 

# Here's another way to write it! 
  
    """ if 'counter' in request.session: 
        request.session['counter'] += 1  
        request.session['random_word'] = get_random_string(length=14, allowed_chars='abcdefghijklmnopqrstuvwxyz ') 
    else: 
        request.session['counter'] = 1 """
    

    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return render(request, 'index.html')
