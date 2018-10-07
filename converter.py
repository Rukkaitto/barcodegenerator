from PIL import Image

codePatterns = {    " ":"11011001100",
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

quietZone = "0000000000"
startCode = "11010010000"
stopCode = "1100011101011"

barCode = "BARCODE"

def convertCode(code):
    global quietZone, startCode, stopCode
    res = quietZone + startCode
    for i in code:
        res += codePatterns[i]
    res += stopCode + quietZone
    return res


def printBarCode128(code, height):
    code = convertCode(code)
    barcode = Image.new("1",(len(code),height+20),1)
    for y in range(height):
            for x in range(len(code)):
                barcode.putpixel((x,y),0) if code[x]=="1" else barcode.putpixel((x,y),1)
    
    barcode.show()

printBarCode128(barCode,10)
