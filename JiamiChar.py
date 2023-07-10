import base64
import re

Getascii = re.compile(r"\d+")


def Jiami(charstr):
    firstData = str(list(map(ord, charstr)))
    secondData = base64.b64encode(firstData.encode())
    return secondData


def Jiemi(charstr):
    firstData = base64.b64decode(charstr).decode()
    secondData_1 = Getascii.findall(firstData)
    endCharStr = ''
    for i in secondData_1:
        endCharStr = endCharStr + chr(int(i))
    return endCharStr



