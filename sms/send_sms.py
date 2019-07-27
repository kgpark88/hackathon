# https://www.twilio.com/docs/sms/quickstart/python#send-an-outbound-sms-with-python
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'twilio_account_si'
auth_token = 'twilio_auth_token'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+00000000000',
        to='+00000000000'
    )

print(message.sid)

