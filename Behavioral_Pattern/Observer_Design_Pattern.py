from abc import ABC, abstractmethod


# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


# Subject
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")


# Concrete Subject
class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        self.notify_observers(f"State updated to {state}")


# Usage example
if __name__ == "__main__":
    subject = ConcreteSubject("Initial State")

    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    subject.add_observer(observer1)
    subject.add_observer(observer2)

    subject.set_state("New State 1")
    subject.set_state("New State 2")

    subject.remove_observer(observer1)

    subject.set_state("Final State")

'''In this example:

Originator is the object whose state needs to be saved.
Memento is the object that stores the state of the Originator.
Caretaker is responsible for keeping track of multiple states of the Originator.
The Originator can save its state to a Memento and later restore its state from a Memento.
The Caretaker keeps track of multiple states using a list of Mementos.'''