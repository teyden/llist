from A4Q1e import *

def main(testLevel):
    
    if testLevel == 1:
        L = LinkedList()
        print "\n\n\tTESTLEVEL = 1\n\n"
        #
        #
        # Test constructor __init__
        print "***Test __init__ ***"
        if L.head == L.tail and L.tail == None:
            print "Passed test 1, __init__:  Empty list so head and tail points to None"
        else: 
            print "Failed test 1, __init__:  Empty list"
        
        if L.size == 0:
            print "Passed test 2, __init__:  List size 0"
        else:
            print "Passed test 2, __init__:  List size 0"
        
        #
        #
        # Test append() #
        print "\n\n***Test append() on good input***"
        L.append(1)
        if L.head.item == 1:
            print "Passed test 1, append():  Add single item"
        else:
            print "Failed test 1, append():  Add single item"
            
        if L.head == L.tail and L.size == 1:
            print "Passed test 2, append():  Head and tail point at same node; thus size = 1"
        else:
            print "Failed test 2, append():  Head and tail references"
            
        L.append(2)
        if L.head != L.tail and L.size == 2:
            print "Passed test 3, append():  Head and tail no longer point at same node"
        else:
            print "Failed test 3, append():  Head and tail references"
        
            
        #
        #
        # Test str() #
        print "\n\n***Test str() on good input***"
        emptylist = LinkedList()        
        el = str(emptylist)
        el_print = "[]"
        l = str(L)
        l_print = "[1, 2]"
        
        if el == el_print:
            print "Passed test 1, str():  Correct string format for empty list"
        else:
            print "Failed test 1, str():  Incorrect string format for empty list"
        
        if l == l_print:
            print "Passed test 2, str():  Correct string format"
        else:
            print "Failed test 2, str():  Incorrect string format"

            
        #
        #
        # Test len()
        print "\n\nTest len() on good input:"
        length = len(L)
        if length == L.size and L.size == 2: 
            print "Passed test 1, len():  Non-empty list"
        else:
            print "Failed test 1, len():  Non-empty list"
        
        LL = LinkedList()
        length = len(LL)
        if length == 0:
            print "Passed test 2, len():  Empty list"
        else:
            print "Failed test 2, len():  Empty list"
    
            
            
            
    elif testLevel == 2:
        main(1)
        
        print "\n\n\tTESTLEVEL = 2\n\n"
        l = LinkedList()
        for x in range(10):
            l.append(x**2)
        """
        l is a list which looks like:
        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        len(l) == 10
        """
        #
        #
        # Test good input
        # remove(i)
        print "***Testing remove() on good and bad input***"
        l.remove(0)
        if l.head.item == 1 and len(l) == 9:
            print "Passed test 1, remove():  Item at list head removed"
        else:
            print "Failed test 1, remove():  Item at list head not removed"
        
        l.remove(81)
        if l.tail.item == 64 and len(l) == 8:
            print "Passed test 2, remove():  Item at list tail removed"
        else:
            print "Failed test 2, remove():  Item at list tail not removed"
            
        l.remove(25)
        length = len(l)
        if length == 7:
            print "Passed test 3, remove(): Item in middle of list removed"
        else: 
            print "Failed test 3, remove(): Item in middle of list not removed"
            
        # Test bad input
        try:
            l.remove(100)
        except ValueError:
            print "Passed test 4, remove()  Item not found"
        except Exception:
            print "Failed test 4, remove(): Item not found"
        
        ll = LinkedList()
        try:
            ll.remove(1)
        except ValueError:
            print "Passed test 5, remove(): Attempt to remove from empty list"
        except Exception:
            print "Failed test 5, remove(): Attempt to remove from empty list"
        
            
            
        
    elif testLevel == 3: 
        main(2)
        print "\n\n\tTESTLEVEL = 3\n\n"
        """
        l = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        """
        
        # Test good input
        l = LinkedList()
        for x in range(10):
            l.append(x**2)
            
        #
        #
        # pop(i)
        print "***Testing pop() on good and bad input***"
        if l.pop(0) == 0 and l.head != 0: 
            print "Passed test 1, pop: Removed node at first index position"
        else:
            print "Failed test 1, pop: Did not remove node at i = 0"
        
        if l.pop(2) == 9 and l.size == 8:
            print "Passed test 2, pop: Removed node in middle of list"
        else:
            print "Failed test 2, pop: Did not remove node in middle of list"
        
        if l.pop(l.size-1) == 81 and l.size == 7:
            print "Passed test 3, pop: Removed last node"
        else: 
            print "Failed test 3, pop: Did not remove last node"
        
        ll = LinkedList()
        # empty list
        try: 
            ll.pop(0)
        except IndexError:
            print "Passed test 4, pop - bad input: Attempt to remove from empty list"
        else:
            print "Failed test 4, pop - bad input: IndexError" 
        
        # index out of range
        try:
            length = l.size
            l.pop(length)
        except IndexError:
            print "Passed test 5, pop - bad input: pop index out of range"
        else:
            print "Failed test 5, pop - bad input: IndexError"
        
        # negative input 
        try:
            l.pop(-1)
        except ValueError:
            print "Passed test 6, pop - bad input: Input must be non-negative"
        else:
            print "Failed test 6, pop - bad input: Negative input"

        
            
        print "\n\n***Testing insert() on good and bad input***"
        #
        #
        # insert(i, anItem)
        l.insert(l.size, 10000)
        if l.pop(l.size-1) == 10000:
            print "Passed test 1, insert: Insert in last index position"
        else: 
            print "Failed test 1, insert: Insert in last index position"
        
        l.insert(0, 999)
        if l.pop(0) == 999: 
            print "Passed test 2, insert(): Insert in first index position"
        else:
            print "Failed test 2, insert(): Insert in first index position"
            
        ll = LinkedList()
        ll.insert(0, "hey")
        if ll.pop(0) == "hey" and ll.head == None:
            print "Passed test 3, insert(): Insert into an empty list"
        else:
            print "Failed test 3, insert(): Did not insert into empty list"
        
        # ensure nodes are moved over by one element 
        ll.insert(0, "a")
        ll.insert(0, "b")
        if ll.pop(1) == "a" and ll.size == 1:
            print "Passed test 4A, insert(): Insert shifts elements over by one position"
        else:
            print "Failed test 4, insert(): Did not shift elements over correctly"
        
        if ll.head.item == ll.tail.item:
            print "Passed test 4B, insert():  Correct reassignment of head and tail"
        else:
            print "Failed test 4B, insert():  Incorrect reassignment of head and tail"
            
        # index out of range
        try:
            length = l.size
            l.insert(length+1,"A")
        except IndexError:
            print "Passed test 5, insert() - bad input: Index out of range"
        else:
            print "Failed test 5, insert() - bad input: IndexError"
        
        # negative input 
        try:
            l.insert(-1, "A")
        except ValueError:
            print "Passed test 6, insert() - bad input: Input must be non-negative"
        else:
            print "Failed test 6, insert() - bad input: Negative input"
        
            
            
        
        print "\n\n***Testing count() on good and bad input***"
        # count(anItem)
        l = LinkedList()
        for i in range(15):
            if i%2 == 0:
                l.append("hi")
            else:
                l.append("bye")
            
        if l.count("hi") == 8:
            print "Passed test 1, count(): Correct count"
        else:
            print "Failed test 1, count(): Wrong count"
        
        if l.count("bye") == 7:
            print "Passed test 2, count(): Correct count"
        else:
            print "Failed test 2, count(): Wrong count"
        
        if l.count(1) == 0:
            print "Passed test 3, count(): Zero number of that item"
        else:
            print "Failed test 3, count(): Zero number of that item"
        
        ll = LinkedList()
        if ll.count(2) == 0:
            print "Passed test 4, count(): Empty list, zero items"
        else:
            print "Failed test 4, count(): Empty list, zero items"
            
        
        
                
                
        
         
        
            
            
if __name__ == "__main__": 
    main(3)

