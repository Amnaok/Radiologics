from django.shortcuts import render

# Create your views here.



# views.py
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import ContactUs
from .Serializers import ContactMessageSerializer
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
@api_view(['GET'])
def getRoutes(request):
    return Response('hello')

# api/views.py
class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactMessageSerializer


    


    # @api_view(['POST'])
    # def send_email(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     # save data
    #     self.perform_create(serializer)

    #     # send email using send_mail
    #     subject = 'New Contact Form Submission'
    #     message_body = f'Name: {serializer.validated_data["name"]}\nEmail: {serializer.validated_data["email"]}\nPhone: {serializer.validated_data["phone"]}\nMessage: {serializer.validated_data["message"]}'
    #     from_email = settings.DEFAULT_FROM_EMAIL  # Use the default from your settings
    #     to_email = ['amnatariqok@gmail.com']  # Replace with your email address or recipients

    #     send_mail(subject, message_body, from_email, to_email, fail_silently=False)

    #     return JsonResponse({'message': 'Email sent successfully'})


# api/views.py
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
@api_view(['POST'])
def send_email(request):
    data = request.POST
    name = data.get('name')
    email = data.get('email')
   
    message = data.get('message')
  


    subject = 'New Mail from SOS Page'
    message_body = f'An Email has been sent you by  {name}.\n \n{message}\n\nContact Information is as follows. \n\n Email:  {email}    '
    from_email = email
    to_email = ['amnatariqok@gmail.com','noorshahidok@gmail.com']

    try:
        send_mail(subject, message_body, from_email, to_email, fail_silently=False)
        return JsonResponse({'message': 'Email sent successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)})



from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

