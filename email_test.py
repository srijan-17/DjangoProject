import os
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define email settings (replace with your actual SMTP host details)
EMAIL_HOST = 'smtp.gmail.com'        # Replace with your SMTP server
EMAIL_PORT = 587                      # Typically 587 for TLS
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

try:
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()  # Start TLS encryption
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")
