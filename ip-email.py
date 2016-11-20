# R-Pi auto email IP address
# https://www.youtube.com/watch?v=P_hpXQ8VgPI&index=12&list=PLNnwglGGYoTvy37TSGFlv-aFkpg7owWrE
from urllib.request import urlopen
import re
import smtplib 

# credentials
subject = "R-Pi IP Address"
from_address = "davidsrpicomms@gmail.com"
username = "davidsrpicomms"
to_address = "david.anthony.lei@gmail.com"
password = "myRpi&Comms"

url = "http://checkip.dyndns.com/"	# website to check public ip address

# open url, read contents and extract ip address
request = urlopen(url).read().decode('utf-8')
current_ip = re.findall("\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}", request)	# regex for ip one to three digits then period and so forth
current_ip = str(current_ip)
print("IP address: "  + current_ip)

def send_email(current_ip, to_address, from_address, subject, username):
	# body of email
	body = current_ip + " is davids-pi IP address"
	# msg is broken up lines of joint lists 
	msg = "\r\n".join(["To: %s" % to_address,
						"From: %s" % from_address,
						"Subject: %s" % subject,
						'', body])
	# send email, need smpt lib 
	# set up smpt server
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls() 	# security for transmission of credentials
	server.login(username, password)
	server.sendmail(from_address, to_address, msg)
	server.quit()
	print("Email sent to %s" % to_address)

send_email(current_ip, to_address, from_address, subject, username)



