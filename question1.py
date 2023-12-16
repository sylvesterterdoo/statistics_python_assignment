# Question 1. 
# create 2 functions 
# 1. stack -> add, remove
# 2. queue -> add, remove
# stack(our_list, operation, new_element)
# queue(our_list, operation, new_element)

# Global constants
INITIAL_POSITION = 0
ADD_OPERATION    = 'add'
REMOVE_OPERATION = 'remove'


def stack(our_list, operation, new_element=None):
    _internal_stack = list(our_list)
    if operation == ADD_OPERATION:
        _internal_stack.insert(INITIAL_POSITION, new_element)
    elif operation == REMOVE_OPERATION:
        _internal_stack.pop(INITIAL_POSITION)
    else:
        raise Exception("Sorry, operation not supported, use (add, remove)")

    return _internal_stack

def queue(our_list, operation, new_element=None):
    _internal_queue = list(our_list)
    if operation == ADD_OPERATION:
        _internal_queue.append(new_element)
    elif operation == REMOVE_OPERATION:
        _internal_queue.pop(INITIAL_POSITION)
    else:
        raise Exception("Sorry, operation not supported, use (add, remove)")
    return _internal_queue

def Main():
    new_list = [1, 2, 3, 4]
    print(f"Initial list : {new_list}")
    print('Adding new element to the stack [0]')
    new_list = stack(new_list, 'add', 0)
    print(new_list)
    print('Remove an element from stack [0]')
    new_list = stack(new_list, 'remove')
    print(new_list)
    # Queue
    print(f"\nInitial list : {new_list}")
    print('Adding new element to the queue [5]')
    new_list = queue(new_list, 'add', 5)
    print(new_list)
    print('Remove an element from the queue')
    new_list = queue(new_list, 'remove')
    print(new_list)

# Starter program testing the structures
if __name__ == '__main__':
    Main()

