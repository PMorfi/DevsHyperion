i = 1        
lines = 9  # the lines in the pattern given is 9

while i <= lines:
    if i <= lines // 2 + 1:
        print("*" * i)
    else:
        print("*" * (lines - i + 1))
    i += 1