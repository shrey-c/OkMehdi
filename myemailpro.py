import smtplib
from email.message import EmailMessage

def sendemail(from_addr, to_addr, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.send_message(msg)
    #problems = server.sendmail(from_addr, to_addr_list, message)
    
    server.quit()
