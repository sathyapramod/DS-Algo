#  What is the Big O of the below function?

def anotherFunChallenge(input):
  a = 5 # O(1)
  b = 10 # O(1)
  c = 50 # O(1)
  for i in range(0,input): # O(m)
    x = i + 1 # m * O(1)
    y = i + 2 # m * O(1)
    z = i + 3 # m * O(1)
  for i in range(0,input): # O(n)
    p = i * 2 # n * O(1)
    q = i * 2 # n * O(1)
  whoAmI = "I don't know" # O(1)

anotherFunChallenge(5)

# Total Time complexity of the function anotherFunChallenge = 
# O ( 1 + 1 + 1 + m + m*1 + m*1 + m*1 + n + n*1 + n*1 + n*1 + 1) = O (4 + 4m + 4n)
# O (4 (1 + m + n )) = O(m + n)
  