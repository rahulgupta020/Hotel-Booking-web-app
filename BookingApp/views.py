from django.shortcuts import render,redirect
from django.http import HttpResponse
from BookingApp.forms import BookingForm

def Booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/BookingSuccess')
            except:
                pass
    else:
        form=BookingForm()
    return render(request,'BookingApp/booking.html', {'form':form})

def BookingSuccess(request):
    return render(request, 'BookingApp/BookingSuccess.html')