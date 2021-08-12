import smtplib
import getpass
    
sender_email = ""
rec_email = ""
password = getpass.getpass("Plz type your password:")
message = "Alert! Security Breach"
    
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email, password)
print("Login Successful")
    
#sending mail
server.sendmail(sender_email, rec_email, message)
server.quit()
