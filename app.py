# import random
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from flask import Flask, render_template, request, redirect, url_for
# import stripe
# from pymongo import MongoClient
# from flask_mail import Mail, Message

# app = Flask(__name__)

# cluster = MongoClient('mongodb+srv://lakshmansoma1313:lakshman@cluster0.evfapf9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
# db = cluster['ehealth']
# ops = db['ops']

# email=""
# name=""

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/book', methods=['POST'])
# def book():
#     global email, name
#     name = request.form['name']
#     email = request.form['email']
#     date = request.form['date']
#     dept = request.form['dept']
#     phone = request.form['phone']
#     message = request.form['message']
#     _op = ops.find_one({'date': date})
#     if _op:
#         return render_template('confirmation.html', status='already booked with same date', name='name: '+name, email='email: '+email, date='Your appointment date: '+date, dept='Department: '+dept, phone='Phone: '+phone)
#     ops.insert_one({"name": name, "email": email, "date": date, "dept": dept, "phone": phone, "message": message})
#     send_email()  # Call the function to send the email
#     return render_template('confirmation.html', status='BOOKING CONFIRMED', name='name: '+name, email='email: '+email, date='Your appointment date: '+date, dept='Department: '+dept, phone='Phone: '+phone)

# @app.route('/payment', methods=['GET', 'POST'])
# def payment():
#     publishable_key = "pk_test_51OxLmRSAadpL2s7R8Ij7qpsCAvvtw03HslJzsqJS0W0vgQ78JwtYzX7qpwt7ZU4GLzLNu2uQ2zpXVmCq1D4qtf9P00z0fkO9jx"
#     return render_template('payment.html', publishable_key=publishable_key)

# stripe.api_key = "sk_test_51OxLmRSAadpL2s7RWUQABYW4FiVOkFLYPqDfPcI6LK2uzmzwWpvHi3fBGSctgHgL4sM9eajV893JPOLr0TEVkfxD00OB3h0FPv"

# @app.route('/process_payment', methods=['POST','GET'])
# def process_payment():
#     # Get the amount from the form
#     amount = int(request.form['amount'])
    
