def main():
    i = 3
    intxt = input("Enter a nuber to stop at: ")
    topout = int(intxt)
    primelist = [2]
    isprime = 0
    j = 0

    while i < topout:
        j = sqrt(i)
        for p in primelist:
            if i % p == 0:
                isprime = 1
                break
            if j > p:
                break

        if isprime == 0:
            primelist.append(i)

        isprime = 0

        i += 1

    primelist.insert(0,1)

    for prime in primelist:
        print(prime)

main()


#Improvement ideas:
#   -Determine a quick half-point check, as in stopping at p = root(i) (because any higher number has no way to be a prime)
#   -Create a break condition in the for-loop after isprime != 0 to prevent over-evaluation
