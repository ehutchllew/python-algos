def encode(st):
    new_str = ""
    for i in range(len(st)):
        c = st[i]
        encoded_char = 0
        if c == "a":
            encoded_char = "1"
        elif c == "e":
            encoded_char = "2"
        elif c == "i":
            encoded_char = "3"
        elif c == "o":
            encoded_char = "4"
        elif c == "u":
            encoded_char = "5"
        else:
            encoded_char = c
        new_str += encoded_char
    return new_str


def decode(st):
    new_str = ""
    for i in range(len(st)):
        c = st[i]
        decoded_char = ""
        if c == "1":
            decoded_char = "a"
        elif c == "2":
            decoded_char = "e"
        elif c == "3":
            decoded_char = "i"
        elif c == "4":
            decoded_char = "o"
        elif c == "5":
            decoded_char = "u"
        else:
            decoded_char = c
        new_str += decoded_char
    return new_str
