def encode(message, key):
    ret = ""
    for i in range(len(message)):
        number = ord(message[i])
        letter = chr(number + key)
        ret += letter
    return ret


def encode_better(phrase, key_phrase, file_name):
    ret = " "
    for i in range(len(phrase)):
        character = ord(phrase[i]) - 65
        letter = ord(key_phrase[i % len(key_phrase)]) - 65
        cipher_val = ((character + letter) % 58) + 65
        cipher_text = chr(cipher_val)
        ret += cipher_text
    file = open(file_name, "a")
    file.write(ret)
