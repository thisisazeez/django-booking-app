from django.shortcuts import render
from django.core.mail import send_mail
from .models import Days, Doctors, Time


def appointment(request):
    days = Days.objects.all()
    time = Time.objects.all()
    doctor = Doctors.objects.all()
    context = {
        'days':days,
        'time':time,
        'doctor':doctor,
    }
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone  = request.POST['your-phone']
        your_email  = request.POST['your-email']
        your_address  = request.POST['your-address']
        your_schedule  = request.POST['your-schedule']
        your_date  = request.POST['your-date']
        your_doctor  = request.POST['your-doctor']
        your_message  = request.POST['your-message']
		
        
        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Day: " + your_date + " Message: " + your_message + "Doctor:" + your_doctor
        send_mail(
            'Appointment Request',
            appointment,
			your_email,

            ['abdoulazeezx@gmail.com']
        )

        return render(request, 'appointment.html', {
            'your_name' : your_name,
            'your_phone' : your_phone,
            'your_email' : your_email,
            'your_address' : your_address,
            'your_schedule':your_schedule,
            'your_date' : your_date,
            'your_doctor':your_doctor,
            'your_message':your_message
            })

    else:
        return render(request, 'home.html', context)