#ord returns the decimal value of a char input
def picoRe(flag):
    newText = ""
    for i in range(0, len(flag)):
        newText += chr((ord(flag[i]) >> 8)) + (chr((ord(flag[i])) - ((ord(flag[i])>>8)<<8)))

    return newText

print(picoRe("灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"))