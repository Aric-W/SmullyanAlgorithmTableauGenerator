from inferenceGenerator import inGen

def reason(formula,TT,branchOrInfer):
    #if there is nothing to infer from then we are making an assumption
    if len(formula) == 0:
        because = " BY ASSUMPTION "
    else:
        because = " BECAUSE "
    if len(formula) <= 2:
        if(branchOrInfer == "I"):
            TT.infer(formula)
        else:
            TT.branch(formula) 
        return

    s1,s2,alpha = inGen(formula)

    if alpha:
        print(s1 + because + formula)
        print(s2 + because + formula)
        reason(s1,TT,"I")
        reason(s2,TT,"I")
        
    else:
        print("EITHER " + s1 + " OR " + s2 + because + formula)

        reason(s1,TT,"B")
        
        reason(s2,TT,"B")


def contradictionChecker(TT):
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
    
def reasoningDriver(formula,TT):
    reason(formula,TT,"I")

    return contradictionChecker(TT)