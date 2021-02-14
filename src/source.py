import socket as s

hostName = input('PLease Enter name host:')

try:
        ip = s.gethostbyname(hostName)
except:
        print("try bad input ''' ")

print('ip of {} is {}'.format(hostName , ip))