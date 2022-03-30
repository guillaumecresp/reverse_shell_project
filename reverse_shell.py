import getpass
import os
from socket import socket

s = socket()
s.bind(("10.106.0.69", 4444))
s.listen(2)
client, adr = s.accept()
print("client connecté")

username = client.recv(1024).decode()
password = client.recv(1024).decode()

print("Username: {}".format(username))
print("Password: {}".format(password))
print("IP: {}".format(adr))