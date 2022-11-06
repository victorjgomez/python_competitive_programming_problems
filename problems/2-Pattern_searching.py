'''
• Pattern searching 

Having the following string AABAACAADAABAABA, please find how many times you can find the pattern AABA (the string and the pattern to found could be changed) 

Example:
Input: AABAACAADAABAABA
Pattern: AABA
Result: Pattern found at 0, 9 and 12

'''

pattern = 'AABA'

print('Enter your input:')
input = input()

result = []

end = (len(input) - len(pattern)) + 1

for index in range(end):
    
    if input[index] == pattern[0] and input[index+1] == pattern[1] and input[index+2] == pattern[2] and input[index+3] == pattern[3]:
          result.append(index)  
    
    

print(result)