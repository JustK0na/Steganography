import cv2 
import numpy as np 
import sys


image = sys.argv[1];
#image = "Steganography\hasloXboxMinecraft_rev.bmp"

#file = open("Steganography\\recivedMessage.txt", "w")
mess_len = 302500

pic = cv2.imread(image)
if pic is None:
    sys.exit("Could not read the image.")


string = ""
char = ""
a=0
while True:
    byte = ""
    for i in range(8): 
        _,_,color = pic[0,8*a+i]
        #print("color: ", color,type(color),sep="\t")
        bit = bin(color)[-1]
        #print("bit: ", bit, type(bit), sep="\t")
        byte = byte + bin(int(bit))[-1]
        #print("byte: ",byte)
    char = chr(int(byte,2))
    string += char
    #print("\n\nchar: ",char)
    #print("\n\nstring: ", string)
    a+=1
    if char == "~":
        break
    

string = string[:-1]
#print(string, sep="\n\n")


height, width, _ = pic.shape
mess_bin = []
mess_len = int(string)*8

for i in range(int(mess_len/height)+1):
    if i >= height:
        break

    if mess_len > width:
        for j in range(width):
            _,_,bit = pic[i,j]
            mess_bin.append(bin(bit)[-1])
    else:
        for j in range(mess_len):
            _,_,bit = pic[i,j]
            mess_bin.append(bin(bit)[-1])

mess_bin = "".join(mess_bin)

mess_txt = []
for i in range(1,int(mess_len/8)+1):
    mess_txt.append(chr(int(mess_bin[(i-1)*8:i*8],2)))

mess_txt = "".join(mess_txt)
#mess_txt = mess_txt[len(string+"~"):]

#file.write(mess_txt)
print("message decrypted: \t")
print(mess_txt)

#file.close()