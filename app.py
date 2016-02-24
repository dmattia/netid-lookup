from flask import Flask, request, redirect
import twilio.twiml
from twilio_response import get_netid_info
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def index():
	from_number = request.values.get('From', None)
	body = request.values.get('Body', None)
	if body:
		body = body.rstrip().lstrip()
		message = get_netid_info(body)

		resp = twilio.twiml.Response()
		resp.message(message)
	 
		return str(resp)
	else:
		resp = twilio.twiml.Response()
		resp.message("Something went wrong")
		
		return str(resp)
 
if __name__ == "__main__":
	app.run(debug=False)
