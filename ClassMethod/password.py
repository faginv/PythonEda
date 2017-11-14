# I have to build a Password class which has a method that takes various numbers
# of functions as validation. Each function should be called with the stored
# password and if any of them return False, the method also should return False.
# Otherwise it should return True. How can I do that?

class Password:

    def validationOne(self, val):
        if val == 'valueOne':
            return True
        else:
            return False

    def validationTwo(self, val):
        if val == 'valueTwo':
            return True
        else:
            return False

    def validationThree(self, val):
        if val == 'valueThree':
            return True
        else:
            return False

    def checkPassword(self, valOne, valTwo, valThree):

        self.valOne = self.validationOne(valOne)
        self.valTwo = self.validationTwo(valTwo)
        self.valThree = self.validationThree(valThree)

        if(self.valOne and self.valTwo and self.valThree):
            return True
        else:
            return False

pw = Password()

result = pw.checkPassword('valueOnie', 'valueTwo', 'valueThree')

print(result)
