from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.mailgun.org'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'postmaster@sandboxc3c8395066d14f9c8bcdd4f02cc33841.mailgun.org'
app.config['MAIL_PASSWORD'] = '7354ecddfd649340987e3b9c22db2680'  # Use your Mailgun API key here
app.config['MAIL_DEFAULT_SENDER'] = 'abinayatamilselvan7@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/send_email', methods=['POST'])
def send_email():
    print("Received POST request to /send_email")
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Update this to include your email
    msg = Message(subject, recipients=['abinayatamilselvan7@gmail.com'])  # Your email
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    try:
        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')

    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(debug=True)

