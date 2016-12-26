user_input = int(raw_input("Number to find divisors: "))
result_list = [divisor for divisor in range(1, user_input + 1) if user_input % divisor == 0]
print result_list
