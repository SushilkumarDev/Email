import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email credentials
your_email = "your mail"  //5u5h1lkum4r.y4d4v@gmail.com//
your_password = " mail pass please"  //hego epto znki gnze// # Avoid hardcoding sensitive data like this

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587  # TLS port

# Function to send email
def send_email(subject, body, to_email, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the body with the msg (HTML format)
    msg.attach(MIMEText(body, 'html'))

    # Attach resume
    try:
        part = MIMEBase('application', 'octet-stream')
        with open(attachment_path, 'rb') as attachment:
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="Mechanical_Sushilkumar Yadav.pdf"')
        msg.attach(part)

        print(f"Resume attached: {attachment_path}")
    
    except Exception as e:
        print(f"Failed to attach resume: {e}")

    try:
        # Connect to Gmail SMTP server and login
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Encrypt the connection
        server.login(your_email, your_password)

        # Send email
        text = msg.as_string()
        server.sendmail(your_email, to_email, text)

        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

    finally:
        server.quit()

# List of recipient emails (make sure these are real email addresses)
recipients = [
    "sushilkumaryadav9545@gmail.com",
    # Add more emails here if needed
]

# Email content with enhanced HTML formatting
subject = "Application for Design Opportunities - Mechanical Engineering Graduate (2025)"
body = """
<html>
  <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f4f4f4; color: #333;">
    <div style="background-color: #ffffff; padding: 20px; border-radius: 8px; max-width: 600px; margin: 0 auto;">
      <h2 style="color: #2C3E50; text-align: center;">Application for Design Opportunities - Mechanical Engineering Graduate (2025)</h2>
      
      <p style="font-size: 16px;">Dear Hiring Manager,</p>
      
      <p style="font-size: 16px;">I hope this message finds you well. My name is <b style="color: #2980B9;">Sushilkumar Baban Yadav</b>, and I am a <b style="color: #2980B9;">Mechanical Engineering student</b>, graduating in <b style="color: #2980B9;">2025</b>. I am reaching out to express my interest in career opportunities within the <b style="color: #2980B9;">design field</b> at your organization.</p>

      <p style="font-size: 16px;">Though I am still completing my studies, I have gained significant exposure to design principles in the context of mechanical engineering. My passion for <b style="color: #2980B9;">creative problem-solving</b> and <b style="color: #2980B9;">innovation</b> has driven me to pursue design-related projects throughout my academic career. I believe my background in engineering, combined with my eagerness to learn, would allow me to contribute effectively to your team.</p>

      <p style="font-size: 16px;">I have attached my resume for your review. I would appreciate the opportunity to discuss how my skills and interests could align with any <b style="color: #2980B9;">available roles</b> or <b style="color: #2980B9;">internship opportunities</b> within your organization.</p>
      
      <p style="font-size: 16px;">As a <b style="color: #2980B9;">recent graduate</b>, I am eager to apply my knowledge in a real-world setting and gain hands-on experience. I would be grateful for any guidance or recommendations you might have, and I look forward to the possibility of contributing to your team.</p>

      <p style="font-size: 16px;">Thank you for considering my application. I look forward to the opportunity to discuss my candidacy with you. Please feel free to contact me at your convenience to schedule an interview.</p>

      <br>

      <p style="font-size: 16px;">Best regards,</p>
      <p style="font-size: 16px; font-weight: bold; color: #2980B9;">Sushilkumar Baban Yadav</p>
      <p style="font-size: 16px;">Email: <a href="mailto:5u5h1lkum4r.y4d4v@gmail.com" style="color: #2980B9; font-weight: bold;">5u5h1lkum4r.y4d4v@gmail.com</a></p>
    </div>
  </body>
</html>
"""

# Loop to send emails with attachment
for recipient in recipients:
    send_email(subject, body, recipient, "Mechanical_Sushilkumar Yadav.pdf")
