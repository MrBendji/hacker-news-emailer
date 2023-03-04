# Import necessary modules
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Initialize the content variable
content = ''

# Define a function to extract news from Hacker News URL
def extract_news(url):
    print("Extracting Hacker News Stories...")

    # Initialize the cnt variable
    cnt = ''

    # Add title and separator to cnt variable
    cnt += ('<b>HN Top Stories:</b>'+'\n'+'<br>'+'-'*50+'<br>')

    # Send a GET request to the URL and extract HTML content
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    # Extract news articles and append to cnt variable
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+' :: '+tag.text + '\n' +
                '<br>') if tag.text != 'More' else '')

    # Return the cnt variable
    return cnt

# Call the extract_news function and append news articles to content variable
cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<b>-----------<b>')
content += ("<br><br>End of Message")

# Initialize email server details and create a MIMEMultipart message object
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = ''
TO = ''
PASS = ''
msg = MIMEMultipart()

# Set subject, sender, and recipient fields of the message object
msg["Subject"] = 'Top New Stories HN [Automated Email]' + \
    ' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From'] = FROM
msg['To'] = TO

# Attach content as HTML text to the message object
msg.attach(MIMEText(content, 'html'))

# Set up the SMTP server, initiate connection, and send email
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())
server.quit()
