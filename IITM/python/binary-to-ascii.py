def binToChar(b):
  decVal = int(b, 2)
  return chr(decVal)

def add(a,b):
  return a+b

def binToSentence(binaryString):

  #Convert the binary into a list of binary strings separated by whitespace.
  binaryList=binaryString.split(' ')

  #convert each binary to character
  charMap= map(binToChar,binaryList)
  charList=list(charMap)

  #join all character
  from functools import reduce
  sentence = reduce(add,charList)
  
  return sentence


b="1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010 1101100 1100100"
binToSentence(b)
