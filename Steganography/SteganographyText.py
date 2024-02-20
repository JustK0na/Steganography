import cv2 
import numpy as np 
import sys

image = "openC/Steganography/misjakleopatra"

with open("openC/Steganography/secretMessage.txt") as f:
    message = f.read()
message = str(len(message)+len(str(len(message)))+1)+"~"+message
message_bin = ''.join(format(ord(char), '08b') for char in message)
print("dlugosc ciagu:",len(message_bin)/8)

pic = cv2.imread(image+".jpg")
cv2.imwrite(image+".bmp", pic)
if pic is None:
    sys.exit("Could not read the image.")

height, width, _ = pic.shape
print(height,width ,sep="\t")


print("Start")
a=0
if len(message_bin) <= width*height:
    for i in range(int(len(message_bin)/height)+1):
        for j in range(width):
        
            r,g,b = pic[i,j]

            #print("First color: ", r,g,b, sep="\t")
            #print(a,len(message_bin), sep="\t")
            if message_bin[a] == '1':
                b = b | 1<<0
            else:
                b = b & ~(1<<0)
        
            #print("Second color", r,g,b, sep="\t")
            pic[i,j] = r,g,b

            #print("pic pixel w petli: ",pic[i,j])
            a=a+1
            if a == len(message_bin):
            #print("rowne",a,len(message_bin), sep="\t")
                break;
        else:
            continue  # only executed if the inner loop did NOT break
        break

    print("Done")
else:
    print("image to small or message to big")
#print("drugi pic pixel poza petla: ", pic[0,0])
cv2.imwrite(image+"_rev.bmp", pic)
