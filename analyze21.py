# import from the 21 Developer Library
import click
import json
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# set up bitrequest client for BitTransfer requests
wallet = Wallet()
requests = BitTransferRequests(wallet)

# server address
server_url = 'http://10.244.107.98:4002/'

#@click.command()
#@click.argument('text')
#def cli(text):
def buy_machine():

    input_text = input("Enter some text:\n")
    sel_url = server_url+'machine?text={0}'
    response = requests.get(url=sel_url.format(input_text))
    #response = requests.get(url=sel_url.format(text))
    #click.echo(response.text)

    print(response.text)

if __name__=='__main__':
    buy_machine()
