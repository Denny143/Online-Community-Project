from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.views.generic import TemplateView
#from django.views.generic.list import ListView
from .models import studio_calendar,user_calendar
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from calender.forms import SignUpForm, StudioForm
from datetime import date, timedelta




# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')


def schedules(request):
    template_name='calender/schedules.html'
    queryset=user_calendar.objects.all()
    context={
           "obj_list":queryset
        }
    return render(request,template_name,context)


#class StudioView(ListView):
#    template_name="calender/studios.html"
#    model=studio_calendar
def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)

def studios(request):
    year=date.today().year
    month=date.today().month


    studio_list = studio_calendar.objects.filter(Operate_From__year=year, Operate_From__month=month)
    first_day_of_month = date(year, month, 1)
    last_day_of_month = get_last_day_of_month(year, month)
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())

    month_cal = []
    week = []
    week_headers = []

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['event'] = False
        for studio in studio_list:
            if day >= studio.Operate_From.date() and day <= studio.Operate_From.date(): ###check this condition for studio_calendar objects
                cal_day['event'] = True
        if day.month == month:
            cal_day['in_month'] = True
        else:
            cal_day['in_month'] = False
        week.append(cal_day)
        if day.weekday() == 6:
            month_cal.append(week)
            week = []
        i += 1
        day += timedelta(1)

    context = {'calendar': month_cal, 'headers': week_headers}
    template_name='calender/studios.html'
    return render(request,template_name,context)

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

def studioform(request):

    queryset=studio_calendar.objects.get(id=1)

    data={'Owner_name':queryset.Owner_name,
          'Studio_name':queryset.Studio_name,
          'Operate_From':queryset.Operate_From,
          'Operate_To':queryset.Operate_To,
          'Hourly_rate':queryset.Hourly_rate,
            }

    form = StudioForm(initial=data, auto_id=False)

    if request.method == 'POST':
        form = StudioForm(request.POST)
        if form.is_valid():

            Owner_name = form.cleaned_data.get('Owner_name')
            Studio_name = form.cleaned_data.get('Studio_name')
            Operate_From = form.cleaned_data.get('Operate_From')
            Operate_To = form.cleaned_data.get('Operate_To')
            Hourly_rate = form.cleaned_data.get('Hourly_rate')
            form.save()

            return redirect('/studios')
    else:
        form = StudioForm()
    return render(request, 'studioform.html', {'form': form})
