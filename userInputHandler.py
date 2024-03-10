import FormulaChecker as fc
import inferenceGenerator as ig
import developTableau as dt
import FormulaSplitter as fs
from colorama import Fore, Back, Style
import time

def generateTable(input):
    if not fc.wellFormed(input):
        print(Fore.RED + "invalid input")
        print(Fore.WHITE + "")
        return
    else:
        if input[0] == "~":
            print("ASSUME" + " " "~(" + input + ")")
        else:
            print("ASSUME" + " " + "~" + input)
        if(dt.driver("~" + input,[],"",[])):
            print(Fore.GREEN + "THE INPUT IS A TAUTOLOGY")
            print(Fore.WHITE + "")
            
        else:
            print(Fore.YELLOW + "THE INPUT IS NOT A TAUTOLOGY")
            print(Fore.WHITE + "")
    time.sleep(3)