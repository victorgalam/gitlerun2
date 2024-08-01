from itertools import product

# קלט מהמשתמש - רשימה ראשונה
input1 = input("Enter the first list separated by spaces: ")
list1 = input1.split()

# קלט מהמשתמש - רשימה שנייה
input2 = input("Enter the second list separated by spaces: ")
list2 = input2.split()

# יצירת Cartesian product באמצעות הפונקציה product של itertools
cartesian_product = list(product(list1, list2))

print(cartesian_product)


#li = []
#x = input()
#while x != -99:
#    li.append(x)
#    x = input()
#print(li)



#x = input("enter num: ")
#li = [i for i in x]
#print(li)



#num = int(input())
 #li = []
 #while num > 0:
  #  li.append(num % 10)
  #  num //= 10
#li.reverse()
#print(li)

