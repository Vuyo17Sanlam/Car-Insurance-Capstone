from mailersend import emails

# Your MailerSend API key
api_key = "mlsn.12a484d76826acf75f0420f42c62fd690ec0175d4454b7d341cea5556a270688"

# Create a MailerSend email object
mailer = emails.NewEmail(api_key)

# Define the mail sender (From)
mail_from = {
    "name": "Luvuyo",
    "email": "trial-nrw7gym9n32g2k8e.mlsender.net",  # Your verified sender email address
}

# Define the recipient(s)
recipients = [
    {
        "name": "John Doe",
        "email": "sweetnessmatomela@gmail.com",  # Recipient's email
    }
]

# Define the reply-to email (optional)
reply_to = [
    {
        "name": "Luvuyo",
        "email": "luvuyomatomela17@gmail.com",  # Reply-to email
    }
]

# Prepare the email body content
mail_body = {}

# Set the sender and recipient
mailer.set_mail_from(mail_from, mail_body)
mailer.set_mail_to(recipients, mail_body)

# Set the subject of the email
mailer.set_subject("Test Email from MailerSend", mail_body)

# Set the HTML content of the email
mailer.set_html_content(
    "<h1>Hello, John!</h1><p>This is a test email sent via MailerSend.</p>", mail_body
)

# Set the plain text content (a fallback for email clients that do not support HTML)
mailer.set_plaintext_content(
    "Hello, John! This is a test email sent via MailerSend.", mail_body
)

# Set the reply-to address
mailer.set_reply_to(reply_to, mail_body)

# Send the email
response = mailer.send(mail_body)

# Print the response to check the status
print(response)
