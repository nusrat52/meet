from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Meetups, Participants
from .forms import RegistrationForm

# Create your views here.


def index(response):

 
    mettups =Meetups.objects.all()

 
    return render(response, "meetups/index.html", {"meetups": mettups, "show": True})



def succes_view(request, slug_success):
    meetup=Meetups.objects.get(slug=slug_success)
    email=meetup.organizer_email
    return render(request, "meetups/success.html", {"email": email})



def detail_meetup(request, slugg):
    form = RegistrationForm()

      
    try:
        meetup=Meetups.objects.get(slug=slugg)
        if request.method=='GET':
            ttmt='ttmt'
            
        else:
            requsetForm=RegistrationForm(request.POST)
            if requsetForm.is_valid():
                
               d=requsetForm.cleaned_data.get('email')
               print(d, 'user_email')
               participiant, _= Participants.objects.get_or_create(email=d)
               meetup.participants.add(participiant)
               return redirect('successPageName', slug_success=slugg)

        return render(request, "meetups/meetup-detail.html", {"form":form, "title":meetup.title, "description":meetup.description, "image":meetup.image.url, "paticipants":meetup.participants,"organizer":meetup.organizer_email, "date":meetup.date, 'location':meetup.location.name, "address":meetup.location.adress, "slug": meetup.slug})
    except Exception as exc:
        print(exc ," print olan yer")
        return render(request, "meetups/meetup-detail.html", {"form":requsetForm,   "slug": meetup.slug})
        return render(request, "meetups/404.html")

    
        