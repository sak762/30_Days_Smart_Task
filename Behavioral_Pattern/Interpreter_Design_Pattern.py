#Step 1: Define the Abstract Expression
from abc import ABC, abstractmethod

# Abstract Expression

class Expression(ABC):
    def interpret(self,context):
        pass
#Step 2: Implement Terminal Expressions
class VariableExpression(Expression):
    def __init__(self,name):
        self.name=name
    def interpret(self,context):
        return context.get_variable_value(self.name)
    
#Step 3: Implement Non-terminal Expressions  
class AddExpression(Expression):
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def interpret(self,context):
        return self.left.interpret(context)+self.right.interpret(context)
class SubtractExpression(Expression):
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def interpret(self,context):
        return self.left.interpret(context)-self.right.interpret(context)

#Step 4: Create a Context
class Context:
    def __init__(self):
        self.variables={}
    def set_variable_value(self,variable,value):
        self.variables[variable]=value
    def get_variable_value(self,variable):
        return self.variables.get(variable,0)
    
#Step 5: Client Code
if __name__ == "__main__":
    context = Context()
    context.set_variable_value("x",5)
    context.set_variable_value("y",10)

    #Create expression 
    expression = AddExpression(VariableExpression("x"),SubtractExpression(VariableExpression("y"),VariableExpression("x")))
    #Interpret the expression
    result=expression.interpret(context)
    print("Result:",result)

'''Given the variable values set in the context:

x is set to 5.
y is set to 10.
Let's substitute these values into the expression:

python
Copy code
result = 5 + (10 - 5)
Now, perform the calculations:

python
Copy code
result = 5 + 5
result = 10
So, the result of the expression is 10. The output of the code will be:

makefile
Copy code
Result: 10'''

'''In this example:

Expression is the abstract expression class that declares the interpret method.
VariableExpression is a terminal expression representing a variable.
AddExpression and SubtractExpression are non-terminal expressions representing addition and subtraction operations.
Context holds the variables and their values.
The client code sets variable values in the context and creates an expression (AddExpression). The interpreter then interprets the expression,
taking into account the variable values, and produces a result.'''