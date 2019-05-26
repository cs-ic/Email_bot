import smtplib

#send_email function
def send_email(subject, msg):
    
    #define the email address and password to login in server
    #change the email and password before using
    FROM_EMAIL_ADDRESS = "xyz@gmail.com" 
    PASSWORD = "123456"
    TO_EMAIL_ADDRESS = "abc@gmail.com"

    try: 
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(FROM_EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(TO_EMAIL_ADDRESS,TO_EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email Sent")
    except:
        print("Email failed to sent")

#define the subject and msg
subject = "Test subject"
msg = "hello there, how are you today?"

#executing the script
send_email(subject, msg)