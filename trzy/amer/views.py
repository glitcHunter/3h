from django.shortcuts import render, get_object_or_404, render_to_response
from amer.forms import ContactForm, menuForm
from amer.models import Character
import datetime
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.core.context_processors import csrf




from django.http import HttpResponse
from django.views.generic import View



def login_view(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password= password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/amer/loggedin')
    else:
        return HttpResponseRedirect('/amer/invalid')

def loggedin(request):
    return render(request,'loggedin.html',
                              {'full_name':request.user.username}) 

def invalid(request):
    return render(request,'invalid.html')
    
def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

class GreetingView(View):
    greeting = ""

    def get(self, request):
        return HttpResponse(self.greeting)

def about(request,template_name):
    return render(request, template_name)

def custom_proc(request):

    return {
        'app':'Hi, here',
        'message':'i am a smile in your mirror ',
        }


def request_view(request, template_name):
    return render(request, template_name, context_instance=RequestContext(request, processors=[custom_proc]))

def page_title_changer(request,id):
    ''' I have regular group expression in url a/(?P<id>\d+)/$. I'll implement get_object_or_404 to catch others urls than id(model)!=id(from url)'''
    '''If model id don't exists - request method get exception -404'''
    instance = get_object_or_404(Character, id=id)
    context = {'instance':instance}
    return render(request,'child.html',context)


# Create your views here.
def home_page(request, model):
    now = datetime.datetime.now()
    obj_list= model.objects.all()
    
    return  render(request,'base.html',{'obj_list':obj_list})


def forms_need(request,template_name):
    return render(request,template_name)

def contact(request):
    #if this is a POST request we need to process the form data
    if request.method== 'Post':
        ## create a form instance and populate it with data from the request:
        form =ContactForm(request.Post)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'})
        
    return render(request,'contact.html', {'form':form})

def menu_form(request):
    #if this is a POST request we need to process the form data
    if request.method == 'Post':
        ## create a form instance and populate it with data from the request:
        form =menuForm(request.Post)
        # check whether it's valid:
        if form.is_valid():
            cd = form.save(commit=False)
            print (form.cleaned_data.get("your_name"))
            cd.save()
            return HttpResponseRedirect('/menu_form/your_name/')
    else:
        form = menuForm()

        
    return  render(request,'menu_form.html', {'form':form})
