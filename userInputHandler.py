import FormulaChecker as fc
#import developTableau as dt
from colorama import Fore
from TableauTree import TableauTree
from TableauFormer import reasoningDriver

def generateTable(input):
    TT = TableauTree("")
    if not fc.wellFormed(input):
        print(Fore.RED + input + " IS NOT VALID INPUT")
        print(Fore.WHITE + "")
        return
    else:
        if(len(input) == 2):
            print("ASSUME" + " " "~(" + input + ")")
            print("p BY ASSUMPTION")
            print(Fore.YELLOW + input + " IS NOT A TAUTOLOGY")
            print(Fore.WHITE + "")
            return
        if input[0] == "~":
            print("ASSUME" + " " "~(" + input + ")")
            #if(dt.driver(input[1:len(input) - 1],[],"",[],TT)):
            if(reasoningDriver(input[1:len(input)-1],TT)):
                print(Fore.GREEN + input + " IS A TAUTOLOGY")
                print(Fore.WHITE + "")
        else:
            print("ASSUME" + " " + "~" + input)
            #if(dt.driver("~" + input,[],"",[],TT)):
            if(reasoningDriver("~" + input,TT)):
                print(Fore.GREEN + input + " IS A TAUTOLOGY")
                print(Fore.WHITE + "")

            else:
                print(Fore.YELLOW + input + " IS NOT A TAUTOLOGY")
                print(Fore.WHITE + "")