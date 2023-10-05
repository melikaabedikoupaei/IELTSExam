import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
import logging

class IeltsScraper:
    def __init__(self):
        pass

    def fetch_exam_info(self):
        url = "https://irsafam.com/ielts/timetable?city%5B%5D=tehran&model%5B%5D=ielts&type%5B%5D=academic"
        try:
            r = requests.get(url)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, 'html.parser')
            results = soup.find_all('div', attrs={'class': 'exam'})
            return [result.text.strip() for result in results]
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch exam info: {e}")
            return []

class EmailSender:
    def __init__(self, sender_email, sender_password, receiver_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email

    def send_email(self, subject, message_body):
        try:
            msg = """Subject:IeltsExam """ 
            msg += message_body


            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, [self.receiver_email], msg)
            server.close()
            logging.info("Email sent successfully")
        except Exception as e:
            logging.error("An error occurred while sending the email:", e)


def main():
    scraper = IeltsScraper()
    exam_info = scraper.fetch_exam_info()
    nothing_new=['بر اساس جستجوی شما هیچ آزمونی پیدا نشد. لطفا جستجوی انجام شده خود را اصلاح نمایید.']
    if exam_info==nothing_new:
        message_body = "No new exams found.baby.I love you "
    else:
        message_body = "check irsafam website baybe.kiss"

    sender_email = 'melikaabedi681375@gmail.com'
    sender_password = 'sckl gryk bpkx mfgj' 
    receiver_email = 'melikaabedi681375@gmail.com'

    email_sender = EmailSender(sender_email, sender_password, receiver_email)
    email_sender.send_email("IeltsExam", message_body)

if __name__ == "__main__":
    main()
