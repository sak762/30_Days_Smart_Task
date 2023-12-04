#Step 1: Define the Iterator Interface
from abc import ABC, abstractmethod


class Iterator(ABC):
    def has_next(self):
        pass
    def next(self):
        pass

#Step 2: Implement the Concrete Iterator        
class ConcreteIterator(Iterator):
    def __init__(self,collection):
        self.collection=collection
        self.index=0
    def has_next(self):
        return self.index<len(self.collection)

    def next(self):
      if self.has_next():
        item = self.collection[self.index]
        self.index +=1
        return item
      else:
          raise StopIteration
      
#Step 3: Define the Aggregate Interface
class Aggregate(ABC):
    def create_interator(self):
        pass

#Step 4: Implement the Concrete Aggregate
class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.items=[]
    def add_item(self,item):
        self.items.append(item)
    def create_iterator(self):
        return ConcreteIterator(self.items)

#Step 5: Client Code

if __name__ =="__main__":
    aggregate=ConcreteAggregate()

    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

# Create an iterator for the aggregate
iterator = aggregate.create_iterator()

while iterator.has_next():
    item= iterator.next()
    print(item)

"""In this example:

Iterator Interface: Iterator declares the interface for the iterator with has_next and next methods.

Concrete Iterator: ConcreteIterator implements the iterator interface.
It keeps track of the current index while traversing the elements of the collection.

Aggregate Interface: Aggregate declares the interface for creating an iterator with the create_iterator method.

Concrete Aggregate: ConcreteAggregate implements the aggregate interface.
It maintains a collection of items and provides a method to create an iterator for that collection.

Client Code: The client code creates a concrete aggregate, adds items to it,
creates an iterator for the aggregate, and iterates over the elements using the iterator."""