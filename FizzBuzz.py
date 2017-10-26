def fizzbuzz(numbers):
    current_number = 0

    for n in numbers:

        n = numbers[current_number]

        if n % 3 == 0 and n % 5 == 0:
            numbers[current_number] = 'FizzBuzz'
            
        elif n % 3 == 0:
            numbers[current_number] = 'Fizz'

        elif n % 5 == 0:
            numbers[current_number] = 'Buzz'

        else:
            numbers[current_number] = 'Bazz'


        current_number = current_number + 1
    return numbers