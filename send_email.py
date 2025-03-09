import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def send_certificate(name: str, email: str):
    client = boto3.client(
        'ses',
        region_name='us-east-1',
        aws_access_key_id='AKIAYF4JFVMXAV5YHEUF',
        aws_secret_access_key=os.getenv('AWS_SECRET')
    )

    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    message = MIMEMultipart()
    message['Subject'] = 'Certificate of Attendance for the Scrum Day Nigeria - Lagos 2025 conference'
    message['From'] = 'info@valuehut.co'
    message['To'] = email
    # message body
    text = """\
        <html>
          <body>
            <p>Dear %s,<br>
              Please find attached the certificate of attendance for the Scrum Day Nigeria - Lagos 2025 conference.</p>
            <p>I look forward to seeing you at the next year conference.</p>
            <p> Kind Regards,</p>
            <p> Sam Adesoga </p>
            <p> Convener, Scrum Day Nigeria </p>
          </body>
        </html>""" % name
    part = MIMEText(text, 'html')


    message.attach(part)
    # attachment

    part = MIMEApplication(open("generated/" + name +".png", 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=name +".png")
    message.attach(part)
    response = client.send_raw_email(
        Source=message['From'],
        Destinations=[email],
        RawMessage={
            'Data': message.as_string()
        }
    )
