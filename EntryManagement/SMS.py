from twilio.rest import Client
from Check_in import *
from Config import *

#This function send sms to the host contains details of the visitor
def sms(vis_name,vis_num,host_num):
    # Your Account SID from twilio.com/console
    account_sid = account_Id
    # Your Auth Token from twilio.com/console
    auth_token = auth_Token

    client = Client(account_sid, auth_token)
        #print(host_num)
    message = client.messages.create(
        to= str(host_num),
        from_ = number,
        body=vis_name+ " is coming to meet you and visitor's Contact Number is " + vis_num)