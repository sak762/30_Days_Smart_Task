# Originator: The object whose state needs to be saved
class Originator:
    def __init__(self,state):
        self.state=state
    def set_state(self,state):
        print(f"Setting state to:{state}")
        self.state=state
    def save_to_memento(self):
        print("Saving state to Memento")
        return Memento(self.state) 
    def restore_from_memento(self,memento):
        print("Restoring state from Memento")
        self.state=memento.get_state()
    def __str__(self) :
        return f"Current State:{self.state}"
# Memento: The object that stores the state of the Originator
class Memento:
    def __init__(self,state):
        self.state=state
    def get_state(self):
        return self.state

# Caretaker: The object that keeps track of multiple states of the Originator
class Caretaker:
    def __init__(self):
        self.mementos=[]
    def add_memento(self,memento):
        print("Adding Memento to the list")
        self.mementos.append(memento)
    def get_memento(self,index):
        print(f"Getting Memento at index{index}")
        return self.mementos[index]

# Usage example
if __name__ =="__main__":
    originator = Originator("State1")
    caretaker=Caretaker()
    print(originator)

    memento1 = originator.save_to_memento()
    caretaker.add_memento(memento1)

    originator.set_state("State2")
    print(originator)  

    memento2= originator.save_to_memento()
    caretaker.add_memento(memento2)

    originator.set_state("State3")
    print(originator)                      
    
# Restore to the previous state    

memento_to_restore=caretaker.get_memento(1)
originator.restore_from_memento(memento_to_restore)
print(originator)
'''The Originator can save its state to a Memento and later restore its state from a Memento.
The Caretaker keeps track of multiple states using a list of Mementos.'''