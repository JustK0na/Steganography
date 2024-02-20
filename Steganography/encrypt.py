message_str = "138000~abcdefg"
message_bin = ''.join(format(ord(i), '08b') for i in message_str)
string = ""
char = ""

for i in range(int(len(message_bin)/8)):
    if char != "~": 
        byte = message_bin[i*8:i*8+8]
        char = chr(int(byte,2))
        string += char
        print(char)
string = string[:-1]
print(message_bin, string, sep="\n\n")