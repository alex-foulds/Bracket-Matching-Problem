#Bracket Matching Problem

def main():
    inputString = '({[]()})';
    stack = [];

    for i in inputString:
        if isOpener(i):
            #Last In First Out
            stack.append(i);
        
        elif isCloser(i):
            if bracketMatch(stack[-1],i):
                #Remove most recently opened bracket
                stack.pop();
            else:
                #More closers than openers
                print("Invalid bracket string");
                return False;
        
        else:
            print("Unexpected character:", i);
            return False;
    
    #Ensure that stack variable is empty
    if len(stack)==0 and len(inputString)>0:
        print("Valid String");
    else:
        #More openers than closers
        print ("Invalid or Empty Input")

def isOpener(var):
    if var in ['[','{','(']:
        return True;
    else:
        return False;

def isCloser(var):
    if var in [']','}',')']:
        return True;
    else:
        return False;

#Match up bracket pairings
def bracketMatch(var1, var2):
    if var1 == '[' and var2 == ']':
        return True;
    if var1 == '(' and var2 == ')':
        return True;
    if var1 == '{' and var2 == '}':
        return True;
    else:
        return False;

main();