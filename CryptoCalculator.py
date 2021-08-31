#!/usr/bin/python3.8
import urllib3
urllib3.disable_warnings()
import requests, bs4, re
from test import *

x = str(input("Is the input value in EUR or Crypto?: "))

if x == "EUR":
    y = float(input("Insert the amount in EUR: "))
    y1 = str(input("To what cryptocurrency will you be converting (BTC, ETH, XRP, ADA, DOT, TRX, IOTA, LINK)?: "))
    if y1 == "BTC":
        total = (y*usdPrice)/btcFloat
        print("This is equal to {} BTC".format(total))
    elif y1 == "ETH":
        total = (y*usdPrice)/ethFloat
        print("This is equal to {} ETH".format(total))
    elif y1 == "XRP":
        total = (y*usdPrice) / xrpFloat
        print("This is equal to {} XRP".format(total))
    elif y1 == "ADA":
        total = (y*usdPrice) / adaFloat
        print("This is equal to {} ADA".format(total))
    elif y1 == "DOT":
        total = (y*usdPrice) / dotFloat
        print("This is equal to {} DOT".format(total))
    elif y1 == "TRX":
        total = (y*usdPrice) / trxFloat
        print("This is equal to {} TRX".format(total))
    elif y1 == "IOTA":
        total = (y*usdPrice) / iotaFloat
        print("This is equal to {} IOTA".format(total))
    elif y1 == "LINK":
        total = (y*usdPrice) / linkFloat
        print("This is equal to {} LINK".format(total))

elif x == "Crypto":
    y1 = str(input("What cryptocurrency do you have (BTC, ETH, XRP, ADA, DOT, TRX, IOTA, LINK)?: "))
    y = float(input("Insert the amount of tokens you have: "))
    if y1 == "BTC":
        total = (y*btcFloat)/usdPrice
        print("You have {} EUR".format(total))
    elif y1 =="ETH":
        total = (y*ethFloat)/usdPrice
        print("You have {} EUR".format(total))
    elif y1 =="XRP":
        total = (y*xrpFloat)/usdPrice
        print("You have {} EUR".format(total))
    elif y1 =="ADA":
        total = (y*adaFloat)/usdPrice
        print("You have {} EUR".format(total))
    elif y1 =="DOT":
        total = (y*dotFloat)/usdPrice
        print("You have {} EUR".format(total))
    elif y1 =="TRX":
        total = (y*trxFloat)/usdPrice
        print("You have {} EUR".format(total))
    elif y1 =="IOTA":
        total = (y*iotaFloat)/usdPrice
        print("You have {} EUR".format(total))
    elif y1 =="LINK":
        total = (y*linkFloat)/usdPrice
        print("You have {} EUR".format(total))

close = str(input("Hit enter to close!"))