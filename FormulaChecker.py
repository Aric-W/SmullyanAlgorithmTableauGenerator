def wellFormed(string):
    return noUselessParen(string) and matchingParen(string) and patternChecker(string) 

def patternChecker(string):
    validPatterns = ["~(", "~a","~b","~c","~d","~e","~f","~g","~h","~i","~j","~k","~l","~m","~n","~o","~p","~q","~r","~s","~t","~u","~v","~w","~x","~y","~z"
                 ,"(~","|~","&~",">~","(a","(b","(c","(d","(e","(f","(g","(h","(i","(j","(k","(l","(m","(n","(o","(p","(q","(r","(s","(t","(u","(v",
                 "(w","(x","(y","(z",">(","|(","&(","a>","b>","c>","d>","e>","f>","g>","h>","i>","j>","k>","l>","m>","n>","o>","p>",
                 "q>","r>","s>","t>","u>","v>","w>","x>","y>","z>","a|","b|","c|","d|","e|","f|","g|","h|","i|","j|","k|","l|","m|",
                 "n|","o|","p|","q|","r|","s|","t|","u|","v|","w|","x|","y|","z|","|a","|b","|c","|d","|e","|f","|g","|h","|i","|j",
                 "|k","|l","|m","|n","|o","|p","|q","|r","|s","|t","|u","|v","|w","|x","|y","|z","a&","b&","c&","d&","e&","f&","g&",
                 "h&","i&","j&","k&","l&","m&","n&","o&","p&","q&","r&","s&","t&","u&","v&","w&","x&","y&","z&","&a","&b","&c","&d",
                 "&e","&f","&g","&h","&i","&j","&k","&l","&m","&n","&o","&p","&q","&r","&s","&t","&u","&v","&w","&x","&y","&z",
                 ">a",">b",">c",">d",">e",">f",">g",">h",">i",">j",">k",">l",">m",">n",">o",">p",">q",">r",">s",">t",">u",">v",">w",
                 ">x",">y",">z","&~","|~","))","((","a)","b)","c)","d)","e)","f)","g)","h)","i)","j)","k)","l)","m)","n)","o)","p)",
                 "q)","r)","s)","t)","u)","v)","w)","x)","y)","z)",")|",")&",")>","~("]
    validFacts = ["~a","~b","~c","~d","~e","~f","~g","~h","~i","~j","~k","~l","~m","~n","~o","~p","~q","~r","~s","~t","~u","~v","~w","~x","~y","~z",
                  "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    if len(string) == 1 or len(string) == 2:
        for c in validFacts:
            if string == c:
                return True
        
            
    prev = ''
    pairs = []
    for c in string:
        pair = ''
        for i in range(0,1):
            pair = prev + c
        if(len(pair) == 2):
            pairs.append(pair)
        prev = c
    

    valid = True
    if(len(pairs) < 2):
        return False
    j = 0
    for p in pairs:
        j = 0
        for i in validPatterns:
            if p == i:
                break
            
            if(j == len(validPatterns)-1):
                valid = False
                break
            j = j + 1
        
    return valid

def matchingParen(strin):
    leftParenCounter = 0
    rightParenCounter = 0
    for c in strin:
        if(ord(c) == 40):
            leftParenCounter = leftParenCounter + 1
        elif(ord(c) == 41):
            rightParenCounter = rightParenCounter + 1
        if(rightParenCounter > leftParenCounter):
            return False
    return leftParenCounter == rightParenCounter

def noUselessParen(string):
    hotConnective = False
    leftParenCounter = 0
    rightParenCounter = 0
    connectiveCounter = 0

    for c in string:
        if (c == "("):
            leftParenCounter = leftParenCounter + 1
            hotConnective = False
        elif(c == ")"):
            rightParenCounter = rightParenCounter + 1
            hotConnective = False
        elif(c == "&" or c == "|" or c == ">"):
            connectiveCounter = connectiveCounter + 1
            hotConnective = True
            continue
        if((c == "&" or c == "|" or c == ">") and hotConnective):
            return False
        else:
            continue

    return leftParenCounter == connectiveCounter and rightParenCounter == connectiveCounter
