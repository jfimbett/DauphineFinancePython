

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

    # TODO: Create a list of numbers from 1 to N, call is number_array

    # TODO: Create an empty vector where you will store all the prime numbers
    #       call it primes
    primes = []
    
    # TODO: 1 is not a prime, set it in the boolean list to False
    
    for n in range(N):
        if bool_array[n] == True:
            primes.append(number_array[n])
            # TODO: loop through all numbers larger than the current one
            #       and set its value in the boolean list to false if its a multiple

    
    return primes


compute_primes(100)