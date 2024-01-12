import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace these with your own values
repository_owner = 'aryaparasharmrt'
repository_name = 'Python4'
access_token = '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'
notification_recipient = 'aryaparasharj007@gmail.com'

def get_closed_milestones():
    url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/milestones'
    headers = {'Authorization': f'token {access_token}'}
    params = {'state': 'closed', 'sort': 'updated', 'direction': 'desc'}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch milestones. Status Code: {response.status_code}')
        return None

def send_notification(milestone):
    # Replace this with your preferred notification method (email, Slack, etc.)
    # Example: Send an email

    sender_email = 'aryaparasharj02@gmail.com'
    sender_password = 'Gmail123@#123'
    recipient_email = 'aryaparasharj02@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
  
    subject = f'Milestone Closed: {milestone["title"]}'
    body = f'The milestone "{milestone["title"]}" has been closed on {milestone["closed_at"]}.'
    # Implement your email sending logic here

    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

        # Attach body to the message
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Close the connection
        server.quit()

        print(f'Notification sent: {subject}\n{body}')

    except Exception as e:
        print(f'Failed to send notification. Error: {str(e)}')


    print(f'Notification sent: {subject}\n{body}')

def check_and_notify():
    milestones = get_closed_milestones()

    if milestones:
        for milestone in milestones:
            # Convert GitHub API datetime format to a more readable format
            milestone['closed_at'] = datetime.strptime(milestone['closed_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
            send_notification(milestone)

if __name__ == '__main__':
    check_and_notify()
