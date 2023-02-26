import os
import time
import datetime

from twilio.rest import Client

account_sid = os.enviorn["TwilioKey"]  
auth_token = os.enviorn["TwilioToken"]
client = Client(account_sid, auth_token)


def send_sms(message,
             twilio_number,
             user_number,
             schedule_time=datetime.time(hour=13, minute=0)):
    while True:
        now = datetime.datetime.now()
        # Check if the current time matches the schedule time
        if (now.hour == schedule_time.hour
                and now.minute == schedule_time.minute):
            print("Program ran at ", now)
            # Send the SMS
            message = client.messages.create(body=message,
                                             from_=twilio_number,
                                             to=user_number)
            return message.sid

        time.sleep(60)
