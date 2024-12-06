from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.authtoken.views import obatin_auth_token
@sensitive_post_parameters()
@csrf_protect()
@never_cache()

def login(request):
    if request.method == 'Post':
        username = request.POST['user']
        password = request.POST['pass']
        dados ={
            "username": "{0}".format(username),
            "password": "{0}".format(password)
            }
        response = request.post("http://127.0.0.1:8000/auth/", data=dados)
        if response.status_code != 400:
            autorizacao = json.loads(response.content)
            request.session['tk'] = autorizacao['token']
        else:
            return render(request, 'login.html', {'code': 400})
    else:
        return render(request, 'login.html')


@csrf_protect
@never_cache
def logout(request): 
    if 'tk' in request.session:
        del request.session['tk']
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')