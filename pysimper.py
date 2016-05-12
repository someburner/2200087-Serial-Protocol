import serial, argparse, sys


def getArrFromStr(serialData):
    output = []
    inputList = serialData.split(" ")
    for value in inputList:
        binStr = bin(int(value, base=16))[2:]
        for i in range(8 - len(binStr)):
            binStr = '0' + binStr
        output.append(binStr)
    return output


def processDigit(digitNumber, binArray):
    decimalPointBool = False
    digitValue = -1
    bin = []
    if digitNumber == 4:
        bin.append(binArray[2][::-1])
        bin.append(binArray[3][::-1])
    if digitNumber == 3:
        bin.append(binArray[4][::-1])
        bin.append(binArray[5][::-1])
    if digitNumber == 2:
        bin.append(binArray[6][::-1])
        bin.append(binArray[7][::-1])
    if digitNumber == 1:
        bin.append(binArray[8][::-1])
        bin.append(binArray[9][::-1])

    print ('working with bin')
    print (bin)
    digitDict = {}
    digitDict['A'] = int(bin[0][0])
    digitDict['F'] = int(bin[0][1])
    digitDict['E'] = int(bin[0][2])
    digitDict['B'] = int(bin[1][0])
    digitDict['G'] = int(bin[1][1])
    digitDict['C'] = int(bin[1][2])
    digitDict['D'] = int(bin[1][3])
    digitValue = getCharFromDigitDict(digitDict)

    decimalPointBool = bool(int(bin[0][3]))

    if digitNumber == 4:
        decimalPointBool = False

    print('decimalPointBool:%d digitValue: %d', decimalPointBool, digitValue)
    return (decimalPointBool, digitValue)



def getCharFromDigitDict(digitDict):

    return  9  if is9(digitDict) else  8  if is8(digitDict) \
      else  7  if is7(digitDict) else  6  if is6(digitDict) \
      else  5  if is5(digitDict) else  4  if is4(digitDict) \
      else  3  if is3(digitDict) else  2  if is2(digitDict) \
      else  1  if is1(digitDict) else  0  if is0(digitDict) \
      else 'C' if isC(digitDict) else 'F' if is4(digitDict) \
      else 'E' if isE(digitDict) else 'P' if isP(digitDict) \
      else 'N' if isN(digitDict) else 'L' 



