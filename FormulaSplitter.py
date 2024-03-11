def split(string):
    negation = False
    if string[0] == "~":
        negation = True
    subformula1 = ""
    subformula2 = ""
    highestLevelConnective = ""

    subformula1, subformula2, highestLevelConnective = getSubformulas(string)
    
    return cleanUpSubformulas(string,subformula1,subformula2,highestLevelConnective,negation)

   
def cleanUpSubformulas(string,subformula1,subformula2,highestLevelConnective, negation):
    if(subformula1 == ""):
        if len(string) < 3:
            return string,"",""
        else:
            return "","","",""
    if (len(subformula1) > 3 and subformula1[0] != "(") and subformula1[0] != "~":
        return "","",""
    #if the first element of subFormula 1 is a round bracket then chop it off
    if(subformula1[0] == "("):
        subformula1 = subformula1[1:len(subformula1)]
        
    return subformula1, subformula2[0:len(subformula2)-1], highestLevelConnective, negation

def getSubformulas(string):
    subformula1 = ""
    subformula2 = ""
    highestLevelConnective = ""
    layer = 0
    buildSubformula1 = True
    buildsubformula2 = False
    for c in string:
        if c == "(":
            layer = layer + 1
        if c == ")":
            layer = layer - 1 
        if (c == "V" or c == "^" or c == ">") and layer == 1:
            buildsubformula2 = True
            buildSubformula1 = False
            highestLevelConnective = c
            continue
        if(buildSubformula1 and layer > 0):
            subformula1 = subformula1 + c
        if(buildsubformula2):
            subformula2 = subformula2 + c
    return subformula1, subformula2, highestLevelConnective