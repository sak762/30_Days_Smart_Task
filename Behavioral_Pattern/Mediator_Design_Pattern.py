from abc import ABC, abstractmethod

#Mediator interface 

class Mediator(ABC):
    def notify(self,sender,message):
        pass

#Concrete Mediator
class ChatroomMediator(Mediator):
    def __init__(self):
        self.participants = []
    def add_participant(self,participant):
        self.participants.append(participant)
    def notify(self,sender,message):
        for participant in self.participants:
            if participant !=sender:
               participant.receive(message)  

# Colleague interface
class Colleague(ABC):
    def __init__(self,mediator):
        self.mediator=mediator  

    def send(self,message):
        pass    
    def receive(self,message):
        pass
# Colleague interface
class Participant(Colleague):
    def __init__(self,name,mediator):
        super().__init__(mediator)
        self.name=name
    def send(self,message):
        print(f"{self.name} sends:{message}") 
        self.mediator.notify(self,message)

    def receive(self,message):
        print(f"{self.name} receives:{message}")


# Usage example 
if __name__ == "__main__":
    chatroom=ChatroomMediator()

    participant1= Participant("Alice",chatroom)
    participant2=Participant("Bob",chatroom)
    participant3=Participant("Charlie",chatroom)

    chatroom.add_participant(participant1)
    chatroom.add_participant(participant2)
    chatroom.add_participant(participant3)

    participant1.send("Hello,everyone!")
    participant2.send("Hi,Alice!")
    participant3.send("Nice to meet you all")

    '''In this example:

Mediator is an abstract class that defines the interface for communication between colleagues.
ChatroomMediator is a concrete mediator that manages the communication between participants.
Colleague is an abstract class representing participants in the communication.
Participant is a concrete colleague that communicates through the mediator.'''

'''In this example, when a participant sends a message,
the mediator (ChatroomMediator) notifies all other participants except the sender, simulating a chatroom-like communication. 
The output demonstrates how the messages are sent and received by the participants.'''