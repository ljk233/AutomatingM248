
class Account():
    '''
    Account class used to model simple bank accounts, allowing money
    to be credited to, and debited and transfered from, an account.

    Adapted from M250_Account

    @author M250 Module Team
    @version 1.0
    '''

    def __init__(self,
                 holderName: str = None,
                 accountNumber: str = None,
                 anAmmount: float = 0.0) -> None:
        '''
        Constructor for objects of class Account.
        '''

        self.holder: str = holderName
        self.number: str = accountNumber
        self.balance: float = anAmmount

    def getBalance(self) -> float:
        '''
        Returns the balance of the receiver
        '''

        return self.balance

    def setBalance(self, anAmmount: float) -> None:
        '''
        Set the balance of the receiver to the value of the argument anAmount
        '''

        self.balance = anAmmount

    def getHolder(self) -> str:
        '''
        Returns the holder of the receiver
        '''

        return self.holder

    def setHolder(self, accountHolder: str) -> None:
        '''
        Set the holder of the receiver to the value of the argument
        accountHolder
        '''

        self.holder = accountHolder

    def getNumber(self) -> str:
        '''
        Returns the number of the receiver
        '''

        return self.number

    def setNumber(self, accountNumber: str) -> None:
        '''
        Set the number of the receiver to the value of the argument
        accountNumber
        '''

        self.number = accountNumber

    def credit(self, anAmmount: float) -> None:
        '''
        Credits the receiver with the value of the argument anAmount.

        Example of object sending message to itself.
        '''

        self.setBalance(self.getBalance() + anAmmount)

    def debit(self, anAmmount: float) -> bool:
        '''
        If the balance of the receiver is equal to or greater than the argument
        anAmount, the balance of the receiver is debited by the argument
        anAmount and the method returns true.

        If the balance of the receiver is not equal to or greater than the
        argument anAmount, the method simply returns false.

        Example of object sending message to itself.
        Example of a selection condition.
        '''

        # if the account balance greater or equal to ammount
        if self.getBalance() >= anAmmount:
            self.setBalance(self.getBalance() - anAmmount)
            return True

        else:
            return False

    def transfer(self, toAccount: object, anAmmount: float) -> bool:
        '''
        If the balance of the receiver is equal to or greater than the
        argument anAmount, the balance of the receiver is debited by the
        argument anAmount. The argument toAccount is then credited by the
        argument anAmount and the method returns true.

        If the balance of the receiver is not equal to or greater than the
        argument anAmount, the method simply returns false.

        Example of object collaboration.
        '''

        if self.debit(anAmmount):
            toAccount.credit(anAmmount)
            return True

        else:
            return False
