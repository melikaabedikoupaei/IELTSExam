from bs4 import BeautifulSoup 
import requests 
import smtplib 
from email.mime.multipart import MIMEMultipart
class IeltsExam:
    def __init__(self):
        self.nothing_new=['بر اساس جستجوی شما هیچ آزمونی پیدا نشد. لطفا جستجوی انجام شده خود را اصلاح نمایید.\n']
        self.exam_info = "" 
        self.message_body=""
        self.gmail_user = 'melikaabedi681375@gmail.com'  
        self.gmail_password = 'sckl gryk bpkx mfgj'
        self.receiver_email_address='ghazalrezaei2001@gmail.com' 
    def request_for_information(self):
        r = requests.get("https://irsafam.com/ielts/timetable?city%5B%5D=tehran&model%5B%5D=ielts&type%5B%5D=academic") 
        soup = BeautifulSoup(r.text, 'html.parser') 
        result = soup.find_all('div', attrs = {'class':'exam'})
        return result 
    def body_of_email(self):
        results = self.request_for_information()
        for i in results: 
            self.exam_info += i.text.strip() 
            self.exam_info+= "\n"
        self.exam_info=[self.exam_info]
        if self.exam_info==self.nothing_new:
            self.message_body="nopeeee baby nothing changes"
        else:
            self.message_body="check the irsafam.com website "
        return self.message_body
    def send_email(self):
        try:
            sent_from = self.gmail_user
            to = [self.receiver_email_address]
            msg = """Subject:IeltsExam """
            msg += self.body_of_email()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.gmail_user, self.gmail_password)
            server.sendmail(sent_from, to, msg)
            server.close()
            print("email sent successfully")
        except Exception as e:
            print("An error occurred while sending the email:", e)

email_sender = IeltsExam()
email_sender.send_email()



 
