from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables


def file_upload_view(request):
    if request.method == 'POST' and request.FILES['file']:
        # Handle file upload and sending email here

        uploaded_file = request.FILES['file']

        # Get email configuration
        EMAIL_HOST = os.getenv('EMAIL_HOST')
        EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
        EMAIL_PORT = int(os.getenv('EMAIL_PORT'))

        # Your email sending logic goes here
        try:
            send_mail(
                subject='Python Assignment - Srijan Gupta',
                message='Your email body here',
                from_email=EMAIL_HOST_USER,
                recipient_list=['tech@themedius.ai'],
                fail_silently=False,
            )
            return HttpResponse("Email sent successfully!")  # Return a response
        except Exception as e:
            return HttpResponse(f"Failed to send email: {e}")  # Return an error response

    # Render the upload form for GET requests
    return render(request, 'upload.html')  # Ensure you have an upload.html template
