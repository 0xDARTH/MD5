import colorama
from colorama import Fore, Back, Style
import os,sys,hashlib,time

print("""  
███╗   ███╗    ██████╗     ███████╗
████╗ ████║    ██╔══██╗    ██╔════╝
██╔████╔██║    ██║  ██║    ███████╗
██║╚██╔╝██║    ██║  ██║    ╚════██║
██║ ╚═╝ ██║    ██████╔╝    ███████║
╚═╝     ╚═╝    ╚═════╝     ╚══════╝
                                   
  """)

hash = input("hash md5 :")
wordlist = input("list password :")

try:
		if len(hash)!=32:
			print ("This hash is not MD")
			exit()
		if not os.path.isfile(wordlist):
			print (Fore.RED+"Error No Such File "+wordlist)
			sys.exit(2)
		loop = 1
		with open(wordlist) as wl:
			for passwd in wl:
					passwd=passwd.replace("\n","")
					final=hashlib.md5(passwd.encode()).hexdigest()
					print ("Trying this password : {}".format(passwd))
					if final==hash:
						time.sleep(3)
						#print (Fore.RED +"[+] Decryption Successfully [+]")
						print (Fore.RED+"GOOD :" +hash +' : '+ passwd)
						break
					else:
						print ("#####################################")
					loop+=1
		print (Fore.WHITE+"by @0xDARTH")
except KeyboardInterrupt as key:
		print (key)
		sys.exit(1)
except KeyError as keyer:
		print (keyer)
		sys.exit(1)
except EOFError as error:
		print (error)
		sys.exit(1)
