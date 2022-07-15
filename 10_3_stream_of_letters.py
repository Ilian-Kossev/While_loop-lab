data = input()
counter_command = 0
counter_c = 0
counter_o = 0
counter_n = 0
letter = ""
word = ""
while data != "End":
    symbol = ord(data)
    if 65 <= symbol <= 90 or 97 <= symbol < 99 or 99 < symbol < 110 or 111 < symbol <= 122:
        letter = chr(symbol)
    if symbol == 99:
        counter_c += 1
        if counter_c > 1:
            letter = chr(symbol)
        else:
            letter = ""
            counter_command += 1
    elif symbol == 111:
        counter_o += 1
        if counter_o > 1:
            letter = chr(symbol)
        else:
            letter = ""
            counter_command += 1
    elif symbol == 110:
        counter_n += 1
        if counter_n > 1:
            letter = chr(symbol)
        else:
            letter = ""
            counter_command += 1
    word += letter
    if counter_command == 3:
        print(word + " ", end="")
        word = ""
        counter_command = 0
        counter_c = 0
        counter_o = 0
        counter_n = 0
    letter = ""
    data = input()
