number = int(input())

reverse_number = 0
number_copy = number
while number_copy > 0:
    reverse_number = reverse_number*10 + number_copy%10
    number_copy = number_copy // 10
if number == reverse_number:
    print('Palindrome')
else:
    print('No Palindrome')