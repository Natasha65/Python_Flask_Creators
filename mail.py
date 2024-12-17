
from flask_mail import Mail, Message

mail = Mail()

  
def configure_mail(app):
    # Email configuration (using Gmail)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False  # Disable SSL when using TLS
    app.config['MAIL_USERNAME'] = 'swenatasha@gmail.com'
    app.config['MAIL_PASSWORD'] = 'cvooibzmewepqscp'
    mail.init_app(app)


      