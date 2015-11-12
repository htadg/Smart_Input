from __future__ import print_function #48 57
import msvcrt, winsound

def get_input(input_type="name",length=30,action="lenient"):
	str=""
	if input_type == "name":
		while(True):
			ch = msvcrt.getch()
			if(ord(ch) == 13):
				if action == "strict":
					if len(str)==length:
						return str
					else:
						winsound.Beep(2500,1000)
				else:
					return str
			elif(ord(ch)<65 or (ord(ch)>90 and ord(ch)<97) or ord(ch)>122)and ord(ch)!=32 and ord(ch)!=8:
				winsound.Beep(2500,1000)
			elif ord(ch)==8:
				if str == "":
					winsound.Beep(2500,1000)
				else:
					print("\b \b",end="")
					str = str[:len(str)-1]
			else:
				if len(str)<length:
					print(''.join(ch),end="")
					str += ''.join(ch) 
				else:
					winsound.Beep(2500,1000)
	elif input_type == "number":
		while(True):
			ch = msvcrt.getch()
			if(ord(ch) == 13):
				if action == "strict":
					if len(str)==length:
						return str
					else:
						winsound.Beep(2500,1000)
				else:
					return str
			elif (ord(ch)<48 or ord(ch)>57) and ord(ch) != 8:
				winsound.Beep(2500,1000)
			elif ord(ch)==8:
				if str == "":
					winsound.Beep(2500,1000)
				else:
					print("\b \b",end="")
					str = str[:len(str)-1]
			else:
				if len(str)<length:
					print(''.join(ch),end="")
					str += ''.join(ch) 
				else:
					winsound.Beep(2500,1000)
	print("")
	print("")
	return str