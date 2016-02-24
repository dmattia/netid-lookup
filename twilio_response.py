import requests
import json

def get_netid_info(netid):
	url = 'http://ur.nd.edu/request/eds.php?uid=' + netid + '&full_response=true'
	
	r = requests.get(url)
	sms_body = ""
	
	if r.status_code == 200:
		try:
			j = r.json()
			
			sms_body += 'Full Name: ' + j['ndformalname'] + '\n'
			if 'ndtoplevelprimarydepartment' in j:
				sms_body += 'Department: ' + j['ndtoplevelprimarydepartment'] + '\n'
			if 'ndofficeaddress' in j:
				sms_body += 'Office: ' + j['ndofficeaddress'] + '\n'
			if 'Level' in j:
				sms_body += 'Level: ' + j['ndlevel']
			sms_body += 'Main email: ' + j['krbprincipal'].lower() + '\n'
			if 'ndcsoalias' in j:
				sms_body += 'Secondary email: ' + j['ndcsoalias'] + '@nd.edu' + '\n'
			if 'ndcsounique' in j:
				sms_body += 'Third email: ' + j['ndcsounique'] + '@nd.edu' + '\n'
			if 'postaladdress' in j:
				sms_body += 'Main Address: ' + j['postaladdress'].replace('$','\n') + '\n'
			if 'homepostaladdress' in j:
				sms_body += 'Home Address: ' + j['homepostaladdress'].replace('$','\n') + '\n'
			if 'telephonenumber' in j:
				sms_body += 'Phone number: ' + j['telephonenumber']
		except ValueError:
			sms_body += 'Could not find user with netid: ' + netid
	else:
		sms_body += 'Could not find user with netid: ' + netid
	return sms_body