def isE(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 1 and \
       digitDict['G'] == 1 and digitDict['B'] == 0 and \
       digitDict['C'] == 0 and digitDict['D'] == 1 and digitDict['E'] == 1:
        return True
    return False


def isN(digitDict):
    if digitDict['A'] == 0 and digitDict['F'] == 0 and \
       digitDict['G'] == 1 and digitDict['B'] == 0 and \
       digitDict['C'] == 1 and digitDict['D'] == 0 and digitDict['E'] == 1:
        return True
    return False


def isL(digitDict):
    if digitDict['A'] == 0 and digitDict['F'] == 1 and \
       digitDict['G'] == 0 and digitDict['B'] == 0 and \
       digitDict['C'] == 0 and digitDict['D'] == 1 and digitDict['E'] == 1:
        return True
    return False


def isP(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 1 and \
       digitDict['G'] == 1 and digitDict['B'] == 1 and \
       digitDict['C'] == 0 and digitDict['D'] == 0 and digitDict['E'] == 1:
        return True
    return False


def isF(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 1 and \
       digitDict['G'] == 1 and digitDict['B'] == 0 and \
       digitDict['C'] == 0 and digitDict['D'] == 0 and digitDict['E'] == 1:
        return True
    return False


def isC(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 1 and \
       digitDict['G'] == 0 and digitDict['B'] == 0 and \
       digitDict['C'] == 0 and digitDict['D'] == 1 and digitDict['E'] == 1:
        return True
    return False


def is9(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 1 and \
       digitDict['G'] == 1 and digitDict['B'] == 1 and \
       digitDict['C'] == 1 and digitDict['D'] == 1 and digitDict['E'] == 0:
        return True
    return False


def is8(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 1 and \
       digitDict['G'] == 1 and digitDict['B'] == 1 and \
       digitDict['C'] == 1 and digitDict['D'] == 1 and digitDict['E'] == 1:
        return True
    return False


def is7(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 0 and \
       digitDict['G'] == 0 and digitDict['B'] == 1 and \
       digitDict['C'] == 1 and digitDict['D'] == 0 and digitDict['E'] == 0:
        return True
    return False


def is6(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 1 and \
       digitDict['G'] == 1 and digitDict['B'] == 0 and \
       digitDict['C'] == 1 and digitDict['D'] == 1 and digitDict['E'] == 1:
        return True
    return False


def is5(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 1 and \
       digitDict['G'] == 1 and digitDict['B'] == 0 and \
       digitDict['C'] == 1 and digitDict['D'] == 1 and digitDict['E'] == 0:
        return True
    return False


def is4(digitDict):
    if digitDict['A'] == 0 and digitDict['F'] == 1 and \
       digitDict['G'] == 1 and digitDict['B'] == 1 and \
       digitDict['C'] == 1 and digitDict['D'] == 0 and digitDict['E'] == 0:
        return True
    return False


def is3(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 0 and \
       digitDict['G'] == 1 and digitDict['B'] == 1 and \
       digitDict['C'] == 1 and digitDict['D'] == 1 and digitDict['E'] == 0:
        return True
    return False


def is2(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 0 and \
       digitDict['G'] == 1 and digitDict['B'] == 1 and \
       digitDict['C'] == 0 and digitDict['D'] == 1 and digitDict['E'] == 1:
        return True
    return False


def is1(digitDict):
    if digitDict['A'] == 0 and digitDict['F'] == 0 and \
       digitDict['G'] == 0 and digitDict['B'] == 1 and \
       digitDict['C'] == 1 and digitDict['D'] == 0 and digitDict['E'] == 0:
        return True
    return False


def is0(digitDict):
    if digitDict['A'] == 1 and digitDict['F'] == 1 and \
       digitDict['G'] == 0 and digitDict['B'] == 1 and \
       digitDict['C'] == 1 and digitDict['D'] == 1 and digitDict['E'] == 1:
        return True
    return False

global debug
debug = False

def strToFlags(strOfBytes):
    flags = []
    binArray = getArrFromStr(strOfBytes)
    if debug: print('strToFlags. strOfBytes: {0}\n binarray: {1}', strOfBytes, binArray)
    for index, binStr in enumerate(binArray): binArray[index] = binStr[::-1]
    flagopts = [['AUTO', 0, 0],         ['CONTINUITY',1,3],   ['DIODE', 1, 2],      
                ['LOW BATTERY', 1, 1],  ['HOLD', 1, 0],       ['MIN', 10, 0],       
                ['REL DELTA', 10, 1],   ['HFE', 10, 2],       ['Percent', 10, 3],
                ['SECONDS', 11, 0],     ['dBm', 11, 1],       ['n (1e-9)', 11, 2], 
                ['u (1e-6)', 11, 3],    ['m (1e-3)', 12, 0],  ['VOLTS', 12, 1],
                ['AMPS', 12, 2],        ['FARADS', 12, 3],    ['M (1e6)', 13, 0],
                ['K (1e3)', 13, 1],     ['OHMS', 13, 2],      ['Hz', 13, 3], ['AC', 0, 2]]

    for flag in flagopts: 
      if binArray[flag[1]][flag[2]] == '1': flags.append(flag[0])

    return flags


def strToDigits(strOfBytes):
    binArray = getArrFromStr(strOfBytes)
    digits = ""
    for number in reversed(range(1, 5)):
        out = processDigit(number, binArray)
        if out[1] == -1:
            print("Protocol Error: Please start an issue here: \
                https://github.com/ddworken/2200087-Serial-Protocol/issues \
                and include the following data: '" + strOfBytes + "'")
            sys.exit(1)
        if out[0]:
            digits += "."
        digits += str(out[1])
    minusBool = bool(int(binArray[0][::-1][3]))
    if minusBool:
        digits = '-' + digits
    return digits
