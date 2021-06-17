def makeCodebook():
	decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m',\
			'*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}
		
	encbook = {}
	for k in decbook:
		val = decbook[k]
		encbook[val] = k

	return encbook, decbook


def encrypt(msg, encbook):
	for c in msg:
		if c in encbook:
			msg = msg.replace(c, encbook[c])			
			
	return  msg


def decrypt(msg, decbook):
	for c in msg:
		if c in decbook:
			msg = msg.replace(c, decbook[c])
			
	return msg
	

if __name__ == '__main__': 
	h = open('plain.txt', 'rt')    
	content = h.read()
	h.close()

	encbook, decbook = makeCodebook()
	content = encrypt(content, encbook)

	h = open('encryption.txt', 'wt+')
	h.write(content)
	h.close()
