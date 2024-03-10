from inferenceGenerator import inGen

def develop(formula, listOfFacts,upperLevel,listOfAtoms,qualifier):
    
    if len(upperLevel) == 0:
        because = " BY ASSUMPTION "
    else:
        because = " BECAUSE "
    if len(formula) <= 2:
        listOfAtoms.append(formula + qualifier)
        return
        
    s1,s2,alpha = inGen(formula)
    listOfFacts.append(s1)
    listOfFacts.append(s2)

    if alpha:
        print(s1 + because + upperLevel)
        print(s2 + because + upperLevel)
        develop(s1,listOfFacts,s1,listOfAtoms,"F")
        develop(s2,listOfFacts,s2,listOfAtoms,"F")
        



    else:
        print("EITHER " + s1 + " OR " + s2 + because + upperLevel)

        
        copy1 = listOfFacts.copy()
        develop(s1,copy1,s1,listOfAtoms,"O")
        del copy1
        
            

        copy2 = listOfFacts.copy()
        develop(s2,copy2,s2,listOfAtoms,"O")
        del copy2


    

def checkConjugate(atom,listOfFacts):
    for c in listOfFacts:
        if (atom[0] == "~" and atom == "~" + c) or c == "~" + atom:
            return True
        
    return False

def driver(formula, listOfFacts,upperLevel,listOfAtoms):
    develop(formula,listOfFacts,upperLevel,listOfAtoms)
    
    contradiction = True
    for i in listOfAtoms:
        c = 0
        for j in listOfAtoms:
            if (i == "~" + j) or (j == "~" + i):
                contradiction = contradiction and True
                break
            c = c + 1
        if c == len(listOfAtoms):
            contradiction = contradiction and False
    return contradiction




    
    