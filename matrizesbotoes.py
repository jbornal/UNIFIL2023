import numpy as np 
A = [[3, 1, 3], 
    [6, 5, 5]] 
B = [[100, 50], 
    [50, 100], 
    [50, 50]] 
  
  
result= [[0,0], 
        [0,0]] 
  
result = np.dot(A,B) 
  
for r in result: 
    print(r) 