import smtplib, ssl
'''
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "joglekarsumedh@gmail.com"
receiver_email = "sjogleka@uncc.edu"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
'''
fromaddr = 'joglekarsumedh@gmail.com'
toaddrs  = ['joglekarsumedh@gmail.com']
msg = '''
    From: {fromaddr}
    To: {toaddr}
    Subject: testin'     
    This is a test 
    .
'''
server.starttls()
print("Connection Opened")
server.ehlo("joglekarsumedh@gmail.com")
server.mail(fromaddr)
server.rcpt(toaddrs[0])
server.data(msg)
server.quit()