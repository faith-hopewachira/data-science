# stack = []
stack1 = []
#ADDING THE NUMBERS TO THE STACK
stack1.append(10)
stack1.append(20)
stack1.append(30)
stack1.append(40)
print(stack1)

# # # #REMOVING NUMBERS FROM THE stack1
# stack1.pop()
# stack1.pop()
# stack1.pop()
# stack1.pop()
# print(stack1)

# #ACCESSING THE LAST ELEMENTIN THE stack1
print(stack1[-1])
print(stack1[0])
print(stack1[1])
print(stack1[2])
print(stack1[3])


# PUSH FUNCTION BODY
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
        # REMOVING THE ELEMENT FROM THE STACK
        e = stack.pop()
        print("removed element:",e)
        print(stack)

# USER TO SELECT THE OPERATION
while True:
    print("Select the option 1.push 2.pop 3.quit")
    choice = int(input())
    # EXECUTE PUSH FUNCTION BODY
    if choice ==1:
        push()
    elif choice ==2:
        pop_element()
    elif choice ==3:
        break
    else:
        print("Enter the correct operation!")





# stack2 = []

# stack2.push('onion')
# print(stack2)

# transport={"bus": ["morning","night"],["big","small"]}
# transport["bus"][0]