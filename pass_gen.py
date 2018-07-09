#random password generator
import random
password = ''
pass_len = random.randint(8, 16)
spec_char = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
alphabet_upper = []
for i in range(len(alphabet)):
    alphabet_upper.append(alphabet[i].upper())-

for j in range(pass_len):
    switch = random.randint(1, 4)
    #print (switch)
    if switch == 1:
        password += spec_char[random.randint(0, 11)] 
    elif switch == 2:
        password += alphabet[random.randint(0, 25)]
    elif switch == 3:
        password += alphabet_upper[random.randint(0, 25)]
    elif switch == 4:
        password += str(random.randint(0, 9))

print(password)