# Circular_Linked_List
A circular list is a special case of a linked list. It is a list where the endpoints are connected. That is, the last node in the list points back to the first node. Circular lists can be based on both singly and doubly linked lists. In the case of a doubly linked circular list, the first node also needs to point to the last node. A header node is placed as the first node of the circular list.
Basic operations
•	insert − Inserts an element at the start of the list.
The new node must be pointed at itself, then the list’s head must be pointed at the new node.
•	delete − Deletes an element from the start of the list.
•	display − Displays the list.

Code
The code was implemented using circular linked list. Student class has objects name, ID and GPA. The user can delete student, reverse the list of students. The all methodes were used in main function 
Complexity
The complexity of insert and delete functions
 in the worst case is O(n). However if elements needs to be inserted at front (just before the node pointed by head), can be done in O(1)
