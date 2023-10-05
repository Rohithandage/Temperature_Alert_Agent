● Project name :

Temperature Alert Agent

● Description of the project :

Your challenge is to create the Temperature Alert Agent using uAgent library, a tool that:
a) Connects to a free weather API to fetch real-time temperatures for the specified location.
b) Lets users set their preferred temperature range (e.g., a minimum and maximum temperature) and
location.
c) Sends an alert/notification to the user when the current temperature in their chosen
location goes below the minimum or above the maximum threshold they've set.
d) In the alert/notification user can see the current temperature and the current weather of chosen location they've set.

● Instructions to run the project :

Python 3.8, 3.9 or 3.10.

PIP (Python Installs Packages).

Poetry for virtual environments (optional).

uAgents framework

Twilio for Sending Notifications:

A] Twilio Account Setup:
If you don't already have one, sign up for a Twilio account at Twilio.
Once registered, you'll need to obtain the following credentials:
Twilio Account SID
Twilio Auth Token
Twilio Phone Number (a phone number you've purchased or received from Twilio)
Recipient Phone Number (the phone number where you want to receive notifications)

R]Configuration in the Script:
Open the Python script  and replace the following placeholders with your Twilio credentials:
Twilio credentials (replace with your actual Twilio credentials) TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID' TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN' TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER' TO_PHONE_NUMBER = 'RECIPIENT_PHONE_NUMBER'

Sending SMS Alerts:
Twilio API to send SMS messages :Python def send_sms_alert(message): client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) client.messages.create( to=TO_PHONE_NUMBER, from_=TWILIO_PHONE_NUMBER, body=message )

 CONSOL Window : 
 python filename.py
 Then You Have To,
 Enter City :
 Enter Minimum Temperature :
 Enter Maximum Temperature:

 Output : 
 After that you will see the minimum or maximum Temperature in the alert notification.
 Cuurent Temperature in the alert notification.
 Also Cuurent Weather in the alert notification.