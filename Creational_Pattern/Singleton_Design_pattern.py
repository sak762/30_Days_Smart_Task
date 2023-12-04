class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Additional initialization can be done here
        return cls._instance

# Usage
if __name__ == "__main__":
    # Creating instances of Singleton
    singleton_instance1 = Singleton()
    singleton_instance2 = Singleton()

    # Both instances refer to the same object
    print(singleton_instance1 is singleton_instance2)  # Output: True

'''In this example, the __new__ method ensures that only one instance of the Singleton class is created. 
When you create multiple instances (singleton_instance1 and singleton_instance2),
they both refer to the same object due to the singleton pattern.'''