import socket
import sys
from datetime import datetime
import time

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])

else:
        print("Invalid amout of arguments")
        print("Please in that format \"scan1.py <IP>\"")

#Banner
print("*" * 20)
print("Scanning the host " + target + ".")
print("Ping start " + str(datetime.now()) + ".")
print("*" * 20)

def connect():
        for port in range(3000, 3335):
                socket.setdefaulttimeout(0.1)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((target,port))
                if result == 0:
                        print("Port " + str(port) + " is open!".format(port))

#Port Scan
try:
	connect()

#Exit
except KeyboardInterrupt:
        print("\nKeyboard endet")
        sys.exit()

except socket.gaierror:
        print("Hostneme not valid")
        sys.exit()

except socket.error:
        print("could not connect at all")
        sys.exit()

print("\n" * 2)
print("`" * 20)
print("Scan endet at" + str(datetime.now()))
