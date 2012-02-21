from models import *
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson


def view_list(request, user_name, list_name):
#    import pdb; pdb.set_trace()
    user = User.objects.filter(username=user_name)
    if len(user) == 0:
        user = User.objects.create_user(user_name, 'test@test.com', 'xyzzy')
        user.save()
    else:
        user = user[0]
    existing_list = user.list_set.filter(name=list_name)
    if len(existing_list) == 1:
        list = existing_list[0]
    else:
        list = List(name=list_name)
        list.user = user
        list.save()

    return render_to_response("list.html", {
            "list": list
        }, context_instance=RequestContext(request))


def add_item(request, user_name, list_name, new_item):
    list = User.objects.get(username=user_name).list_set.get(name=list_name)
    item = Item(name=new_item)
    item.list = list
    item.save()
    result = {"name": item.name, "pk": item.pk}
    return HttpResponse(simplejson.dumps(result))


def remove_item(request, user_name, list_name, pk):
    item = Item.objects.get(pk=pk)
    item.delete()


def clear_list(request, user_name, list_name):
    list = User.objects.get(username=user_name).list_set.get(name=list_name)
    list.item_set.all().delete()


def user_lists(request, user_name):
    user = request.user
    if not user.is_authenticated():
        user = User.objects.filter(username=user_name)
        if len(user) == 1:
            user = user[0]
        else:
            user = None
    #user = get_or_create_user(user_name)
    return render_to_response("user.html", {
            "user": user
        }, context_instance=RequestContext(request))


def home(request):
    return render_to_response("index.html",
        None,
        context_instance=RequestContext(request)
    )
