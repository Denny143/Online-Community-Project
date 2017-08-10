from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import studio_calendar
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from calender.forms import SignUpForm
import calendar



# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')


def schedules(request):
    months=[]
    for i in range(1,13):
        months.append(calendar.month_name[i])
    #months=["July", "Aug", "September", "December"]
    studios=["La-peurta-Negra", "Studio-pleamar", "Delphine-Mantha-Studio"]
    context={"month_var":months,
            "studio_var":studios
            }
    return render(request,"schedules.html",context)

def events(request):
    events=["event1","event2","event3","event4"]
    studios=["La-peurta-Negra", "Studio-pleamar", "Delphine-Mantha-Studio"]
    context={"event_list":events,
            "studio_var":studios
            }
    return render(request,"events.html",context)

def venues(request):
    venue_list=["venue-1", "venue-2", "venue-3", "venue-4"]
    studios=["La-peurta-Negra", "Studio-pleamar", "Delphine-Mantha-Studio"]
    context={"venue_list":venue_list,
            "studio_var":studios
            }
    return render(request,"venues.html",context)

def reservations(request):
    template_name='calender/reservations.html'
    queryset=studio_calendar.objects.all()

    context={
       "obj_list":queryset
    }
    return render(request,template_name, context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
