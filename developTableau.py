from inferenceGenerator import inGen


def develop(formula, listOfFacts,upperLevel,listOfAtoms,qualifier,TT):
    if len(upperLevel) == 0:
        because = " BY ASSUMPTION "
    else:
        because = " BECAUSE "
    if len(formula) <= 2:
        if(qualifier == "O"):
            TT.branch(formula)
        else:
            TT.infer(formula)
        #listOfAtoms.append(formula + qualifier)
        listOfAtoms.append(formula)
        return
        
    s1,s2,alpha = inGen(formula)
    listOfFacts.append(s1)
    listOfFacts.append(s2)

    if alpha:
        print(s1 + because + upperLevel)
        print(s2 + because + upperLevel)
        develop(s1,listOfFacts,s1,listOfAtoms,"F",TT)
        develop(s2,listOfFacts,s2,listOfAtoms,"F",TT)
        



    else:
        print("EITHER " + s1 + " OR " + s2 + because + upperLevel)

        
        copy1 = listOfFacts.copy()
        develop(s1,copy1,s1,listOfAtoms,"O",TT)
        del copy1
        
            

        copy2 = listOfFacts.copy()
        develop(s2,copy2,s2,listOfAtoms,"O",TT)
        del copy2


    
#I'm not using checkConjugate any more?
def checkConjugate(atom,listOfFacts):
    for c in listOfFacts:
        if (atom[0] == "~" and atom == "~" + c) or c == "~" + atom:
            return True
        
    return False

def driver(formula, listOfFacts,upperLevel,listOfAtoms,TT):
    develop(formula,listOfFacts,upperLevel,listOfAtoms,"F",TT)

    branches = []
    branch = []
    TT.goDownTheBranches(branches,branch)


    breakerFlag = False
    openBranches = 0
    for i in branches:
        breakerFlag = False
        for j in i:
            if(j == ""):
                continue
            if(breakerFlag):
                break
            for k in i:
                if ((j == "~" + k) or (k == "~" + j)):                  
                    breakerFlag = True
                    break
        if(not breakerFlag):
            openBranches = 1 + openBranches

    if(openBranches > 0):
        return False
    else: 
        return True




    
    