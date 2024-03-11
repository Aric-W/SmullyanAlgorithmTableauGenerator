What is this program?:
    This is a logical tableau generator.

What is the purpose of this tableau-generator?
    This program automatically generates a logical tableau for an inputted truth-function using the alpha-beta 
    tableau generation algorithm described by Smullyan(2014).
    The purpose of logical tableaus is to prove that an inputted truth-function is (or is not) a tautology. For a definition of 
    a tautology, see the note on truth-functions below. This program is meant to provide a nice and simple example of 
    automated proofs.

What user input should look like:
    (1.) All valid input only contains the symbols '(',')','~','V','^','a','b','c','d','e','f','g',
        'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'.  31 in total.
         Any other symbols are invalid, if the user forgets the tableau-generator will remind them
    (2.) Lowercase letters represent propositional variables.
    (3.) Because there is no order of operations for logical connectives, all formulas (unless they are a propositional variable)
         are a surrounded by a pair of round braces: 1 left brace, '(', and 1 right brace, ')', 
    (4.) Individual propositional variables are not surrounded by braces, since that is redundant.
    (5.) Because a binary connective cannot be next to another binary connective, a unary connective cannot be next to another unary
         connective. Thus '~~p' is invalid, and the double-negative is '~(~p)'.

A note on truth-functions:
    Truth-functions (here called formulas) are composed of propositional variables, which are true or false and represent facts.
    In addition to propositional variables, there are also round braces: '(' ')' and connectives. This tableau-generator has
    4 connectives: 1 unary, and 3 binary. our unary connective (so-called because it applies to one formula) is '~' which represents
    negation, and applies to the left of the formula. Our binary connectives are placed 
    in-between conjoined formulas; they are:  '^' which represents logical conjunction, 'V' which represents logical disjunction
    and '>' which represents logical implication. 
    
    Below are truth tables that give all the interpretations for each of the three connectives. 
    
    Here are some clues for reading the tables: when p is true, ~p is false, when p and q are true
    p^q is true, if both p and q are false, pVq is false, if p is true and q is false then 'p implies q' (p>q) is false.

    p ~p      p q (p^q) (p>q) (pVq)
    T  F      T T  T    T      T
    F  T      T F  F    F      T
              F T  F    T      T
              F F  F    T      F

    A tautology is a formula that is always true regardless of the values of its variables. An example is given in the table below:

    p (pV~p)
    T  T
    F  T

    (pV~p) is true even when p is false! We can use truth-tables to determine whether or not a formula is a tautology, but a more
    efficient and advanced way is to use a logical tableau.
    
