#/usr/bin/python
import os 
from selenium import webdriver
import io
import urllib
import time
from selenium.webdriver.chrome.options import Options
from datetime import timedelta
import datetime
import shutil

options = Options()
options.headless = False
driver = webdriver.Chrome(chrome_options=options)

driver.get ("https://sintegre.ons.org.br/")
driver.find_element_by_id("username").send_keys("jose_cpfl")
driver.find_element_by_id ("password").send_keys("bbAA4433!!")
driver.find_element_by_name("submit.Signin").click()

time.sleep(7.5)

flag = True
while flag == True:

   Dia = (datetime.date.today() - timedelta(days=1)).strftime('%d')
   print(Dia)
   #print("HAHA, voltei ")
   driver.get ("https://sintegre.ons.org.br/sites/7/39/_layouts/download.aspx?SourceUrl=/sites/7/39/Produtos/155/IPDO-" + str(Dia) + "-09-2019.pdf")
   time.sleep(9.5)

   path = 'C:\\Users\\jose.eustaquio\\Downloads'
   files = []

   for r, d, f in os.walk(path):
      for file in f:
         if "IPDO" in file:
            files.append(file)

   # puxar arquivos e ver se de fato ele baixou; se baixou, continua o fluxo; caso não, volta pro loop 
   if "IPDO-" + str(Dia) + "-09-2019.pdf" in files: 
      shutil.move("C:\\Users\\jose.eustaquio\\Downloads\\IPDO-" + str(Dia) + "-09-2019.pdf", "C:\\Users\\jose.eustaquio\\Downloads\\IPDO")
      print("saiu o IPDO") 
      break #sai do loop e vai enviar o email 
   
   else:
      time.sleep(10.5)
      print("não saiu IPDO")

driver.close()

###############################################

# Parte que envia o email 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders 
from email.mime.image import MIMEImage
import smtplib

# Define these once; use them twice!
strFrom = 'carmo.jose.eng@gmail.com'
strTo = 'jose.eustaquio@cpflrenovaveis.com.br, masterjecj@hotmail.com'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'IPDO_' + str(Dia) + "-09-2019"
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<br> Bom dia, <br> <br> Segue em anexo o Informativo Preliminar da Operação Diária atualizado.', 'html')

msgAlternative.attach(msgText)

fp = open("C:\\Users\\jose.eustaquio\\Downloads\\IPDO\\IPDO-" + str(Dia) + "-09-2019.pdf", 'rb')

msgDocument = MIMEBase('application', "octet-stream")
msgDocument.set_payload(fp.read())

encoders.encode_base64(msgDocument)

fp.close()

msgDocument.add_header('Content-Disposition', 'attachment', filename="IPDO-" + str(Dia) + "-09-2019.pdf")

msgRoot.attach(msgDocument)

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

fromaddr = "carmo.jose.eng@gmail.com"
toaddr = "jose.eustaquio@cpflrenovaveis.com.br", "masterjecj@hotmail.com"

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, "bbAA44330") 

# Converts the Multipart msg into a string 
text = msgRoot.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 

# fim, o email foi enviado com o IPDO atualizado
