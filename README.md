# CompilerDesign
Lab Component of Compiler Design

1. The lr.py file contains the functions which help us remove the left recursion and left factoring for a given grammar. 
2. These functions are crucial during the syntax analysis phase of a top-down parser ( Eg. LL(1) Parser ). Since the LL(1) parser does parsing from left to right, it is important to remove left recursion ( if present ) else it might create an infinite loop during parsing. Also it is important to remove the left factoring in order to eliminate back-tracking.
