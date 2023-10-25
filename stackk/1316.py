n = int(input())
sum = 0
for _ in range(n):
   s = input()
   st = [i for i in s]
   result = []
   for i in range(len(st) - 1, -1, -1):
      count = 0
      if st[i] != st[i - 1]:
         count = 0
         result.append(st[i])
      else:
         count += 1
      
   if count != 0:
      result.append(st[0])

   for i in range(len(result)):
      a = result.count(result[i])
      if a > 1:
         num = 0
         break
      else:
         num = 1

   sum += num
 
print(sum)
      
      
   
   
   