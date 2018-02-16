import math
import re

status =''
S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
l = len(S)

def validate_status():
	m = input('Please Enter the mode | 0 For Encrypt / 1 for Decrypt')
	if m == '0' :
		st = 'encrypt'
	elif  m == '1' :
		st = 'decrypt'
	else :
			m = input('Invalid Value, again | Type: 0 For Encrypt / Type: 1 for Decrypt')

	return st


def caesar_cipher_enc (msg, k, l, S, status):
	msg_encypted = ''
	for c in msg :
		if c in S: # Only characters in 'S' 
			c_index = S.index(c); # Character's index

			if status == 'encrypt':
				c_enc_index = (c_index + int(k) )% l
			else : 
				c_enc_index = (c_index - int(k) )% l

			msg_encypted += S[c_enc_index]
		else :
			msg_encypted += c 

	print(msg_encypted)
	print('Done')
	return msg_encypted

def Main():

	msg = input('Please Enter your Message :')
	key = input('Please Enter your Key :')
	status = validate_status()
	print('Mode : ', status)
	print('\n')
	print('the message is : ', msg)
	print('\n')
	print('The Key is : ', key )
	print('\n')
	print('Processing now ...' )
	res = caesar_cipher_enc(msg, key, l, S, status)
	print(res)
if __name__ == '__main__':
 	Main()