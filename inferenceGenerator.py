from FormulaSplitter import split
def inGen(formula):
    subForm1, subForm2,connective, negated = split(formula)
    isItAlpha = True
    if(negated):
        if connective == "|":
            if subForm1[0] == "~":
                inference1 = subForm1[1:len(subForm1)]
            else:
                inference1 = "~" + subForm1
            if subForm2[0] == "~":
                inference2 = subForm2[1:len(subForm2)]
            else:
                inference2 = "~" + subForm2
        elif connective == ">":
            inference1 = subForm1
            if subForm2[0] == "~":
                inference2 = subForm2[1:len(subForm2)]
            else:
                inference2 = "~" + subForm2
        elif connective == "&":
            if(subForm1[0] == "~"):
                inference1 = subForm1[1:len(subForm1)]
            else:
                inference1 = "~" + subForm1
            if(subForm2[0] == "~"):
                inference2 = subForm2[1:len(subForm2)]
            else:
                inference2 = "~" + subForm2
            
            isItAlpha = False
    else:
        if connective == ">":
            if subForm1[0] == "~":
                inference1 = subForm1[1:len(subForm1)]
            else:
                inference1 = "~" + subForm1
            inference2 = subForm2
            isItAlpha = False
        elif connective == "|":
            inference1 = subForm1
            inference2 = subForm2
            isItAlpha = False
        elif connective == "&":
            inference1 = subForm1
            inference2 = subForm2
    #if isItAlpha is false we branch
    return inference1, inference2, isItAlpha
