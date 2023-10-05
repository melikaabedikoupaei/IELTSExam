###https://thecaferobot.com/learn/web-scraping-raspberry-pi-python-tutorial-guide/
from bs4 import BeautifulSoup 
import requests 
import re 
import smtplib 
from email.mime.multipart import MIMEMultipart
nothing_new=['بر اساس جستجوی شما هیچ آزمونی پیدا نشد. لطفا جستجوی انجام شده خود را اصلاح نمایید.\n']
exam_info = "" 
message_body=""
r = requests.get("https://irsafam.com/ielts/timetable?city%5B%5D=tehran&model%5B%5D=ielts&type%5B%5D=academic") 
soup = BeautifulSoup(r.text, 'html.parser') 
result = soup.find_all('div', attrs = {'class':'exam'}) 
 
for i in result: 
    exam_info += i.text.strip() 
    exam_info += "\n"
exam_info=[exam_info]
gmail_user = 'melikaabedi681375@gmail.com'  
gmail_password = 'sckl gryk bpkx mfgj'   #Enter your Email pasword 
sent_from = gmail_user   
to = ['melikaabedi681375@gmail.com']      #list of destination Email address 

    #Email title 
msg = """Subject:IeltsExam 
    """ 
    #add news to email massage 
message_body=""
if exam_info==nothing_new:
    message_body="nopeeee baby nothing changes"
else:
    message_body="check the irsafam.com website " 
msg += message_body

server = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
server.ehlo() 
server.login(gmail_user, gmail_password) 
server.sendmail(sent_from, to, msg) 
server.close() 

print ('Email sent!') 

 
