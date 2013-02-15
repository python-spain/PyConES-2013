from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from django.contrib.auth.models import User


def suscribe_newsletter(request):
    """
        View to suscribe new users to newsletter
    """
    if request.method == 'POST':
        email_user = request.POST['email_user']
        if email_user:
            #try:
                user = User.objects.create_user(email_user,email_user,email_user)
                user.last_name='newsletter'
                user.save()
                return HttpResponse('<html><h1>Todo ok</h1></html>')
            #except:
            #    raise Http404
        else:
            raise Http404
    else:
        raise Http404

def unsuscribe_newsletter(request):
    """
        View to unsuscribe newsletter
    """
    if request.method == 'GET':
        email_user = request.GET['email']
        token_user = request.GET['val_token']
        if email_user and token_user:
            try:
                user = get_object_or_404(User,username=email_user,
                                        email=email_user,
                                        password=token_user)
                if user:
                    user.delete()
                    return HttpResponse('<h1>Usuario borrado</h1>')
                else:
                    raise Http404
            except:
                raise Http404
        else:
            raise Http404
    else:
        raise Http404

