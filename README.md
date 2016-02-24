# netid-lookup
An sms based service to respond with directory information for a given netid

# Usage #

Text any Notre Dame netid to (574)318-0123 and receive an sms response with their basic information

# How it works

I setup a flask app on heroku that sends a twiml response containing a user's information to my twilio account based upon the contents of the sender's message.  I find a user's information using Notre Dame's netid api found here: http://dev.nd.edu/apis/json-netid-attributes/
