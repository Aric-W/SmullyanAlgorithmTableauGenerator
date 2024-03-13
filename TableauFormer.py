from inferenceGenerator import inGen

def reason(formula,TT,branchOrInfer,efficiencyTableau):
    #if there is nothing to infer from then we are making an assumption
    if(not efficiencyTableau):
        if(branchOrInfer == "I"):
            TT.infer(formula)
        else:
            TT.branch(formula) 
    if len(formula) == 0:
        because = " BY ASSUMPTION "
    else:
        because = " BECAUSE "
    if len(formula) <= 2:
        if(efficiencyTableau):
            if(branchOrInfer == "I"):
                TT.infer(formula)
            else:
                TT.branch(formula) 
        return

    s1,s2,alpha = inGen(formula)


    if alpha:
        print(s1 + because + formula)
        print(s2 + because + formula)
        reason(s1,TT,"I",efficiencyTableau)
        reason(s2,TT,"I",efficiencyTableau)
        
    else:
        print("EITHER " + s1 + " OR " + s2 + because + formula)

        reason(s1,TT,"B",efficiencyTableau)
        
        reason(s2,TT,"B",efficiencyTableau)


def contradictionChecker(TT):
    branches = []
    branch = []
    TT.goDownTheBranches(branches,branch)


    breakerFlag = False
    openBranches = 0
    #iterate through the list of branches
    #when a contradiction is found on a branch,
    #that is when a variable is found in the same branch with its conjugate
    #for example, if p is found with ~p
    #break out of the nested for loop that takes an element of the 
    #branch and tries to find it's conjugate
    #and move on to the next branch
    for i in branches:
        breakerFlag = False
        for j in i:
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
    
def reasoningDriver(formula,TT,efficiencyTableau):
    reason(formula,TT,"I",efficiencyTableau)

    return contradictionChecker(TT)