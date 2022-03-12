"""
Linked List

Linked list - is a linear collection of data elements whose order is not given by their physical placement in memory.
Instead, each element (usually called "Node") points to the next.

Regular Linked list / Singly-linked List has connections only in one direction (e.g. left to right), but there is also
a Linked List where connections can go both directions which is called - Doubly-linked List.
"""

HeadNode = None
MENU_OPTIONS = {
    1: 'Quick create a Linked List',
    2: 'Delete a Linked List',
    3: 'Check if a Linked List is empty',
    4: 'Print out the values in the List',
    5: 'Find a node in a Linked List',
    6: 'Insert a node in a Linked List',
    7: 'Delete a node from a Linked List',
    0: 'Exit'
}


class ListNode:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer


def print_menu():
    print("\n================= MENU =================")
    for key in MENU_OPTIONS.keys():
        print(key, '--', MENU_OPTIONS[key])
    print("========================================")


def quick_create_list():
    global HeadNode
    node_d = ListNode('D', None)
    node_c = ListNode('C', node_d)
    node_b = ListNode('B', node_c)
    node_a = ListNode('A', node_b)
    HeadNode = node_a
    print("\nList created")


def delete_list():
    global HeadNode
    HeadNode = None
    print("\nList deleted")


def list_is_empty():
    global HeadNode
    return HeadNode is None


def print_count_nodes_with_loop():
    global HeadNode
    current = HeadNode
    count_nodes = 0

    if current is not None:
        print("\nNodes in the list:")
        while current.pointer is not None:
            print(current.value, end="-->")
            current = current.pointer
            count_nodes = count_nodes + 1

        count_nodes += 1
        print(current.value)

        print("Number of nodes in the list:", count_nodes)
        print("Last node at the position:", count_nodes - 1)
    else:
        print("\nList is empty")


def find_node(val):
    global HeadNode
    current = HeadNode

    if not list_is_empty():
        while (current.pointer is not None) and (current.value != val):
            current = current.pointer

        if current.value != val:
            print(val, "is not in the list")
        else:
            print("Found Node:", current.value)
    else:
        print("\nList is empty")


def insert_node(pos, val):
    global HeadNode
    current = HeadNode
    position_counter = 1

    node_x = ListNode(val, None)

    if pos == 0:
        HeadNode = node_x
        node_x.pointer = current
    else:
        try:
            while pos > position_counter:
                current = current.pointer
                position_counter += 1

            node_x.pointer = current.pointer
            current.pointer = node_x
        except Exception as e:
            print('\nSelected position exceeds the length of the list --->', e)
            print_count_nodes_with_loop()


def delete_node(val):
    global HeadNode
    previous = None
    current = HeadNode

    if not list_is_empty():
        if current.value == val:
            HeadNode = current.pointer
            print("Node:", current.value, "- deleted")
        else:
            while (current.pointer is not None) and (current.value != val):
                previous = current
                current = current.pointer

            if current.value != val:
                print(val, "is not in the list")
            else:
                previous.pointer = current.pointer
                print("Node:", current.value, "- deleted")
    else:
        print("\nList is empty")


def main():
    while True:
        print_menu()
        menu_option = None

        try:
            menu_option = int(input('\nEnter your choice: '))
        except ValueError as e:
            print('\nPlease provide integers only to avoid the following error:', e)
            main()

        if menu_option == 1:
            quick_create_list()
        elif menu_option == 2:
            delete_list()
        elif menu_option == 3:
            if list_is_empty():
                print("\nList is empty")
            else:
                print("\nList is not empty")
        elif menu_option == 4:
            print_count_nodes_with_loop()
        elif menu_option == 5:
            node_val = input('\nEnter node value to find: ')
            find_node(node_val)
        elif menu_option == 6:
            node_pos = int(input('\nEnter node position: '))
            node_val = input('Enter node value: ')
            insert_node(node_pos, node_val)
        elif menu_option == 7:
            node_val = input('\nEnter node value to delete: ')
            delete_node(node_val)
        elif menu_option == 0:
            print('Exiting...')
            exit()
        else:
            print('Invalid option. Please enter a number between [0 - 7].')


if __name__ == '__main__':
    main()
