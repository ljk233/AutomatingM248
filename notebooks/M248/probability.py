from math import comb, e, sqrt, factorial
from random import randrange
import seaborn as sns


def rollDie(n: int) -> list:
    '''
    Simulates rolling a dice n number of times.
    '''

    aListOfRolls: list = list()
    aListOfCounts: list = list()

    i: int = 0

    # roll the dice, append it to a list of rolls
    while i < n:
        aListOfRolls.append(randrange(1, 7))
        i = i + 1

    # count up the occurences of each die face
    aDieFace: int = 1
    while aDieFace <= 6:
        count = 0
        for roll in aListOfRolls:
            if aDieFace == roll:
                count = count + 1
        aListOfCounts.append(count)
        aDieFace = aDieFace + 1

    return aListOfCounts


def simulateDieRolls(n: int) -> None:
    '''
    Plots a list of random dice rolls
    '''

    # rolling 10 times
    rolls: list = rollDie(n)
    sns.barplot(x=[1, 2, 3, 4, 5, 6],
                y=rolls)


class Discrete:
    '''Superclass for discrete distribitions.'''

    def displaySummary(self) -> None:
        '''Display the summary statistics for a distribution.
        E(X), V(X), and S(X)'''

        print('Summary statistics of the distribution')
        print('--------------------------------------')
        self.displayMean()
        self.displayVariance()
        self.displayStdDev()

    def calculateP(self, x1: int, x2: int = None) -> None:
        '''Calculates the probability in a range.x1 must be defined.
        x2 is optional, default to None.
        If x1 >= x2, then return error.
        '''

        # check that the probability range is sensible
        # Provides an early return
        if x2 is not None and x1 >= x2:
            print("x1 must be less than x2.")
            print("Please define a sensible range.")
            return

        strX1: str = str(x1)
        p1: float = 0.0
        p2: float = 0.0
        p3: float = 0.0
        p4: float = 0.0
        p5: float = 0.0

        print('Various probability ranges of selection')
        print('---------------------------------------')

        if x2 is None:
            # Calculate P
            p1 = self.p(x1)
            p2 = self.calculateF(x1)
            p3 = self.calculateF(x1 - 1)
            p4 = 1 - self.calculateF(x1 - 1)
            p5 = 1 - self.calculateF(x1)

            # Cast to strings, round to 6dp
            strP1: str = str(round(p1, 6))
            strP2: str = str(round(p2, 6))
            strP3: str = str(round(p3, 6))
            strP4: str = str(round(p4, 6))
            strP5: str = str(round(p5, 6))

            # Print the probabilities
            print('P(X = ' + strX1 + ') = ' + strP1)
            print('P(X <= ' + strX1 + ') = ' + strP2)
            print('P(X < ' + strX1 + ') = ' + strP3)
            print('P(X >= ' + strX1 + ') = ' + strP4)
            print('P(X > ' + strX1 + ') = ' + strP5)

        else:
            # Calculate P
            p1 = self.calculateF(x2) - self.calculateF(x1 - 1)
            p2 = self.calculateF(x2) - self.calculateF(x1)
            p3 = self.calculateF(x2-1) - self.calculateF(x1-1)
            p4 = self.calculateF(x2-1) - self.calculateF(x1)

            # Cast to strings, round to 6dp
            strX2: str = str(x2)
            strP1: str = str(round(p1, 6))
            strP2: str = str(round(p2, 6))
            strP3: str = str(round(p3, 6))
            strP4: str = str(round(p4, 6))

            # Print the probabilities
            print('P(' + strX1 + ' <= X <= ' + strX2 + ') = ' + strP1)
            print('P(' + strX1 + ' < X <= ' + strX2 + ') = ' + strP2)
            print('P(' + strX1 + ' <= X < ' + strX2 + ') = ' + strP3)
            print('P(' + strX1 + ' < X < ' + strX2 + ') = ' + strP4)

    def displayMean(self) -> None:
        '''Prints the E(X) of the distribution to 6dp'''

        print('E(X) =', round(self.mean, 6))

    def displayVariance(self) -> None:
        '''Prints the V(X) of the distribution to 6dp'''

        print('V(X) =', round(self.var, 6))

    def displayStdDev(self) -> None:
        '''Prints the S(X) of the binomial distribution to 6dp'''

        print('S(X) =', round(self.stdDev, 6))

    def calculateF(self, x: int) -> float:
        '''Calculates F(x)'''

        i: int = 0
        F: float = 0

        while i <= x:
            F = F + self.p(i)
            i = i + 1

        return F


class B(Discrete):
    '''Generates a binomial distribution B(n, p).
    '''

    def __init__(self, sampleSize: int, probability: float) -> None:
        '''Constructor for B'''

        self.__n: int = sampleSize
        self.__p: float = probability
        self.__q: float = 1 - probability
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()
        self.displaySummary()

    def p(self, x: int) -> float:
        '''Calculates P(X)'''

        # calculate the number of combinations
        combinations: int = comb(self.__n, x)
        # calculate p^x
        pX: float = self.__p ** x
        # calculate q^{1-x}
        qNX: float = self.__q ** (self.__n - x)
        # calculate probability of i successes in n trials
        probability: float = combinations * pX * qNX

        return probability

    def calculateMean(self) -> None:
        '''Calculate the E(X)'''

        self.mean = self.__n * self.__p

    def calculateVariance(self) -> None:
        '''Calculate the V(X)'''

        self.var = self.__n * self.__p * self.__q

    def calculateStdDev(self) -> None:
        '''Calculate the S(X)'''

        self.stdDev = sqrt(self.var)


