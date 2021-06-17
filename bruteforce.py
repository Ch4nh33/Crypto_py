def makeDisk(k):
    dec_disk = {}
    for i in range(26):
        alp = (i+k)%26 + 65
        dec_disk[chr(alp)] = chr(i+65)
            
    return dec_disk
	
def caesar(msg, key):
    ret = ''
    msg = msg.upper()
    disk = makeDisk(key)
    for c in msg:
        if c in disk:
            ret += disk[c]
        else:
            ret += c
                    
    return ret
		
def attack(msg):
    for key in range(1, 26):
        decmsg = caesar(msg, key)
        print('SHIFT[%d]: %s' %(key, decmsg))


if __name__ == '__main__':
    msg = 'UGAMKZMBSMGQAVCUJMZBPZMMNQDMWVMBPZMM'
    attack(msg)
