from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.shortcuts import render


def email(request):
    return render(request, 'email.html')



def send_email(request):
    if request.method == 'POST':
        email = request.POST['email']

        body = 'Hii your work has been done'
        try:
            email = EmailMessage('Smartcatcher', body, to=[email])
            k = email.send()
        except:
            print("An exception occurred")
            message = '''<script language="javascript">
                                                alert('may be password is not entered');
                                                </script>'''
            return render(request, 'email.html', {'message': message})

        message = '''<script language="javascript">
                                    alert('YOur  email has been send');
                                    </script>'''
        return render(request,'email.html',{'message':message})
