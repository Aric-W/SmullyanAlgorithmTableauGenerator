import FormulaChecker as fc
#import developTableau as dt
from colorama import Fore
from TableauTree import TableauTree
from TableauFormer import reasoningDriver

def generateTable(input):
    efficiencyTableau = False
    if not fc.wellFormed(input):
        print(Fore.RED + input + " IS NOT VALID INPUT")
        print(Fore.WHITE + "")
        return
    else:
        TT = TableauTree()
        if(len(input) == 2):
            print("ASSUME" + " " "~(" + input + ")")
            print("p BY ASSUMPTION")
            print(Fore.YELLOW + input + " IS NOT A TAUTOLOGY")
            print(Fore.WHITE + "")
            return
        if input[0] == "~":
            print("ASSUME" + " " "~(" + input + ")")
            if(reasoningDriver(input[1:len(input)-1],TT)):
                print(Fore.GREEN + input + " IS A TAUTOLOGY")
                print(Fore.WHITE + "")
        else:
            print("ASSUME" + " " + "~" + input)
            if(reasoningDriver("~" + input,TT,efficiencyTableau)):
                print(Fore.GREEN + input + " IS A TAUTOLOGY")
                print(Fore.WHITE + "")

            else:
                print(Fore.YELLOW + input + " IS NOT A TAUTOLOGY")
                print(Fore.WHITE + "")