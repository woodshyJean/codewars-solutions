'''Your task is to make a function that can take any non-negative integer as an argument
and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

//////////////////////////////////////////////// solution ///////////////////////////////////////////////'''

def descending_order(num):
    s_num = list(str(num))
    s_num.sort(reverse=True)
    i_list = [str(n) for n in s_num]
    fin = ''.join(i_list)
    return int(fin)
