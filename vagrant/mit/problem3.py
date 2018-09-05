#s = 'azcbobobegghakl'

s = 'abza'
s = 'abcbcd'

subStrAlphabet = ""
startInt = 0
endInt = 0
for i in range(1,len(s)):
    print "<<<<<<<<<<<<<"
    # vars
    prevInt = i-1
    print "prevInt"
    print prevInt
    currInt = i
    print "currInt"
    print currInt
    # 
    prevChar = s[prevInt]
    prevCharOrd = ord(prevChar)
    print "prevChar"
    print prevChar
    print "prevCharOrd"
    print prevCharOrd
    #
    currChar = s[currInt]
    currCharOrd = ord(currChar)
    print "currChar"
    print currChar
    print "currCharOrd"
    print currCharOrd
    #
    prevCurrDifference = currCharOrd - prevCharOrd
    print "prevCurrDifference"
    print prevCurrDifference
    # check if in alpabet order
    if(prevCurrDifference == 1): # in alpabet order
        print "difference is 1"
        if(startInt == 0): # startInt not set
            startInt = prevInt
            print "startInt is initialized, it is: "
            print startInt
        endInt = currInt
        print "endInt is set or updated, it is"
        print endInt
    print "==============="
subStrAlphabet = s[startInt:endInt+1]

print("Longest substring in alphabetical order is: "+subStrAlphabet)