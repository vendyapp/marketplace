from flask import Flask
from flask import request, redirect, url_for
from flask.ext.cors import CORS

from mastercardapicore import RequestMap, Config, OAuthAuthentication
from os.path import dirname, realpath, join
from mastercardp2p import PaymentTransfer, Consumer
import os 

app = Flask(__name__)

@app.route("/")
def connect():
	return "hello"

@app.route("/transfer")
def makeTransfer():
    consumerKey = "4FZDE2qryKsPPqA1NwXbbBku3bNHhHZrpZLowyMP6b729703!f435de5c8fe3425aacf9d3b1912611ca0000000000000000"
    keyStorePath = "hackathonalias_sandbox.p12" # e.g. /Users/yourname/project/sandbox.p12 | C:\Users\yourname\project\sandbox.p12
    keyAlias = "hackathonalias"   # For production: change this to the key alias you chose when you created your production key
    keyPassword = "hackathon@123"   # For production: change this to the key alias you chose when you created your production key

    auth = OAuthAuthentication(consumerKey, keyStorePath, keyAlias, keyPassword)
    Config.setAuthentication(auth)
    Config.setSandbox(True)   # For production: use Config.setSandbox(false)

    mapObj = RequestMap()
    mapObj.set("payment_transfer.transfer_reference", "12346991848254111813006")
    mapObj.set("payment_transfer.payment_type", "P2P")
    mapObj.set("payment_transfer.funding_source[0]", "CREDIT")
    mapObj.set("payment_transfer.funding_source[1]", "DEBIT")
    mapObj.set("payment_transfer.amount", "1800")
    mapObj.set("payment_transfer.currency", "USD")
    mapObj.set("payment_transfer.sender_account_uri", "pan:5013040000000018;exp=2017-08;cvc=123")
    mapObj.set("payment_transfer.sender.first_name", "John")
    mapObj.set("payment_transfer.sender.middle_name", "Tyler")
    mapObj.set("payment_transfer.sender.last_name", "Jones")
    mapObj.set("payment_transfer.sender.nationality", "USA")
    mapObj.set("payment_transfer.sender.date_of_birth", "1994-05-21")
    mapObj.set("payment_transfer.sender.address.line1", "21 Broadway")
    mapObj.set("payment_transfer.sender.address.line2", "Apartment A-6")
    mapObj.set("payment_transfer.sender.address.city", "OFallon")
    mapObj.set("payment_transfer.sender.address.country_subdivision", "MO")
    mapObj.set("payment_transfer.sender.address.postal_code", "63368")
    mapObj.set("payment_transfer.sender.address.country", "USA")
    mapObj.set("payment_transfer.sender.phone", "11234565555")
    mapObj.set("payment_transfer.sender.email", "John.Jones123@abcmail.com")
    mapObj.set("payment_transfer.recipient_account_uri", "pan:5013040000000018;exp=2017-08;cvc=123")
    mapObj.set("payment_transfer.recipient.first_name", "Jane")
    mapObj.set("payment_transfer.recipient.middle_name", "Tyler")
    mapObj.set("payment_transfer.recipient.last_name", "Smith")
    mapObj.set("payment_transfer.recipient.nationality", "USA")
    mapObj.set("payment_transfer.recipient.date_of_birth", "1999-12-30")
    mapObj.set("payment_transfer.recipient.address.line1", "1 Main St")
    mapObj.set("payment_transfer.recipient.address.line2", "Apartment 9")
    mapObj.set("payment_transfer.recipient.address.city", "OFallon")
    mapObj.set("payment_transfer.recipient.address.country_subdivision", "MO")
    mapObj.set("payment_transfer.recipient.address.postal_code", "63368")
    mapObj.set("payment_transfer.recipient.address.country", "USA")
    mapObj.set("payment_transfer.recipient.phone", "11234567890")
    mapObj.set("payment_transfer.recipient.email", "Jane.Smith123@abcmail.com")
    mapObj.set("payment_transfer.payment_origination_country", "USA")
    mapObj.set("payment_transfer.sanction_screening_override", " false ")
    mapObj.set("payment_transfer.statement_descriptor", "P2P*THANKYOU")
    mapObj.set("payment_transfer.channel", "KIOSK")
    mapObj.set("payment_transfer.text", "funding_source")
    mapObj.set("partnerId", "ptnr_2370-10D6-ED32-C98E")
    
    response = PaymentTransfer.create(mapObj)
    print("transfer.id--> %s") % response.get("transfer.id") #transfer.id-->trn_4MMUC7147Vamd1IVt77DV0d-mIZr
    print("transfer.resource_type--> %s") % response.get("transfer.resource_type") #transfer.resource_type-->transfer
    print("transfer.transfer_reference--> %s") % response.get("transfer.transfer_reference") #transfer.transfer_reference-->40023991848254111813006
    print("transfer.payment_type--> %s") % response.get("transfer.payment_type") #transfer.payment_type-->P2P
    print("transfer.sender_account_uri--> %s") % response.get("transfer.sender_account_uri") #transfer.sender_account_uri-->acct-ref:ref_20160407070850915
    print("transfer.sender.first_name--> %s") % response.get("transfer.sender.first_name") #transfer.sender.first_name-->John
    print("transfer.sender.middle_name--> %s") % response.get("transfer.sender.middle_name") #transfer.sender.middle_name-->Tyler
    print("transfer.sender.last_name--> %s") % response.get("transfer.sender.last_name") #transfer.sender.last_name-->Jones
    print("transfer.sender.nationality--> %s") % response.get("transfer.sender.nationality") #transfer.sender.nationality-->USA
    print("transfer.sender.date_of_birth--> %s") % response.get("transfer.sender.date_of_birth") #transfer.sender.date_of_birth-->1994-05-21
    print("transfer.sender.address.line1--> %s") % response.get("transfer.sender.address.line1") #transfer.sender.address.line1-->21 Broadway
    print("transfer.sender.address.line2--> %s") % response.get("transfer.sender.address.line2") #transfer.sender.address.line2-->Apartment A-6
    print("transfer.sender.address.city--> %s") % response.get("transfer.sender.address.city") #transfer.sender.address.city-->OFallon
    print("transfer.sender.address.country_subdivision--> %s") % response.get("transfer.sender.address.country_subdivision") #transfer.sender.address.country_subdivision-->MO
    print("transfer.sender.address.postal_code--> %s") % response.get("transfer.sender.address.postal_code") #transfer.sender.address.postal_code-->63368
    print("transfer.sender.address.country--> %s") % response.get("transfer.sender.address.country") #transfer.sender.address.country-->USA
    print("transfer.sender.phone--> %s") % response.get("transfer.sender.phone") #transfer.sender.phone-->11234565555
    print("transfer.sender.email--> %s") % response.get("transfer.sender.email") #transfer.sender.email-->John.Jones123@abcmail.com
    print("transfer.recipient_account_uri--> %s") % response.get("transfer.recipient_account_uri") #transfer.recipient_account_uri-->pan:************0018
    print("transfer.recipient.first_name--> %s") % response.get("transfer.recipient.first_name") #transfer.recipient.first_name-->Jane
    print("transfer.recipient.middle_name--> %s") % response.get("transfer.recipient.middle_name") #transfer.recipient.middle_name-->Tyler
    print("transfer.recipient.last_name--> %s") % response.get("transfer.recipient.last_name") #transfer.recipient.last_name-->Smith
    print("transfer.recipient.nationality--> %s") % response.get("transfer.recipient.nationality") #transfer.recipient.nationality-->USA
    print("transfer.recipient.date_of_birth--> %s") % response.get("transfer.recipient.date_of_birth") #transfer.recipient.date_of_birth-->1999-12-30
    print("transfer.recipient.address.line1--> %s") % response.get("transfer.recipient.address.line1") #transfer.recipient.address.line1-->1 Main St
    print("transfer.recipient.address.line2--> %s") % response.get("transfer.recipient.address.line2") #transfer.recipient.address.line2-->Apartment 9
    print("transfer.recipient.address.city--> %s") % response.get("transfer.recipient.address.city") #transfer.recipient.address.city-->OFallon
    print("transfer.recipient.address.country_subdivision--> %s") % response.get("transfer.recipient.address.country_subdivision") #transfer.recipient.address.country_subdivision-->MO
    print("transfer.recipient.address.postal_code--> %s") % response.get("transfer.recipient.address.postal_code") #transfer.recipient.address.postal_code-->63368
    print("transfer.recipient.address.country--> %s") % response.get("transfer.recipient.address.country") #transfer.recipient.address.country-->USA
    print("transfer.recipient.phone--> %s") % response.get("transfer.recipient.phone") #transfer.recipient.phone-->11234567890
    print("transfer.recipient.email--> %s") % response.get("transfer.recipient.email") #transfer.recipient.email-->Jane.Smith123@abcmail.com
    print("transfer.transfer_amount.value--> %s") % response.get("transfer.transfer_amount.value") #transfer.transfer_amount.value-->1800
    print("transfer.transfer_amount.currency--> %s") % response.get("transfer.transfer_amount.currency") #transfer.transfer_amount.currency-->USD
    print("transfer.created--> %s") % response.get("transfer.created") #transfer.created-->2016-08-29T01:11:02-05:00
    print("transfer.transaction_history.resource_type--> %s") % response.get("transfer.transaction_history.resource_type") #transfer.transaction_history.resource_type-->list
    print("transfer.transaction_history.item_count--> %s") % response.get("transfer.transaction_history.item_count") #transfer.transaction_history.item_count-->1
    print("transfer.transaction_history.data.transaction.id--> %s") % response.get("transfer.transaction_history.data.transaction.id") #transfer.transaction_history.data.transaction.id-->txn_S7hjCOKzzkSzeCTS7g-Fdq0_drCD
    print("transfer.transaction_history.data.transaction.resource_type--> %s") % response.get("transfer.transaction_history.data.transaction.resource_type") #transfer.transaction_history.data.transaction.resource_type-->transaction
    print("transfer.transaction_history.data.transaction.account_uri--> %s") % response.get("transfer.transaction_history.data.transaction.account_uri") #transfer.transaction_history.data.transaction.account_uri-->pan:************0018
    print("transfer.transaction_history.data.transaction.transaction_amount.value--> %s") % response.get("transfer.transaction_history.data.transaction.transaction_amount.value") #transfer.transaction_history.data.transaction.transaction_amount.value-->1800
    print("transfer.transaction_history.data.transaction.transaction_amount.currency--> %s") % response.get("transfer.transaction_history.data.transaction.transaction_amount.currency") #transfer.transaction_history.data.transaction.transaction_amount.currency-->USD
    print("transfer.transaction_history.data.transaction.network--> %s") % response.get("transfer.transaction_history.data.transaction.network") #transfer.transaction_history.data.transaction.network-->STAR
    print("transfer.transaction_history.data.transaction.funds_availability--> %s") % response.get("transfer.transaction_history.data.transaction.funds_availability") #transfer.transaction_history.data.transaction.funds_availability-->IMMEDIATE
    print("transfer.transaction_history.data.transaction.type--> %s") % response.get("transfer.transaction_history.data.transaction.type") #transfer.transaction_history.data.transaction.type-->PAYMENT
    print("transfer.transaction_history.data.transaction.create_timestamp--> %s") % response.get("transfer.transaction_history.data.transaction.create_timestamp") #transfer.transaction_history.data.transaction.create_timestamp-->2016-08-29T01:11:02-05:00
    print("transfer.transaction_history.data.transaction.status--> %s") % response.get("transfer.transaction_history.data.transaction.status") #transfer.transaction_history.data.transaction.status-->APPROVED
    print("transfer.transaction_history.data.transaction.status_reason--> %s") % response.get("transfer.transaction_history.data.transaction.status_reason") #transfer.transaction_history.data.transaction.status_reason-->APPROVED
    print("transfer.transaction_history.data.transaction.status_timestamp--> %s") % response.get("transfer.transaction_history.data.transaction.status_timestamp") #transfer.transaction_history.data.transaction.status_timestamp-->2016-08-29T01:11:02-05:00
    print("transfer.transaction_history.data.transaction.retrieval_reference--> %s") % response.get("transfer.transaction_history.data.transaction.retrieval_reference") #transfer.transaction_history.data.transaction.retrieval_reference-->624200192616
    print("transfer.transaction_history.data.transaction.system_trace_audit_number--> %s") % response.get("transfer.transaction_history.data.transaction.system_trace_audit_number") #transfer.transaction_history.data.transaction.system_trace_audit_number-->926162
    print("transfer.reconciliation_data.custom_field[0].name--> %s") % response.get("transfer.reconciliation_data.custom_field[0].name") #transfer.reconciliation_data.custom_field[0].name-->ABC
    print("transfer.reconciliation_data.custom_field[0].value--> %s") % response.get("transfer.reconciliation_data.custom_field[0].value") #transfer.reconciliation_data.custom_field[0].value-->123
    print("transfer.reconciliation_data.custom_field[1].name--> %s") % response.get("transfer.reconciliation_data.custom_field[1].name") #transfer.reconciliation_data.custom_field[1].name-->DEF
    print("transfer.reconciliation_data.custom_field[1].value--> %s") % response.get("transfer.reconciliation_data.custom_field[1].value") #transfer.reconciliation_data.custom_field[1].value-->456
    print("transfer.reconciliation_data.custom_field[2].name--> %s") % response.get("transfer.reconciliation_data.custom_field[2].name") #transfer.reconciliation_data.custom_field[2].name-->GHI
    print("transfer.reconciliation_data.custom_field[2].value--> %s") % response.get("transfer.reconciliation_data.custom_field[2].value") #transfer.reconciliation_data.custom_field[2].value-->789
    print("transfer.statement_descriptor--> %s") % response.get("transfer.statement_descriptor") #transfer.statement_descriptor-->TST*THANKYOU
    print("transfer.channel--> %s") % response.get("transfer.channel") #transfer.channel-->KIOSK
    print("transfer.status--> %s") % response.get("transfer.status") #transfer.status-->APPROVED
    print("transfer.status_timestamp--> %s") % response.get("transfer.status_timestamp") #transfer.status_timestamp-->2016-08-29T01:11:02-05:00
        

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5555, debug = True, threaded=True)