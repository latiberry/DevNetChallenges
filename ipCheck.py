#This program checks if input is a valid IPv4 address
#Latife Bechara-Medina 7/21/22

import ipaddress
ip = input ("Please enter an IP address to validate it. (Type x to end)\n")

while ip != 'x':

    try: 
        ipaddress.ip_address(ip)
        print("The ip address you entered {} is valid.".format(ip)) 
    except:
        print("The ip address you entered {} is NOT valid.".format(ip))

    ip = input ("Please enter an IP address to validate it. (Type x to end)\n")
    if ip == 'x':
        print("Good bye\n")
        break

