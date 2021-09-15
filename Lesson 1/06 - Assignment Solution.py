#%%

def compute_primes(N):
    """
    
    Computes all prime numbers up to N
    Parameters
    ----------
    N : int

    Returns
    -------
    A list with all prime numbers <= N
    
    Algorithm: 
        1) Create a list of booleans of size N initialized to true
        2) Create a list of numbers from 1 to N
        3) From the list of booleans, leave the position of the first prime as true, 
           and change the boolean in the position of all the multiples of the prime as
           false
        4) Repeat the proceedure with the next prime until there are none left
        5) The elements with value true represent the positions of the prime numbers

    """
    
    # TODO: Create a list of booleans of size N initialized to true
    #       call it bool_array
    bool_array = [True for i in range(N)]

    # TODO: Create a list of numbers from 1 to N, call is number_array
    number_array = [ n + 1 for n in range(N)]

    # TODO: Create an empty vector where you will store all the prime numbers
    #       call it primes
    primes = []
    
    # TODO: 1 is not a prime, set it in the boolean list to False
    bool_array[0]=False
    
    for n in range(N):
        if bool_array[n] == True:
            primes.append(number_array[n])
            # TODO: loop through all numbers larger than the current one
            #       and set its value in the boolean list to false if its a multiple
            for j in range(n+1, N):
                if number_array[j]%number_array[n]==0:
                    bool_array[j] = False

    
    return primes

#%%
compute_primes(100)
# %%
# Extra, how many prime numbers up to n?

from matplotlib import pyplot as plt
import math
N= 100
x = [n+1 for n in range(1, N)]
pi_x = [len(compute_primes(n+1)) for n in range(1, N)]
plt.title("Prime counting function") 
plt.xlabel("x") 
plt.ylabel("pi(x)") 
plt.scatter(x,pi_x) # Plots dots
plt.show()
# %%

x_logx = [x[i]/math.log(x[i]) for i in range(len(x))]
plt.scatter(x,pi_x) # Plots dots
plt.plot(x,x_logx, 'red', zorder = 2) # Plots line
plt.show()
# %%
