from PIL import Image

codePatterns128 = {    " ":"11011001100",
                    "0":"10011101100",
                    "1":"10011100110",
                    "2":"11001110010",
                    "3":"11001011100",
                    "4":"11001001110",
                    "5":"11011100100",
                    "6":"11001110100",
                    "7":"11101101110",
                    "8":"11101001100",
                    "9":"11100101100",
                    "A":"10100011000",
                    "B":"10001011000",
                    "C":"10001000110",
                    "D":"10110001000",
                    "E":"10001101000",
                    "F":"10001100010",
                    "G":"11010001000",
                    "H":"11000101000",
                    "I":"11000100010",
                    "J":"10110111000",
                    "K":"10110001110",
                    "L":"10001101110",
                    "M":"10111011000",
                    "N":"10111000110",
                    "O":"10001110110",
                    "P":"11101110110",
                    "Q":"11010001110",
                    "R":"11000101110",
                    "S":"11011101000",
                    "T":"11011100010",
                    "U":"11011101110",
                    "V":"11101011000",
                    "W":"11101000110",
                    "X":"11100010110",
                    "Y":"11101101000",
                    "Z":"11101100010",
                    }

codePatternsL = ["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]
codePatternsR = ["1110010","1100110","1101100","1000010","1011100","1001110","1010000","1000100","1001000","1110100"]
quietZone = "000000000"
startZone = "101"
middleZone = "01010"
endZone = "101"

quietZone128 = "0000000000"
startCode128 = "11010010000"
stopCode128 = "1100011101011"

barCode128 = "BARCODE"
barCode = "11111111111111111"

def convertCode(code):
    codeL = code[:len(code)//2]
    codeR = code[len(code)//2:]
    res = quietZone + startZone
    for i in codeL:
        res += codePatternsL[int(i)]
    res += middleZone
    for j in codeR:
        res += codePatternsR[int(j)]
    res += endZone + quietZone
    return res

def printBarCode(code, height):
    code = convertCode(code)
    barcode = Image.new("1",(len(code),height),1)
    for y in range(height):
            for x in range(len(code)):
                barcode.putpixel((x,y),0) if code[x]=="1" else barcode.putpixel((x,y),1)
    
    barcode.show()

printBarCode(barCode,10)

def convertCode128(code):
    global quietZone128, startCode128, stopCode128
    res = quietZone128 + startCode128
    for i in code:
        res += codePatterns128[i]
    res += stopCode128 + quietZone128
    return res


def printBarCode128(code, height):
    code = convertCode128(code)
    barcode = Image.new("1",(len(code),height),1)
    for y in range(height):
            for x in range(len(code)):
                barcode.putpixel((x,y),0) if code[x]=="1" else barcode.putpixel((x,y),1)
    
    barcode.show()
    


