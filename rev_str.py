def rev_string(str1):
    rev_str = ''
    index = len(str1)
    while index > 0:
        rev_str = rev_str + str1[index - 1]
        index = index - 1
    return rev_str
        
output = rev_string('1234PRAKASH56789')
print(output)