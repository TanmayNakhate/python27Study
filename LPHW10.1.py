# Creates loading symbol
import os

while True:
    for i in ["/","- ","\\","|","/","-","\\","|"]:
        print "%s\r" % i
        os.system('cls')