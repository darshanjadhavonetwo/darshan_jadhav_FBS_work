def longest_common_prefix(strings):
    if not strings:
        return ""
    shortest = min(strings, key=len)
    
    prefix = ""
    
    for i in range(len(shortest)):
        # Take the set of characters at position i from all strings
        char_set = {s[i] for s in strings}
        
        if len(char_set) == 1:
            # All characters at this position are the same
            prefix += char_set.pop()
        else:
            break  

    return prefix


s= ["flower", "flow", "flight"]
r = longest_common_prefix(s)
print("Longest common prefix:", r)


