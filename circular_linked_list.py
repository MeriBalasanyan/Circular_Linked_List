class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Student:
    def __init__(self, name, ID, GPA):
        self.name = name
        self.ID = ID
        self.GPA = GPA

class CircularLinkedList:
    def __init__(self):
        self.__head = None

    def find(self, data):
        temp = self.__head
        while temp.data is not data:
            temp = temp.next
        return temp

    def display(self):
        printval = self.__head
        while printval is not None:
            print ("name:", printval.data.name, "ID:", printval.data.ID, "GPA:", printval.data.GPA)
            printval = printval.next
            if printval == self.__head:
                break

        print "----------"

    def append(self, newdata):
        newStudent = Student(newdata)
        temp = self.__head
        newStudent.next = self.__head
        if self.__head is  None:
            newStudent.next = newStudent
            self.__head = newStudent
        else:
            while (temp.next != self.__head):
                temp = temp.next
            temp.next = newStudent

    def appendAfter(self, prevStudent, newStudent):
        new_Student = Student(newStudent)
        prev_Student = self.find(prevStudent)

        if prev_Student is None:
            print("This student is not in the list")


        new_Student.next = prev_Student.next
        prev_Student.next = new_Student

    def delete(self, name, ID):
        temp = self.__head
        while temp is not None and temp.next.data != name and temp.Id != ID:
            temp = temp.next
        temp.next = temp.next.next

    def reverse(self):
        prev = None
        temp = self.__head
        while temp is not None:
            next = temp.next

            temp.next = prev
            prev = temp

            temp = next
        self.__head = prev

    def changehead(self, newhead):
        new_head = self.find(newhead)
        self.__head = new_head

def main():
    student = CircularLinkedList()
    st1 = Student("meri","111","3.0")
    student.append(st1)
    student.reverse()

    student.appendAfter()
    student.delete()
    student.changehead()
    student.reverse()
    student.display()

main()