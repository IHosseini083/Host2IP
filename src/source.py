import socket as s

hostName = input('PLease Enter host name :')

try:
        ip = s.gethostbyname(hostName)
except:
        print("Bad input. try again")

print('ip of {} is {}'.format(hostName , ip))
