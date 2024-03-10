import FormulaChecker as fc
import inferenceGenerator as ig
import developTableau as dt
import FormulaSplitter as fs
from colorama import Fore, Back, Style

def generateTable(input):
    if not fc.wellFormed(input):
        print("invalid input")
        return
    else:

        print("ASSUME" + " " + "~" + input)
        if(dt.driver("~" + input,[],"",[])):
            print(Fore.GREEN + "THE INPUT IS A TAUTOLOGY")
            print(Fore.WHITE + "")
            
        else:
            print(Fore.RED + "THE INPUT IS NOT A TAUTOLOGY")
            print(Fore.WHITE + "")