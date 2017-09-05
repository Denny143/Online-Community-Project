from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import Place,StudioUser,Teacher
from django.contrib.auth import login, authenticate
from datetime import date, timedelta
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.dates import WeekArchiveView,DayArchiveView

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


    booking_list = Teacher.objects.filter(teach_from__year=year, teach_from__month=month)
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
        cal_day['booking'] = False

        for booking in booking_list:
            if day >= booking.teach_from.date() and day <= booking.teach_to.date():           ###check this condition for studio_calendar objects
                cal_day['booking'] = True

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

    context = {'calendar': month_cal, 'headers': week_headers, 'currentyear':year, 'currentmonth':month}
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



class TeacherCreate(PermissionRequiredMixin,CreateView):

    permission_required = 'calender.add_teacher'
    raise_exception=True
    model = Teacher
    fields = ['place', 'teacher', 'teach_from', 'teach_to',]
    success_url = '/'

class StudioUserCreate(PermissionRequiredMixin,CreateView):

    permission_required = 'calender.add_studiouser'
    raise_exception=True
    model = StudioUser
    fields = ['place', 'studio_user', 'booked_from', 'booked_to',]
    success_url = '/'

class StudioDayView(DayArchiveView):
    queryset = Teacher.objects.all()
    date_field = "teach_from"
    allow_future = True





#    def get_initial(self):
#        # call super if needed
#        queryset=studio_calendar.objects.get(id=2)
#
#        return {'Owner_name':queryset.Owner_name,
#              'Studio_name':queryset.Studio_name,
#              'Teacher_name':queryset.Teacher_name,
#              'Operate_From':queryset.Operate_From,
#              'Operate_To':queryset.Operate_To,
#              'Hourly_rate':queryset.Hourly_rate,
#                }
#
#    def form_valid(self, form):
#        # This method is called when valid form data has been POSTed.
#        # It should return an HttpResponse.
#
#
#            Owner_name = form.cleaned_data.get('Owner_name')
#            Studio_name = form.cleaned_data.get('Studio_name')
#            Teacher_name = form.cleaned_data.get('Teacher_name')
#            Operate_From = form.cleaned_data.get('Operate_From')
#            Operate_To = form.cleaned_data.get('Operate_To')
#            Hourly_rate = form.cleaned_data.get('Hourly_rate')
#
#            form.save()
#            return super(studioform,self).form_valid(form)
#
#
#
##def studioform(request):
#
#    #queryset=studio_calendar.objects.get(id=1)

    #data={'Owner_name':queryset.Owner_name,
    #      'Studio_name':queryset.Studio_name,
    #      'Operate_From':queryset.Operate_From,
    #      'Operate_To':queryset.Operate_To,
    #      'Hourly_rate':queryset.Hourly_rate,
    #        }

    #form = StudioForm(initial=data, auto_id=False)
#    instance=get_object_or_404(studio_calendar, id=1)
#
#    form = StudioForm(instance=instance)
#
#    if request.method == 'POST':
#        form = StudioForm(request.POST)
#
#        if form.is_valid():
#
#            Owner_name = form.cleaned_data.get('Owner_name')
#            Studio_name = form.cleaned_data.get('Studio_name')
#            Operate_From = form.cleaned_data.get('Operate_From')
#            Operate_To = form.cleaned_data.get('Operate_To')
#            Hourly_rate = form.cleaned_data.get('Hourly_rate')
#            form.save()
#
#            return redirect('/studios')
#    else:
#        form = StudioForm()
#    return render(request, 'studioform.html', {'form': form})
#
