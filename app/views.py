from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone  = request.POST['your-phone']
        your_email  = request.POST['your-email']
        your_address  = request.POST['your-address']
        your_schedule  = request.POST['your-schedule']
        your_date  = request.POST['your-date']
        # your_doctor  = request.POST['your-doctor']
        your_message  = request.POST['your-message']

        # send_mail(
        #     'Appointment Request',
        #     your_name,
        #     your_email,
        #     # your_doctor,
        #     your_message,
        #     your_date,
        #     your_schedule,
        #     ['replymeback2@gmail.com']
        # )

        return render(request, 'appointment.html', {
            'your_name' : your_name,
            'your_phone' : your_phone,
            'your_email' : your_email,
            'your_address' : your_address,
            'your_schedule':your_schedule,
            'your_date' : your_date,
            # 'your_doctor':your_doctor,
            'your_message':your_message
            })

    else:
        return render(request, 'home.html', {})