stack = []
#ADDING THE NUMBERS TO THE STACK
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# print(stack)

# # #REMOVING NUMBERS FROM THE STACK
# # stack.pop()
# # stack.pop()
# # stack.pop()
# # stack.pop()
# # print(stack)

# #ACCESSING THE LAST ELEMENTIN THE STACK
# print(stack[-1])
# print(stack[0])
# print(stack[1])
# print(stack[2])
# print(stack[3])


# PUSH FUNCTION
def push():
    element = input("Enter the element:")
    stack.append(element)
    print(element)

# POP FUNCTION
def pop_element():
    #IF STACK IS EMPTY
    if not stack:
        print("stack is empty!")
    else:
        e = stack.pop()
        print("removed element:",e)
        print(stack)

# USER TO SELECT THE OPERATION
while True:
    print("Select the option 1.push 2.pop 3.quit")
    choice = int(input())
    if choice ==1:
        push()
    elif choice ==2:
        pop_element()
    elif choice ==3:
        break
    else:
        print("Enter the correct operation!")




