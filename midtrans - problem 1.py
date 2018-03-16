#Problem 1 - Address Similarity

def address(address1, address2):
    
    set1 = set(address1.split(' '))
    set2 = set(address2.split(' '))

    count = 0

    for i in set1:
        if i in set2:
            print('There is similarity', i)
            count += 1

    print ('Same words' , count);

    
#input
add1 = input('First address:...')
type(add1)
add2 = input('Second address:...')
type(add2)
check = address(add1, add2)
