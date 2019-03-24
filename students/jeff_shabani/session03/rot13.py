#!/usr/bin/env python3

def rot13(text, delta):
    result = str()
    while (0< len(text) <=50 and
    -26< delta <26):
        for i in text:
            if ord(i) == 32:
                result += chr(32)
            elif ord(i) + delta < 97:
                result += chr(ord(i) + delta + 26)
            elif ord(i) + delta > 122:
                result += chr(ord(i) + delta -26)
            else:
                result += chr(ord(i)+delta)
        return result


if __name__ == '__main__':
    
    assert rot13("a b c", 3) == "d e f"
    assert rot13("a b c", -3) == "x y z"
    assert rot13("simple text", 16) == "iycfbu junj"
    assert rot13("important text", 10) == "swzybdkxd dohd"
    assert rot13("state secret", -13) == "fgngr frperg"
    print('Alles gute!')



