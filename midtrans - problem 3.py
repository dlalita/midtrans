#Problem 3

import re
def normalize(num):
    erase = ['+', '*', '?', '/', '.', '-', '(', ')']
    if len(num) in range(2,17):
        for i in erase:
            if i in num:
                new_num = re.sub(i, '', num)
                if '0' in new_num[0]:
                    new_num = re.sub('0', '62', new_num)
    print (new_num)

add = input('Input number:...')
type(add)
normalize(add)
