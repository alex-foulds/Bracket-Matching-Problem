# Bracket-Matching-Problem

## Introduction
The repository for the implementation of the Bracket Matching interview problem

Given a string of brackets, verify that the opening and closing of brackets is valid

Examples:
- "{[(])}" would return "Invalid"
- "{(())}" would return "Valid"

## Pseudo code and thoughts
### Initial thoughts
- Use Last In First Out data structure
- For a bracket to be closed, it's 'pair' must be the most recent to be opened

### Pseudo Code

```
inputString = "(())"
for i in inputString:
    
    If i is OpeningBracket:
        append to list;

    If i is ClosingBracket:
        If i is matchingBracket to list[last]:
            list pop
    
```