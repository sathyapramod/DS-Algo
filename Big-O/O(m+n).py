import time

large1 = ['nemo' for i in range(100000)]
large2 = ['nemo' for i in range(100000)]

def find_nemo(array1, arrany2):
  t0 = time.time() # O(1)
  for i in range(0, len(array1)): #O(m)
    if array1[i] == 'nemo': # m*O(1)
      print("Found Nemo!!") # k*O(1)
  t1 = time.time() # O(1)
  print(f'Time taken to Search {t1 - t0} seconds.') # O(1)

  t0 = time.time() # O(1)
  for i in range(0, len(arrany2)): # O(n)
    if arrany2[i] == 'nemo': # n * O(1)
      print("Found Nemo!!") # l * O(1)
  t1 = time.time() # O(1)
  print(f'Time taken to search {t1 - t0} Seconds.') # O(1)


find_nemo(large1,large2)

# Total Time complexity of the function find_nemo = 
# O(1 + m + m*1 + k*1 + 1 + 1 + n + n*1 + l*1 + 1 + 1) = O(6 + 2m + 2n + k + l)
# Now if k <=m and l <=n. In worst case, k can be m and l can be n. We Consider worst case
# O(6 + 2m + 2n + m + n) = O(3m + 3n + 6) = O(3 (m + n + 2))
# We ignore constant
# Therefore, O(m + n +2) = O(m + n)