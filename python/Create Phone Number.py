'''Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.
Example;
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"

/////////////////////////////////////////////////// solution ///////////////////////////////////////////////////'''

def create_phone_number(n):
    f1 = [str(n[i]) for i in [0,1,2]]
    f2 = [str(n[i]) for i in [3,4,5]]
    f3 = [str(n[i]) for i in [6,7,8,9]]
    number = f"({''.join(f1)}) {''.join(f2)}-{''.join(f3)}"
    return number
