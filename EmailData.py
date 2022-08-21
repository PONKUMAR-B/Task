
import smtplib
import imaplib,email
import pymysql

sender_email = "ponkumarbalasubramanian@gmail.com"
password = input("Type your password and press enter: ")
receiver_email="ponkumarvirat@gmail.com"
message = """\
Subject: Hi there

This message is sent from smtp."""

# Try to log in to server and send email
try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() 
    server.starttls
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Mail send successfully")

except:
    print("Cannot send mail")
finally:
    server.quit() 



username ="ponkumarbalasubramanian@gmail.com"
app_password= "mgrxigyovunbwonu"
gmail_host= 'imap.gmail.com'

#set connection
mail = imaplib.IMAP4_SSL(gmail_host)
mail.login(username, app_password)
mail.select("INBOX")

_, selected_mails = mail.search(None, '(FROM "ponkumarbalasubramanian@gmail.com")')

#total number of mails from specific user
print("Total Messages from ponkumarbalasubramanian@gmail.com:" , len(selected_mails[0].split()))

for num in selected_mails[0].split():
    _, data = mail.fetch(num , '(RFC822)')
    _, bytes_data = data[0]

email_message = email.message_from_bytes(data[0][1])
print("\n===========================================")

for part in email_message.walk():
    if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
        message = part.get_payload(decode=True)
        print("Message: \n", message.decode())
        print("==========================================\n")
        break

#access data
subject = print("Subject: ",email_message["subject"])
to_attr = print("To:", email_message["to"])
from_attr = print("From: ",email_message["from"])
print("Date: ",email_message["date"])

collect_records="{},{},{}".format(subject,to_attr,from_attr)
con = pymysql.connect(host="localhost",user="root",password="",db="maildata")
cursor = con.cursor()
cmd1 = "insert into mailtable values ('%s')" %(collect_records)
cursor.execute(cmd1)
cmd2 = "select * from mailtable"
cursor.execute(cmd2)
data = cursor.fetchall()
for row in  data:
    print(row[0],row[1],row[2])

con.commit()
print("Record inserted")
con.close()