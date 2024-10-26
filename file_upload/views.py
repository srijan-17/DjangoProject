from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()  # Load environment variables


def file_upload_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return HttpResponse("No file uploaded.")

        EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

        try:
            # Load the file into a DataFrame
            if uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
                df = pd.read_excel(uploaded_file)
            elif uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                return HttpResponse("Unsupported file format. Please upload an Excel or CSV file.")

            # Remove any leading/trailing whitespace from column names
            df.columns = df.columns.str.strip()

            # Apply the filter to the DataFrame
            filtered_df = df[(df['Cust State'].isin(['ARUNACHAL PRADESH', 'JHARKHAND'])) & (df['DPD'] > 0)]

            # Check if filtered data is empty
            if filtered_df.empty:
                message = "No data matched the specified filters."
            else:
                # Convert filtered data to a formatted string table
                message = "Please find the below data:\n\n"
                message += filtered_df.to_string(index=False)

            # Send email with the filtered data
            subject = 'Python Assignment - Srijan Gupta'
            recipient_list = ['tech@themedius.ai']

            email = EmailMessage(subject, message, EMAIL_HOST_USER, recipient_list)
            email.send(fail_silently=False)

            return HttpResponse("Email with data sent successfully!")

        except Exception as e:
            return HttpResponse(f"Failed to process file or send email: {e}")

    return render(request, 'upload.html')
