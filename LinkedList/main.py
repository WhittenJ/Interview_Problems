class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, newElement):
        newNode = Node(newElement)

        # Add the newNode if the List is new.
        if(self.head == None):
            self.head = newNode
            return
        # Otherwise, push all of the other elements down by 1
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode

    # Delete last Element
    def delete_last(self):
        if(self.head != None): # Don't do anything if list is empty
            if(self.head.next == None): # If there's no other items in the list, delete this one
                self.head = None
            else: # Loop through the list until we get to the last element and delete it.
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                lastNode = None

    # Delete at given location
    def delete_at_position(self, position):
        if self.head is None: # Don't do anything if list is empty
            return
        if position == 0: # Delete the head node and replace it with the next node.
            self.head = self.head.next
            return self.head

        # Not super sure what this is doing just yet.
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    # Delete first element
    def delete_first(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None

    # Display the content of the list
    def PrintList(self): # pragma: no cover
        temp = self.head
        if(temp != None):
            print("The list contains:", end=" ")
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")

def printOptions(): # pragma: no cover
    print("Press 1 to add an element: ")
    print("Press 2 to delete an element from the beginning: ")
    print("Press 3 to delete an element from an input location: ")
    print("Press 4 to delete an element from the last: ")
    print("Press 0 to stop the process and display the content of the linked list: ")

def main():
    MyList = LinkedList()
    printOptions()

    n = 10
    while(n != 0):
        n = int(input("Enter your choice: "))
        if(n==1):
            MyList.add_element(int(input("Enter an element to push: ")))
        if(n==2):
            MyList.delete_first()
            print("The first element of the linked list is deleted.\n")
        if(n==3):
            pos = int(input("Enter the position of the element which needs to be deleted: "))
            MyList.delete_at_position(pos)
        if(n==4):
            MyList.delete_last()
            print("The last element of the linked list is deleted.\n")
        if(n==0):
            break
    print("\nResult: \n")
    MyList.PrintList()

if __name__ == "__main__": # pragma: no cover
    main()