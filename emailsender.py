import smtplib

# this will prompt the user to enter the email address of the recipent (the person they wish to send an email)
to = input("Enter the email address of the recipient\n")

# this will prompt the user to enter the subject of the email (more of like caption - reason for sending the email address)
subject = input("Enter the subject of the email\n")

# this will prompt the user to enter the content of the email (this is where you enter the message you wish to pass to the recipient)
content = input("Enter the content of the email\n")

def sendEmail(to, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senderemailaddress@gmail.com', 'password')
    server.sendmail('senderemailaddress@gmail.com', to, subject, content)
    server.close()

sendEmail(to, subject, content)