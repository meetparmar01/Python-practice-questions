for num in range(1, 501):   # numbers from 1 to 500
    if num % 3 == 0:        # check divisible by 3
        digit_sum = sum(int(d) for d in str(num))  # sum of digits
        if digit_sum > 10:  # check condition
            print(num,end=" ")