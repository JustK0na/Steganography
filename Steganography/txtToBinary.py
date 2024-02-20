message = "jestem mikolaj struzykowski"

message_bin = ''.join(format(ord(char), '08b') for char in message)

print(len(message_bin),message_bin, sep="\t")