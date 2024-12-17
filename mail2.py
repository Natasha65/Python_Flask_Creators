from flask_mail import Mail, Message 
from flask import flash

mail = Mail()

def configure_mail(app):
    # Configure email settings for the app
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False  # Disable SSL when using TLS
    app.config['MAIL_USERNAME'] = 'swenatasha@gmail.com'
    app.config['MAIL_PASSWORD'] = 'cvooibzmewepqscp'
    mail.init_app(app)

def send_email(name, lastname ,email, message_body):
    try:
        msg = Message(f"New Contact Form Submission from {name}",
                      sender='swenatasha@gmail.com',
                      recipients=['thecreators234@gmail.com'])  # Replace with your recipient
        msg.body = f"Name: {name}\nLast Name: {lastname}\nEmail: {email}\nMessage:\n{message_body}"
        mail.send(msg)
        print("sent")
        return True
    except Exception as e:
        flash(f"An error occurred: {e}", 'error')
        return False
