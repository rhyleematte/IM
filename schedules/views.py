from django.shortcuts import render, redirect, get_object_or_404
from .models import Schedule
from .forms import ScheduleForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from .models import Schedule

def schedule_list(request):
    category_filter = request.GET.get('category', 'All')
    if category_filter == 'All':
        schedules = Schedule.objects.all().order_by('date', 'time')
    else:
        schedules = Schedule.objects.filter(group=category_filter)

    return render(request, 'schedule_list.html', {'schedules': schedules})


@csrf_protect

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Schedule added successfully!") 
            form = ScheduleForm()
    else:
        form = ScheduleForm()
    return render(request, 'add_schedule.html', {'form': form})

@csrf_protect
def edit_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'add_schedule.html', {'form': form})

@csrf_protect
def delete_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')
    return render(request, 'schedule_confirm_delete.html', {'schedule': schedule})


    
def calendar_view(request):
    return render(request, 'calendar.html')



def event_list(request):
    date = request.GET.get('date')  # e.g., 2025-05-05

    # Directly filter by DateField
    schedules = Schedule.objects.filter(date=date)

    data = []
    for schedule in schedules:
        data.append({
            'title': schedule.title,
            'description': schedule.description,
            'category': schedule.group,
            'start_date': schedule.date.strftime('%Y-%m-%d'),
            'time': schedule.time.strftime('%I:%M %p')  # format time nicely like "03:30 PM"
        })

    return JsonResponse(data, safe=False)