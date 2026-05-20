s = input("Input: ")

if len(s) == 0:
    print("NONE")
else:
    max_seq = ""
    current_seq = s[0]
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_seq += s[i]
        else:
            # Check if the sequence that just ended is the largest one so far
            if len(current_seq) > len(max_seq):
                max_seq = current_seq
            current_seq = s[i] # Reset for the new character
            
    # One final check for the sequence that finishes at the very end of the string
    if len(current_seq) > len(max_seq):
        max_seq = current_seq
        
    # Output the result
    if len(max_seq) > 1:
        print(max_seq)
    else:
        print("NONE")