#first = input('введите любое первое число:')
#second = input('введите второе любое число:')
#third = input('введите любое третье число:')

#if first == second and third == second:
 #   print(3)
#elif first == second or second == third or third == first:
 #   print(2)
#else:
#    print(0)



my_list =  [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 51]
count = 0
while count < len(my_list):

    if my_list [count] < 0:
        break
    elif my_list [count] > 0:
        print(my_list[count])
    count = count + 1 


















