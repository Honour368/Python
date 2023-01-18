class Solution:
   def solve(self, matrix):
      n = len(matrix)

      rows = set()
      cols = set()
      diags = set()
      rev_diags = set()

      for i in range(n):
         for j in range(n):
            if matrix[i][j]:
               rows.add(i)
               cols.add(j)
               diags.add(i - j)
               rev_diags.add(i + j)

      return len(rows) == len(cols) == len(diags) == len(rev_diags) == n
n = int(input())
matrix = []

for i in range(n):          # A for loop for row entries 
    column = []
    for j in range(n): 
        column.append(0)
    matrix.append(column)
  

for i in range(n):
   cordinates = input().split()
   for j in range(n):
       matrix[int(cordinates[0])][int(cordinates[1])] = 1

#for i in range(n):
#    for j in range(n):
#       print(str(matrix[i][j]) + ' ')
#    print('\n')

ob = Solution()


if ob.solve(matrix) == True:
    print("Attack")
else:
    print("Safe")
