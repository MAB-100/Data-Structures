from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    
    for i, char in enumerate(text):
        if char in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(char, i + 1))
        
        elif char in ")]}":
            if not opening_brackets_stack:
                # No matching opening bracket
                return i + 1
            
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, char):
                # Mismatched bracket
                return i + 1
    
    # If there are unmatched opening brackets left
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    
    return "Success"

def main():
    text = input().strip()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
