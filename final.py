'''
Dwight Johnson / Final / 3-15-2018

Include a function that takes at least two user arguments from the command line
x Contain at least one if/else statement
Perform a calculation on a list
Use at least one dictionary
x Have one try/except clause for every function
Output something (write) to a file, using string formatting
x Must include docstrings telling us how to run your script.
x Either create a class to contain the related functions OR output a simple graph

/// How to run the script ///

Instructions:
1: Follow the steps here to allow pythons gmail api https://developers.google.com/gmail/api/quickstart/python
2: Run the script with "python final.py" on the command line

/// END ///

'''
import smtplib

def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

send_email('dwightjay1@gmail.com', 'uwpythonfinal', 'dwightjay1@gmail.com', 'TEST', 'IT WORKED!!!!')
