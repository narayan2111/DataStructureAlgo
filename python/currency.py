import argparse
parser = argparse.ArgumentParser(description='CryptoCurrency Converter')
parser.add_argument('cur', type = int, help='Enter BitCoin')
args = parser.parse_args()
def currency_converter(cur):
	print("Currencies Avaliable:\nUSD(US-Dollor)\nINR(Ruppee)\nGBP(Pound sterling)\nBRL(Brazian Real)\nCNY(Chinese Yuan\nAUD(Australian Dollor)")
	Choice=input("Enter Choice:")
	if(Choice=='GBP'):
		cur=cur*8229.14
		return cur
	elif(Choice=='CNY'):
		cur=cur*72201.74
		return cur
	elif(Choice=='BRL'):
		cur=cur*59484.46
		return cur
	elif(Choice=='AUD'):
		cur=cur*14877.41
		return cur
	elif(Choice=='INR'):
		cur=cur*25042.24
		return cur
	elif(Choice=='USD'):
		cur=cur*10629.23
		return cur
	else:
		nothing = "Currencey Not Avaliable"
		return nothing
print(currency_converter(args.cur))

