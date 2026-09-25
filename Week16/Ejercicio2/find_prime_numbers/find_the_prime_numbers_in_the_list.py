def prime_numbers(numbers_to_work):

    
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




