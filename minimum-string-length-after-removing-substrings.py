def minLength(self, s: str) -> int:
    # stack to push letters as we scan through string
    output_length = 0
    # add to output length whenever we clear the stack and at the end
    chars_stack = []

    for i in s:
        # A or C
        if i == "A" or i == "C":
            chars_stack.append(i)
        # B
        elif i == "B" and len(chars_stack) > 0 and chars_stack[-1] == "A":
            chars_stack.pop()            
        # D
        elif i == "D" and len(chars_stack) > 0 and chars_stack[-1] == "C":
            chars_stack.pop()
        # not any of ABCD
        else:
            chars_stack.append(i)
            output_length += len(chars_stack)
            chars_stack = []
    
    return output_length + len(chars_stack)
            