class G(Discrete):
    '''Generates a geometric distribution G(p).
    '''

    def __init__(self, p: float) -> None:
        '''Constructor for the G'''

        self.__p: float = p
        self.__q: float = 1 - p
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()
        self.displaySummary()

    def p(self, x: int) -> float:
        '''Calculates P(X)'''

        return self.__q ** (x - 1) * self.__p

    def calculateF(self, x: int) -> float:
        '''Calculates F(X).
        Override method due to Discrete CalculateF not working.
        (PDF fails when X=0).
        '''

        return 1 - (1 - self.__p) ** x

    def calculateMean(self) -> None:
        '''Calculate the E(X)'''

        self.mean = self.__p ** (-1)

    def calculateVariance(self) -> None:
        '''Calculate the V(X)'''

        self.var = self.__q / (self.__p ** 2)

    def calculateStdDev(self) -> None:
        '''Calculate the S(X)'''

        self.stdDev = sqrt(self.var)


class Poisson(Discrete):
    '''Generates a Poisson distribution Poisson(mu)
    '''

    def __init__(self, mu: float) -> None:
        '''Constructor for Poisson'''

        self.__mu: float = mu
        self.__negMu: float = -1 * mu
        self.__constant: float = e ** (self.__negMu)
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()
        self.displaySummary()

    def p(self, x: int) -> float:
        '''Calculates P(X)'''

        p: float = 0

        p = self.__constant * ((self.__mu ** x) / factorial(x))

        return p

    def calculateMean(self) -> None:
        '''Calculate the E(X)'''

        self.mean = self.__mu

    def calculateVariance(self) -> None:
        '''Calculate the V(X)'''

        self.var = self.__mu

    def calculateStdDev(self) -> None:
        '''Calculate the S(X)'''

        self.stdDev = sqrt(self.var)


class DiscreteUniform(Discrete):
    '''Generates a discrete uniform distribution with range m to n
    '''

    def __init__(self, m: int, n: int) -> None:
        '''Constructor for DiscreteUniform'''

        self.__m: int = m
        self.__n: int = n
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()
        self.displaySummary()

    def p(self, x: int) -> float:
        '''Calculates P(X)'''

        return (self.__n - self.__m + 1) ** (-1)

    def calculateMean(self) -> None:
        '''Calculate the E(X)'''

        self.mean = 0.5 * (self.__m + self.__n)

    def calculateVariance(self) -> None:
        '''Calculate the V(X)'''

        self.var = ((1 / 12)
                    * ((self.__n - self.__m)
                    * (self.__n - self.__m + 2)))

    def calculateStdDev(self) -> None:
        '''Calculate the S(X)'''

        self.stdDev = sqrt(self.var)


class M():
    '''
    Generates an exponential distribution with parameter 'lambda' as L.
    '''

    def __init__(self, L: float) -> None:
        '''Constructor for the Exponential class'''

        self.__L = L
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()
        self.displaySummary()

    def displaySummary(self) -> None:
        '''Display the summary statistics for a distribution'''

        print('Summary statistics of the distribution')
        print('--------------------------------------')
        self.displayMean()
        self.displayVariance()
        self.displayStdDev()

    def calculateP(self, x1: float, x2: float = None) -> None:
        '''Calculates the probability in a range.
        x1 must be defined. x2 is optional.
        If just x1:
          return <=,>=
        Else:
          return x1 <= X <= x2
        '''

        strX1: str = str(round(x1, 6))
        p1: float = 0.0
        p2: float = 0.0

        print('Probability range of selection')
        print('---------------------------------------')

        if x2 is None:
            p1 = self.calculateF(x1)
            strP1: str = str(round(p1, 6))
            print('P(X <= ' + strX1 + ') = ' + strP1)

            p2 = 1 - self.calculateF(x1)
            strP2: str = str(round(p2, 6))
            print('P(X >= ' + strX1 + ') = ' + strP2)

        else:
            strX2: str = str(round(x2, 6))

            p1 = self.calculateF(x2) - self.calculateF(x1)
            strP1: str = str(round(p1, 6))
            print('P(' + strX1 + ' <= X <= ' + strX2 + ') = ' + strP1)

    def displayMean(self) -> None:
        '''Prints the E(X) of the distribution to 6dp'''

        print('E(X) =', round(self.mean, 6))

    def displayVariance(self) -> None:
        '''Prints the V(X) of the distribution to 6dp'''

        print('V(X) =', round(self.var, 6))

    def displayStdDev(self) -> None:
        '''Prints the S(X) of the distribution to 6dp'''

        print('S(X) =', round(self.stdDev, 6))

    def p(self, x: int) -> float:
        '''Calculates P(X)'''

        p: float = 0

        p = self.__L * e ** (-1 * self.__L * x)

        return p

    def calculateF(self, x: float) -> float:
        '''Calculates F(X)'''

        F: float = 0

        F = 1 - e ** (-1 * self.__L * x)

        return F

    def calculateMean(self) -> None:
        '''Calculate the E(X)'''

        self.mean = 1 / self.__L

    def calculateVariance(self) -> None:
        '''Calculate the V(X)'''

        self.var = 1 / (self.__L ** 2)

    def calculateStdDev(self) -> None:
        '''Calculate the S(X) of the distribution'''

        self.stdDev = 1 / self.__L
