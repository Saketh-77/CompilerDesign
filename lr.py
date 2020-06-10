"""
Name : Amancherla Shanmukha Sai Saketh
Reg.No : BL.EN.U4CSE17528
Section : C
Aim : To write functions that remove left recursion and left factoring for a given grammar(s)

"""

# Let us assume that termianls are lowercase letters and non-terminals are uppercase letters

grammar = {
    'E':['E+T','E-T','T'],
    'T':['T*F','T/F','F'],
    'F':['(E)','id','num']
}

grmr = {
    'E':['E+T','E-T','T'],
    'T':['T*F','T/F','F']
}

lrIdentified = False

# Printing a grammar in a readable format
def printGrammar(grammar):
    i=0
    f=0
    for LHS in grammar.keys():
        print(LHS,' -> ',end=' ')
        f = len(grammar[LHS])
        for rule in grammar[LHS]:
            if i==f-1:
                print(rule)
            else:
                print(rule,' | ',end=' ')        
            i+=1    
        i = 0 
    print('\n')    

# To check if the symbol is terminal or not
def isTerminal(symbol):
    return symbol.islower()

# To check if the symbol is non-terminal or not
def isNonTerminal(symbol):
    return symbol.isupper()

# To remove the left-recursion present in the grammar
def removeLR(grammar):
    lrFreeGrammar = {}
    newNonTerminal = ''
    start = ''
    lr = []
    terminalProductions = []
    nonTerminalProductions = []
    for index in range(len(grammar.keys())):
        start = list(grammar.keys())[index]
        rule = grammar[start]
        lr = []
        terminalProductions = []
        nonTerminalProductions = []
        newNonTerminal = ''
        for production in rule:
            if isTerminal(production[0]) or production[0]=='(':
                terminalProductions.append(production)
            elif isNonTerminal(production[0]):
                if production[0]!=start:
                    nonTerminalProductions.append(production)
                else:
                    lr.append(production)
                    lrIdentified = True
        if lrIdentified:
            newNonTerminal = start+'\''
            if len(terminalProductions)!=0:
                for i in range(len(terminalProductions)):
                    terminalProductions[i] = terminalProductions[i]+newNonTerminal
            if len(nonTerminalProductions)!=0:
                for i in range(len(nonTerminalProductions)):
                    nonTerminalProductions[i] = nonTerminalProductions[i]+newNonTerminal
            for i in range(len(lr)):
                prod = lr[i]
                prod = prod[1:]+newNonTerminal
                lr[i]=prod
            lrFreeGrammar[start] = lrFreeGrammar.get(start,terminalProductions+nonTerminalProductions)
            lr.insert(0,None)
            lrFreeGrammar[newNonTerminal] = lrFreeGrammar.get(newNonTerminal,lr)
            lrIdentified = False    
        else:
            lrFreeGrammar[start] = lrFreeGrammar.get(start,terminalProductions+nonTerminalProductions)       
    return lrFreeGrammar            

# To remove the left-factoring present in the given grammar
def leftFactoring(grammar):
    leftFG = {}
    removeLF = []
    nonRemoveLF = []
    for i in range(len(grammar.keys())):
        removeLF = []
        nonRemoveLF = []
        start = list(grammar.keys())[i]
        rules = grammar[start]
        for rule in rules:
            if len(rule)!=1 and rule[0]==start:
                removeLF.append(rule[1:])
            else:
                nonRemoveLF.append(rule)
        if len(removeLF)>1:
            newStartSymbol = start+'"' 
            newRule = [start+newStartSymbol]
            newRule.extend(nonRemoveLF)
            leftFG[start] = leftFG.get(start,newRule)
            leftFG[newStartSymbol] = leftFG.get(newStartSymbol,removeLF)
    return leftFG

# Grammar free of left recursion
lrFreeGrammar = removeLR(grammar)

# Grammar free of left factoring
lfFreeGrammar = leftFactoring(grmr)

# Main function
if __name__=="__main__":
    print('Grammar before left recursion removal : ')
    printGrammar(grammar)
    print('Grammar after removing left recursion : ')
    printGrammar(lrFreeGrammar)
    print('Grammar before removal of left factoring : ')
    printGrammar(grmr)
    print('Grammar after removal of left factoring : ')
    printGrammar(lfFreeGrammar)
    
