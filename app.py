from flask import Flask, request  , render_template , redirect ,flash
from mail2 import configure_mail, send_email  # Import the email configurations
from models import configure_db
from models import Contact   , db

app = Flask(__name__, template_folder="./templates" , static_folder="./static")

app.config['SECRET_KEY'] = 'thecreators@#' 
configure_mail(app)
configure_db(app)
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact' , methods=['GET'])
# def contact():
#     return render_template('contact.html')

@app.route('/email_sent', methods=['POST'])
def email_sent():
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        message = request.form.get('message')


        new_contact = Contact(name=name, lastname=lastname , email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()
        send_email(name,lastname ,  email, message)
        return render_template('index.html' ,  message="Your message has been sent!")


# @app.route('/service')
# def service():
#     return render_template('services.html')

# @app.route('/portfolio')
# def portfolio():
#     return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True)
