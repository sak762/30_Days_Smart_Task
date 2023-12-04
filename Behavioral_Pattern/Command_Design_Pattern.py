from abc import ABC, abstractmethod


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Concrete Command 1
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

# Concrete Command 2
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

    def press_undo_button(self):
        self.command.undo()

# Client code
if __name__ == "__main__":
    # Create instances of Receiver (Light) and Concrete Commands
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Create an instance of Invoker (RemoteControl)
    remote = RemoteControl()

    # Set the command and press the button
    remote.set_command(light_on)
    remote.press_button()

    # Undo the command
    remote.press_undo_button()

    # Set a different command and press the button
    remote.set_command(light_off)
    remote.press_button()
