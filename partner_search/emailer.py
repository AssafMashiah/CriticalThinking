'''
Created on 2013-01-09

@author: Gord
'''

import smtplib
from email.mime.text import MIMEText
import getpass

class emailer(object):
    '''
    Class to send emails to dancers as part of a partner search
    '''


    def __init__(self):
        self.sender = str()
        self.subject = str()
        self.isSetup = 0
        
        ## This is the server info for gmail
        server = 'smtp.gmail.com'
        port = 587
        
        ## Info for the gmail account sending the mail
        ## should change this to command line parameters or run an smtp server locally
        
        self.sender = raw_input('Enter gmail address to send from: ')
        print('Sending from: ' + self.sender)
        password = getpass.getpass('enter password: ')
        
        self.subject = 'Partner Search'
        
        ## Set up the session with the smtp server
        self.session = smtplib.SMTP(server, port)
        self.session.ehlo()
        self.session.starttls()
        self.session.ehlo
        self.session.login(self.sender, password)
        
    
    def sendEmail(self, recipient):
        ## Sends an e-mail with matches to the recipient dancer
        
        body = "Thank you for participating in UBC Dance Club's partner search, "
        body += recipient.get_first_name() + ".\n\r\n\r"
        
        if(len(recipient.matches) > 0):
            body += "Your matches are as follows: " + recipient.get_matches_string() + ""
        else:
            body += "Unfortunately, we were unsuccessful in pairing you with an individual that met your qualifications. If you would like to discuss this further, please email Holly Zhou at president@ubcdanceclub.com. \n\rAgain, thank you for your interest and we hope to see you dancing at UBC Gala Ball."

        headers = ["From: " + self.sender,
                   "Subject: " + self.subject,
                   "To: " + recipient.name,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)
         
        self.session.sendmail(self.sender, recipient.email, headers + "\r\n\r\n" + body)
        print("Sent mail to " + recipient.name + ", with " + str(len(recipient.matches)) + " matches.")
        
    def quitEmail(self):
        "Ends the email session."
        self.session.quit()
    