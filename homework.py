#find if a num is even or odd
# find gratest of three
# find sum of all the elements in an array
# find peak element in an array
# find maximum element in an array
# find second maximum element in an array
# find second largest element in an array
# reverse an array with out using built-in-functions
# find the sum of squares of given number
# find sum of squares of even and odd digits
# check whether given number is palindrome or not using while loop
# write a program to print frst n fibonacci series
#find even or odd
#def even_or_odd(number):
#    if number % 2 == 0:
#        return f"{number} is even."
#    else:
#        return f"{number} is odd."

#find greatest of 3
#def find_greatest_of_three(a, b, c):
    # Compare a with b and c to find the largest
#    if a >= b and a >= c:
#        return a
#    elif b >= a and b >= c:
#        return b
#    else:
#        return c
#num1 = 12
#num2 = 27
#num3 = 8
#print(f"The greatest of {num1}, {num2}, and {num3} is: {find_greatest_of_three(num1, num2, num3)}")

#find sum of all elements in an array
#def sum_of_array(arr):
#    return sum(arr)
#array = [1, 2, 3, 4, 5]
#print(f"The sum of all elements in the array {array} is: {sum_of_array(array)}")

#find peak element in an array
#def find_peak_element(nums):
#    left, right = 0, len(nums) - 1
#   while left < right:
#        mid = (left + right) // 2
#        if nums[mid] > nums[mid + 1]:
#            right = mid  
#        else:
#            left = mid + 1  
#    return left
#nums = [1, 2, 3, 1]
#peak_index = find_peak_element(nums)
#print(f"A peak element in the array {nums} is at index {peak_index}, with value {nums[peak_index]}")

#find max element in an array
#def find_max_element(nums):
#    max_value = max(nums)
#    return max_value
#nums = [5, 12, 7, 3, 15, 9]
#max_value = find_max_element(nums)
#print(f"The maximum element in the array {nums} is: {max_value}")

#find second max element in an array
#def find_second_max(nums):
#    max1 = float('-inf')
#    max2 = None
#    for num in nums:
#        if num > max1:
#            max2 = max1
#            max1 = num
#        elif num != max1 and (max2 is None or num > max2):
#            max2 = num
#    return max2
#nums = [5, 12, 7, 3, 15, 9]
#second_max = find_second_max(nums)
#print(f"The second maximum element in the array {nums} is: {second_max}")

#find second largest element in an array
#def find_second_largest(nums):
#    if len(nums) < 2:
#        return None 
#    first_max = float('-inf')
#    second_max = None
#    for num in nums:
#        if num > first_max:
#            second_max = first_max
#            first_max = num
#        elif num != first_max and (second_max is None or num > second_max):
#            second_max = num
#    return second_max
#nums = [5, 12, 7, 3, 15, 9]
#second_largest = find_second_largest(nums)
#print(f"The second largest element in the array {nums} is: {second_largest}")

#reverse an array without using built in functions
#def reverse_array(arr):
    #    n = len(arr)
    #   for i in range(n // 2):
#        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
#array = [1, 2, 3, 4, 5]
#print("Original array:", array)
#reverse_array(array)
#print("Reversed array:", array)

#find the sum of squares of given number
#def sum_of_squares(n):
#    sum_squares = 0
#    for i in range(1, n + 1):
#        sum_squares += i * i
#    return sum_squares
#number = 5
#result = sum_of_squares(number)
#print(f"The sum of squares of the first {number} natural numbers is: {result}")

#find sum of squares of even and odd digits
#def sum_of_squares_even_odd_digits(number):
#    even_sum_squares = 0
#    odd_sum_squares = 0
#    number_str = str(number)
#    for digit_char in number_str:
#        digit = int(digit_char)
#        if digit % 2 == 0:
#            even_sum_squares += digit * digit
#        else:
#            odd_sum_squares += digit * digit
#     return even_sum_squares, odd_sum_squares
#num = 1234567
#even_sum, odd_sum = sum_of_squares_even_odd_digits(num)
#print(f"Number: {num}")
#print(f"Sum of squares of even digits: {even_sum}")
#print(f"Sum of squares of odd digits: {odd_sum}")

#check whether given number is palindrome or not using while loop
#def is_palindrome(number):
#    number_str = str(number)
#    left = 0
#    right = len(number_str) - 1
#    while left <= right:
#        if number_str[left] != number_str[right]:
#            return False
#        left += 1
#        right -= 1
#     return True
#num = 12321
#if is_palindrome(num):
#    print(f"{num} is a palindrome")
#else:
#    print(f"{num} is not a palindrome")

#write a program to print first n fibonacci series
#def fibonacci_series(n):
#    fib_list = [0, 1]
#    for i in range(2, n):
#        next_fib = fib_list[-1] + fib_list[-2]
#        fib_list.append(next_fib)
#    return fib_list
#n = 10  
#fibonacci_numbers = fibonacci_series(n)
#print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")