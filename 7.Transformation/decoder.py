with open("./enc") as f:
    flag = f.read()
    
output = []

for char in flag:
    code_point = ord(char)
    char_1 = chr(code_point >> 8)
    char_2 = chr(code_point - ((code_point >> 8) << 8))
    output.append(char_1)
    output.append(char_2)

reversed_flag = "".join(output)
print(reversed_flag)
