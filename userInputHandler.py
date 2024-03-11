import FormulaChecker as fc
import inferenceGenerator as ig
import developTableau as dt
import FormulaSplitter as fs
from colorama import Fore, Back, Style
import time
from TableauTree import TableauTree

def generateTable(input):
    TT = TableauTree("")
    if not fc.wellFormed(input):
        print(Fore.RED + "invalid input")
        print(Fore.WHITE + "")
        return
    else:
        if(len(input) == 2):
            print("ASSUME" + " " "~(" + input + ")")
            print("p BY ASSUMPTION")
            print(Fore.YELLOW + "THE INPUT IS NOT A TAUTOLOGY")
            print(Fore.WHITE + "")
            return
        if input[0] == "~":
            print("ASSUME" + " " "~(" + input + ")")
            if(dt.driver(input[1:len(input) - 1],[],"",[],TT)):
                print(Fore.GREEN + "THE INPUT IS A TAUTOLOGY")
                print(Fore.WHITE + "")
        else:
            print("ASSUME" + " " + "~" + input)
            if(dt.driver("~" + input,[],"",[],TT)):
                print(Fore.GREEN + "THE INPUT IS A TAUTOLOGY")
                print(Fore.WHITE + "")

            else:
                print(Fore.YELLOW + "THE INPUT IS NOT A TAUTOLOGY")
                print(Fore.WHITE + "")
    time.sleep(3)