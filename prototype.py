
import time as ti
import numpy as np
import multiprocessing
import sys



#==========================================
def myfunction(x,y,z):
    
    ti.sleep(1)
    
    return 3*x, y**2, z+1

#==========================================
#Parallelized computation
def wrapper(inputs) :
    
    func = inputs[0]
    args = inputs[1:]
    
    return func(*args)

#==========================================        
def parallel(inputs, lenght, nbrCores, *outputs):
    
    workers = multiprocessing.Pool(processes = nbrCores)
    results = workers.imap(wrapper,inputs)
    
    for i, result in enumerate(results, 0): 
        for j, output in enumerate(outputs, 0): 

            output[i] = result[j]
            
        sys.stderr.write('\rProgress : {0}/{1}'.format(i+1,lenght))
         
    workers.close()
    workers.join()    

    return 0

#==========================================
#inputs
x = np.ones([10,100])
y = np.ones([10,100])
z = np.ones([10,100])
N = len(x)

multiplied_x = np.zeros([10,100])
squared_y = np.zeros([10,100])
added_z = np.zeros([10,100])

nbrCores = 2

inputs = ((myfunction, x[i], y[i], z[i]) for i in xrange(len(x)))

strt = ti.time()
parallel(inputs, N, nbrCores, multiplied_x, squared_y, added_z)
print ti.time()-strt















