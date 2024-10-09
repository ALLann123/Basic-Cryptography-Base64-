#!/usr/bin/python3
import base64

def encode(key):
	key_byte=key.encode('ascii')
	key_encode=base64.b64encode(key_byte)
	encoded_string=key_encode.decode('ascii')
	print("[+]Encrypted password is: ", encoded_string)
	print()
	return

def decode(enigma):
	enigma_byte=enigma.encode('ascii')
	enigma_decode=base64.b64decode(enigma_byte)
	key_string=enigma_decode.decode('ascii')
	print("[+]The Password is>> ", key_string)
	print()
	return

print("****[+]WELCOME To PASS64 MANAGER****")
print("..........by own_the_net.........")
gameover=True
while gameover:
	pick=str(input("Do you want to decrypt or encrypt(or type exit to close)? ")).lower()

	if pick=="encrypt":
		password=str(input("Enter the Password: "))
		print(password)
		encode(password)
		add_another=input("Do you wish to add another?(y/n) ").lower()
		if add_another == "y":
			pass
		elif add_another == "n":
			print("[+]Exiting Program......Bye!!")
			gameover=False
		else:
			print("[-]Invalid input!!")

	elif pick=="decrypt":
		encrypted_key=str(input("Enter the Encrypted Password>> "))
		print(encrypted_key)
		decode(encrypted_key)
		add_another=input("Do you wish to add another?(y/n) ").lower()
		if add_another == "y":
			pass
		elif add_another == "n":
			print("[+]Exiting Program......Bye!!")
			gameover=False
		else:
			print("[-]Invalid input!!")
	elif pick=="exit":
		print("[+]Exiting Application........")
		gameover=False
	else:
		print("[-]Invalid choice!! ")
