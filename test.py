#!/usr/bin/python3.8

import urllib3
urllib3.disable_warnings()
import requests, bs4, re


res = requests.get('https://coinmarketcap.com/currencies/ethereum/')
res.raise_for_status()
ethSoup = bs4.BeautifulSoup(res.text, 'html.parser')
ethList = ethSoup.find_all("div", attrs={"class": "priceValue"})
ethPrice = [el.text for el in ethList]
ethString = ' '.join([str(elem) for elem in ethPrice])
ethClean = ethString.replace(',', '')
ethFloat = float(ethClean.replace('$', ''))
#print(ethFloat)

res1 = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
res1.raise_for_status()
btcSoup = bs4.BeautifulSoup(res1.text, 'html.parser')
btcList = btcSoup.find_all("div", attrs={"class": "priceValue"})
btcPrice = [el.text for el in btcList]
btcString = ' '.join([str(elem) for elem in btcPrice])
btcClean = btcString.replace(',', '')
btcFloat = float(btcClean.replace('$', ''))
#print(btcFloat)

res2 = requests.get('https://coinmarketcap.com/currencies/cardano/')
res2.raise_for_status()
adaSoup = bs4.BeautifulSoup(res2.text, 'html.parser')
adaList = adaSoup.find_all("div", attrs={"class": "priceValue"})
adaPrice = [el.text for el in adaList]
adaString = ' '.join([str(elem) for elem in adaPrice])
adaClean = adaString.replace(',', '')
adaFloat = float(adaClean.replace('$', ''))
#print(adaFloat)

res3 = requests.get('https://coinmarketcap.com/currencies/polkadot-new/')
res3.raise_for_status()
dotSoup = bs4.BeautifulSoup(res3.text, 'html.parser')
dotList = dotSoup.find_all("div", attrs={"class": "priceValue"})
dotPrice = [el.text for el in dotList]
dotString = ' '.join([str(elem) for elem in dotPrice])
dotClean = dotString.replace(',', '')
dotFloat = float(dotClean.replace('$', ''))
#print(dotFloat)

res4 = requests.get('https://coinmarketcap.com/currencies/xrp/')
res4.raise_for_status()
xrpSoup = bs4.BeautifulSoup(res4.text, 'html.parser')
xrpList = xrpSoup.find_all("div", attrs={"class": "priceValue"})
xrpPrice = [el.text for el in xrpList]
xrpString = ' '.join([str(elem) for elem in xrpPrice])
xrpClean = xrpString.replace(',', '')
xrpFloat = float(xrpClean.replace('$', ''))
#print(xrpFloat)


res5 = requests.get('https://coinmarketcap.com/currencies/chainlink/')
res5.raise_for_status()
linkSoup = bs4.BeautifulSoup(res5.text, 'html.parser')
linkList = linkSoup.find_all("div", attrs={"class": "priceValue"})
linkPrice = [el.text for el in linkList]
linkString = ' '.join([str(elem) for elem in linkPrice])
linkClean = linkString.replace(',', '')
linkFloat = float(linkClean.replace('$', ''))
#print(linkFloat)

res6 = requests.get('https://coinmarketcap.com/currencies/tron/')
res6.raise_for_status()
trxSoup = bs4.BeautifulSoup(res6.text, 'html.parser')
trxList = trxSoup.find_all("div", attrs={"class": "priceValue"})
trxPrice = [el.text for el in trxList]
trxString = ' '.join([str(elem) for elem in trxPrice])
trxClean = trxString.replace(',', '')
trxFloat = float(trxClean.replace('$', ''))
#print(trxFloat)

res7 = requests.get('https://coinmarketcap.com/currencies/iota/')
res7.raise_for_status()
iotaSoup = bs4.BeautifulSoup(res7.text, 'html.parser')
iotaList = iotaSoup.find_all("div", attrs={"class": "priceValue"})
iotaPrice = [el.text for el in iotaList]
iotaString = ' '.join([str(elem) for elem in iotaPrice])
iotaClean = iotaString.replace(',', '')
iotaFloat = float(iotaClean.replace('$', ''))
#print(iotaFloat)

res8 = requests.get('https://www.xe.com/currencycharts/?from=EUR&to=USD')
res8.raise_for_status()
usdSoup = bs4.BeautifulSoup(res8.text, 'html.parser')
usdList = usdSoup.find_all("td", attrs={"class": "table__TableCell-sc-1j0jd5l-1 cSMZNP"})
usdPrice = [el.text for el in usdList]
usdPrice = float(usdPrice[1])
#print(usdPrice)
