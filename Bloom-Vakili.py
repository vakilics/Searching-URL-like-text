import sys
import time
from bloomfilter import BloomFilter
n = 1000000 #no of items to add
p = 0.01 #false positive probability
 
bloomf = BloomFilter(n,p)
print("[ m = -nln(p)/(ln2)^2 ]: Bit array Size :{}".format(bloomf.size))
print("[ p= (1-[1-1/m]^kn)^k ]:  False positive Probability :{}".format(bloomf.fp_prob))
print("[ k= (m/n)ln2 ]: Number of hash functions :{}".format(bloomf.hash_count))

print() 

# Add NDN Names
NDN_Names = [line.rstrip('\n') for line in open("names1k.txt", "r")]
count = 0
#print(NDN_Names)    
for name in NDN_Names:
    bloomf.add(name)
    count += 1
print("NDN_Names:",count)
  
lookfor = "/ut/ece/routerlab"

timing = time.time()

#print(check)
if bloomf.check(lookfor) == True:
	print("BF_Result= True: "+lookfor)   	
	print("Time: ", time.time() - timing)
	
else:
 	print("Not Found !!!")

