

def prime_numbers():

    numbers_to_work = [1, 4, 6, 7, 13, 9, 67]
    prime = []
    for i in numbers_to_work:
        
        if i <= 1 :
            continue
        for list_prime in range(2, int(i ** 0.5)+1):

            if i % list_prime == 0:

             break
        else :
           prime.append(i)

        
    return prime




result = prime_numbers()
print(result)