#     # Create a Checkout Session
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=[{
#             'price_data': {
#                 'currency': 'inr',
#                 'unit_amount': amount * 100,  # Amount in cents
#                 'product_data': {
#                     'name': 'Appointment Payment',
#                 },
#             },
#             'quantity': 1,
#         }],
#         mode='payment',
#         success_url=url_for('payment_success', _external=True),
#         cancel_url=url_for('home', _external=True),
#     )
#     return render_template('payment_success.html')

# @app.route('/payment/success')
# def send_email():
#     # Email configuration
#     sender_email = "asifshaik33456@gmail.com"
#     receiver_email = "saikiransk6342@gmail.com"
#     password = "ndsdsiarpucrrazs"

#     # Create a multipart message
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = "Token ID: "+ str(random.randint(100, 999))

#     # Add body to email
#     body = "Hi sai kiran,Your appointment has been booked successfully."
#     message.attach(MIMEText(body, "plain"))

#     # Connect to Gmail's SMTP server
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()  # Secure the connection
#         server.login(sender_email, password)
#         text = message.as_string()
#         server.sendmail(sender_email, receiver_email, text)

#     print("Email sent successfully!")

# def payment_success():
#    return render_template('payment_success.html')

# from datetime import datetime

# @app.route('/check_appointment', methods=['POST','GET'])
# def check_appointment():
#     email = request.args.get('email', '')  # assuming we use email to identify the user
#     today = datetime.now().strftime('%Y-%m-%d')

#     # Query the database for the user's appointment
#     appointment = ops.find_one({'email': email})

#     if appointment:
#         appointment_date = appointment.get('date', '')

#         # Compare the appointment date with today's date
#         if appointment_date == today:
#             # Render a page for today's appointment with video call option
#             return render_template('appointment_today.html', appointment=appointment)
#         else:
#             # Render a page showing appointment details and a message since it's not today
#             return render_template('appointment_details.html', appointment=appointment, message="Your appointment is not today.")
#     else:
#         # Handle the case where no appointment is found
#         return "No appointment found for the provided email."

# if __name__ == "__main__":
#     app.run(host="0.0.0.0")


import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, redirect, url_for
import stripe
from pymongo import MongoClient
from flask_mail import Mail, Message

app = Flask(__name__)

# MongoDB setup
cluster = MongoClient('mongodb+srv://lakshmansoma1313:lakshman@cluster0.evfapf9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cluster['ehealth']
ops = db['ops']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    dept = request.form['dept']
    phone = request.form['phone']
    message = request.form['message']
    def send_email():
    # Email configuration
        sender_email = "asifshaik33456@gmail.com"
        receiver_email = email
        password = "ndsdsiarpucrrazs"

        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Token ID: " +str(random.randint(100,999))

        # Add body to email
        body = "Hi "+name+" ,Your appointment has been booked successfully."
        message.attach(MIMEText(body, "plain"))

        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)

        print("Email sent successfully!")

# Call the function to send the email
    send_email()

    # Check if the appointment already exists for the selected date
    _op = ops.find_one({'date': date})
    if _op:
        return render_template('confirmation.html', status='already booked with same date', name='name: '+name, email='email: '+email, date='Your appointment date: '+date, dept='Department: '+dept, phone='Phone: '+phone)

    # Insert appointment into the database
    ops.insert_one({"name": name, "email": email, "date": date, "dept": dept, "phone": phone, "message": message})
    
    # # Send email confirmation
    # send_email_confirmation(name, email)

    return render_template('confirmation.html', status='BOOKING CONFIRMED', name='name: '+name, email='email: '+email, date='Your appointment date: '+date, dept='Department: '+dept, phone='Phone: '+phone)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    publishable_key = "pk_test_51OxLmRSAadpL2s7R8Ij7qpsCAvvtw03HslJzsqJS0W0vgQ78JwtYzX7qpwt7ZU4GLzLNu2uQ2zpXVmCq1D4qtf9P00z0fkO9jx"
    return render_template('payment.html', publishable_key=publishable_key)

# Stripe API key
stripe.api_key = "sk_test_51OxLmRSAadpL2s7RWUQABYW4FiVOkFLYPqDfPcI6LK2uzmzwWpvHi3fBGSctgHgL4sM9eajV893JPOLr0TEVkfxD00OB3h0FPv"



@app.route('/process_payment', methods=['POST','GET'])

def process_payment():
    # Get the amount from the form
    amount = int(request.form['amount'])
    
    # Create a Checkout Session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'unit_amount': amount * 100,  # Amount in cents
                'product_data': {
                    'name': 'Appointment Payment',
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('payment_success', _external=True),
        cancel_url=url_for('home', _external=True),
    )
    return render_template('payment_success.html')

@app.route('/payment/success')
def payment_success():
    return render_template('payment_success.html')

from datetime import datetime

@app.route('/check_appointment', methods=['POST','GET'])
def check_appointment():
    email = request.args.get('email', '')  # assuming we use email to identify the user
    today = datetime.now().strftime('%Y-%m-%d')

    # Query the database for the user's appointment
    appointment = ops.find_one({'email': email})

    if appointment:
        appointment_date = appointment.get('date', '')

        # Compare the appointment date with today's date
        if appointment_date == today:
            # Render a page for today's appointment with video call option
            return render_template('appointment_today.html', appointment=appointment)
        else:
            # Render a page showing appointment details and a message since it's not today
            return render_template('appointment_details.html', appointment=appointment, message="Your appointment is not today.")
    else:
        # Handle the case where no appointment is found
        return "No appointment found for the provided email."

if __name__ == "__main__":
    app.run(host="0.0.0.0")