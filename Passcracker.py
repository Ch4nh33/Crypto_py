import ccrypt512 as crypt

def findPass(passhash, dictfile):	
    salt = passhash[3:11]
    with open(dictfile, 'r') as dfile:	
        for word in dfile.readlines():
            word = word.strip('\n')
            cryptwd = crypt.sha512_crypt(word, salt)                        
            if cryptwd == passhash:
                return word
    return ''
	
def main():	
    dictfile = 'dictionary.txt'
    with open('passwords.txt', 'r') as passFile:
        for line in passFile.readlines():
            data = line.split(':')
            user = data[0].strip()
            passwd = data[1].strip()
            word = findPass(passwd, dictfile)
            if word:
                print('FOUND Password: ID [%s] Password [%s]' %(user, word))
            else:
                print('Password Not Found!')
		
main()


#salt = 'E3KoH6yW'
#passwd = '12345'
#ret = crypt.sha512_crypt(passwd, salt)
#print(ret)
