import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = '2525'
    smtp_server = 'smtp.mailtrap.io'
    login = 'd149cf21b6d6e9'
    password = '4bccc1de8ce21c'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {
        dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    sender_email = 'd149cf21b6d6e9@smtp.mailtrap.io'
    receiver_email = 'd149cf21b6d6e9@smtp.mailtrap.io'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
