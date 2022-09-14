class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        try:
            return self.__items.pop(0)
        except IndexError:
            print("Empty queue")

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return f"Queue({self.__items})"
        
class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self,/):
        try:
            return self.__items.pop(-1)
        except IndexError:
            print("Empty stack")

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return f"Stack({self.__items})"