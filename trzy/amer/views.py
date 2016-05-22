from django.shortcuts import render
from amer.forms import ContactForm, menuForm
import datetime
from django.http import HttpResponseRedirect



def page_title_changer(request):
    return render(request,'child.html')

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
