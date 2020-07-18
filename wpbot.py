from flask import Flask, request #To define the bot webhook
from twilio.twiml.messaging_response import MessagingResponse #Accessing to the Twilio API's relevant method
import monedavzla 

#So Flask could know the place where the app is defined
app = Flask(__name__) 

#Defining webhook's edge or route to the relevant bot's procedures, with reference to http POST method
@app.route('/wpbot', methods=['POST'])
def wpbot():

	#Requesting incoming message
	incoming_msg = request.values.get('Body', '').lower() 

	#Formatting to Twilio parameters
	resp = MessagingResponse() 

	#The bot response
	msg = resp.message()

	#Relevant control flows 
	if 'moneda' in incoming_msg:
		msg.body(monedavzla.curr_values)
	elif 'dolar' in incoming_msg:
		msg.body(monedavzla.curr_values)
	elif 'euro' in incoming_msg:
		msg.body(monedavzla.curr_values)
	elif 'paypal' in incoming_msg:
		msg.body(monedavzla.curr_values)
	else:
		msg.body("Solo conozco información respecto a valores actuales monetarios venezolanos.\n\nSi le interesa, envíeme un mensaje con la palabra \"moneda\", \"dolar\", \"euro\" o \"paypal\"")
	
	#Returning the bot response
	return str(resp)

if __name__ == '__main__':
	app.run()
