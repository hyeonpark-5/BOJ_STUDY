result = 0
dic = {2: ['A', 'B', 'C'], 
       3: ['D', 'E', 'F'],
       4: ['G', 'H', 'I'],
       5: ['J', 'K', 'L'],
       6: ['M', 'N', 'O'],
       7: ['P', 'Q','R','S'],
       8: ['T', 'U', 'V'],
       9: ['W', 'X', 'Y', 'Z']}

word = input()

result += len(word)

for w in word:
    for k, v in dic.items():
        if w in v:
            result += k

print(result)