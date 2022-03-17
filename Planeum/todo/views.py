from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
import json
from django.contrib import messages


def home(request):
    
    context = {
        "page":"home",
        "Todos":Todo.objects.all()
    }
    return render(request,"todo/home.html",context)

def manageTodo(request):
    get= request.GET
    id = int(0)
    todo = {}
    if 'id' in get:
        id= get['id']
        get_todo = Todo.objects.get(id=id)
        todo = {"title":get_todo.title,"description":get_todo.description}
    context = {
        "page":"manage",
        "id":id,
        "todo":todo
    }
    return render(request,"todo/manage_form.html",context)

def save_todo(request):
    posts = request.POST
    save_resp ={}
    id = posts['id'] if posts['id'].isnumeric() else int(0)
    
    if int(id) > int(0):
        todo = Todo.objects.get(pk=id)
        todo.title= posts['title']
        todo.description= posts['description']
        msg = "Todo ID["+str(id)+"] successfully updated."
    else:
        todo = Todo(title=posts['title'],description=posts['description'])
    # todo = {"id":id,"title":posts['title'],"description":posts['description']}
        msg = "New Todo Successfully created."
    try:
        todo.save()
    except Exception as ex:
        save_resp['status'] = 'failed'
        save_resp['exeption'] = ex
    finally:
        save_resp['status'] = 'success'
        messages.info(request, msg)


    response = {
        "post":posts,
        "save_resp":save_resp
    }
    if save_resp["status"] == 'success':
        return redirect("app-home")
    else:
        return HttpResponse(json.dumps(response), content_type="application/json")
def delete_todo(request):
    posts = request.GET
    if 'id' in posts:
        id = posts['id']
        try:
            print(id)
            todo = Todo.objects.get(id=id)
            print(todo)
            name = todo.title
            todo.delete()
        except Exception as ex:
            messages.error(request, "An error occured while deleting the data")
        finally:
            messages.info(request, "Data '{"+name+"}' successfully deleted")
    else:
        messages.warning(request, "No ID provided")
    return redirect("app-home")

def todo_change_state(request):
    posts = request.POST
    resp={}
    if 'id' in posts:
        status = 1 if posts['checked'] == 'true' else 0
        id = posts['id']
        resp['new_status']=status
        try:
            todo = Todo.objects.get(id=id)
            todo.status = status
            todo.save()
        except Exception as ex:
            print(ex)
            resp['status']="failed"
            resp['error'] = ex
        finally:
            resp['status']="success"
    else:
        resp['status']="failed"
        resp['error'] = "No id provided"
        print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")

