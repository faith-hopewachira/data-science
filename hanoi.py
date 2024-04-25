ef tower_of_hanoi(num_disks, start, target, auxiliary):
    if num_disks == 1:
        print(f"Move disk 1 from {start} to {target}")
        return tower_of_hanoi(num_disks -1, start, auxiliary, target)
    print(f"Move disk {num_disks} from {start} to {target}")
    tower_of_hanoi(num_disks -1, auxiliary, target, start)

    num_disks = 6
    tower_of_hanoi(num_disks, "A", "C" "B")

# Using stacks data structure knowledge
class Stack:
    def __init__(self):
        self.items = []
        def push(self, item):
            self.items.append(item)

        def pop(self):
            if not self.is_empty():
                return self.items.pop()
            
        def is_empty(self):
            return len(self.items) ==0
        
        def peek(self):
            if not self.is_empty():
             return self.items[-1]
            
        def towerOfHanoi(n):
            source = Stack()
            auxiliary = Stack()
            destination = Stack()

            for i in range(n, 0 , -1):
                source.push(i)

            if n%2 == 0 :
                temp = auxiliary
                auxiliary = destination
                destination = temp

            num_moves = 2**n -1

            for i in range(1, num_moves+1):
                if i % 3 ==1:
                    moveDisks(source,destination)
                if