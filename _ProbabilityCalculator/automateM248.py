from math import comb, e, sqrt, factorial


class Discrete:
    '''Add docstring'''

    def displaySummary(self) -> None:
        '''Display the summary statistics for a distribution'''

        print('Summary statistics of the distribution')
        print('--------------------------------------')
        self.displayMean()
        self.displayVariance()
        self.displayStdDev()

    def calculateProbability(self, x1: int, x2: int = None) -> None:
        '''Calculates the probability in a range.
        x1 must be defined. x2 is optional.
        If just x1:
          return =, <=, <, >=, >=
        Else:
          return x1 <= X <= x2, x1 <= X < x2, x1 < X <= x2, x1 < X < x2
        '''

        strX1: str = str(x1)
        p1: float = 0.0
        p2: float = 0.0
        p3: float = 0.0
        p4: float = 0.0
        p5: float = 0.0

        print('Various probability ranges of selection')
        print('---------------------------------------')

        if x2 is None:
            p1 = self.calculateP(x1)
            strP1: str = str(round(p1, 6))
            print('P(X = ' + strX1 + ') = ' + strP1)

            p2 = self.calculateF(x1)
            strP2: str = str(round(p2, 6))
            print('P(X <= ' + strX1 + ') = ' + strP2)

            p3 = self.calculateF(x1 - 1)
            strP3: str = str(round(p3, 6))
            print('P(X < ' + strX1 + ') = ' + strP3)

            p4 = 1 - self.calculateF(x1 - 1)
            strP4: str = str(round(p4, 6))
            print('P(X >= ' + strX1 + ') = ' + strP4)

            p5 = 1 - self.calculateF(x1)
            strP5: str = str(round(p5, 6))
            print('P(X > ' + strX1 + ') = ' + strP5)

            # 6. P(x1 <= X <= x2)
        else:
            strX2: str = str(x2)

            p1 = self.calculateF(x2) - self.calculateF(x1 - 1)
            strP1: str = str(round(p1, 6))
            print('P(' + strX1 + ' <= X <= ' + strX2 + ') = ' + strP1)

            p2 = self.calculateF(x2) - self.calculateF(x1)
            strP2: str = str(round(p2, 6))
            print('P(' + strX1 + ' < X <= ' + strX2 + ') = ' + strP2)

            p3 = self.calculateF(x2-1) - self.calculateF(x1-1)
            strP3: str = str(round(p3, 6))
            print('P(' + strX1 + ' <= X < ' + strX2 + ') = ' + strP3)

            p4: float = self.calculateF(x2-1) - self.calculateF(x1)
            strP4: str = str(round(p4, 6))
            print('P(' + strX1 + ' < X < ' + strX2 + ') = ' + strP4)

    def displayMean(self) -> None:
        '''Prints the E(X) of the distribution to 4dp'''

        print('E(X) =', round(self.mean, 4))

    def displayVariance(self) -> None:
        '''Prints the V(X) of the distribution to 4dp'''

        print('V(X) =', round(self.var, 4))

    def displayStdDev(self) -> None:
        '''Prints the S(X) of the binomial distribution to 4dp'''

        print('S(X) =', round(self.stdDev, 4))

    def calculateF(self, x: int) -> float:
        '''Calculates F(X)'''

        i: int = 0
        F: float = 0

        while i <= x:
            F = F + self.calculateP(i)
            i = i + 1

        return F


class Binomial(Discrete):
    '''Generates a binomial distribution B(n, p).
    '''

    def __init__(self, sampleSize: int, probability: float) -> None:
        '''Add docstring'''

        self.__n: int = sampleSize
        self.__p: float = probability
        self.__q: float = 1 - probability
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()
        self.displaySummary()

    def calculateP(self, x: int) -> float:
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
        '''Calculate the E(X) of the binomial distribution'''

        self.mean = self.__n * self.__p

    def calculateVariance(self) -> None:
        '''Calculate the V(X) of the binomial distribution'''

        self.var = self.__n * self.__p * self.__q

    def calculateStdDev(self) -> None:
        '''Calculate the S(X) of the binomial distribution to 4dp'''

        self.stdDev = sqrt(self.var)


class Geometric(Discrete):
    '''Generates a geometric distribution G(p).
    '''

    def __init__(self, probability: float) -> None:
        '''Add docstring'''

        self.__p: float = probability
        self.__q: float = 1 - probability
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()
        self.displaySummary()

    def calculateP(self, x: int) -> float:
        '''Calculates P(X)'''

        return self.__q ** (x - 1) * self.__p

    def calculateF(self, x: int) -> float:
        '''Calculates F(X).
        Override function due to class CalculateF not working.
        PDF fails when X=0.
        '''

        return 1 - (1 - self.__p) ** x

    def calculateMean(self) -> None:
        '''Calculate the E(X) of the geometric distribution'''

        self.mean = self.__p ** (-1)

    def calculateVariance(self) -> None:
        '''Calculate the V(X) of the geometric distribution'''

        self.var = self.__q / (self.__p ** 2)

    def calculateStdDev(self) -> None:
        '''Calculate the S(X) of the geometric distribution'''

        self.stdDev = sqrt(self.var)


class Poisson(Discrete):
    '''Generates a Poisson distribution Poisson(mu)
    '''

    def __init__(self, mu: float) -> None:
        '''Add docstring'''

        self.__mu: float = mu
        self.__negMu: float = -1 * mu
        self.__constant: float = e ** (self.__negMu)
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()
        self.displaySummary()

    def calculateP(self, x: int) -> float:
        '''Calculates P(X)'''

        probability: float = 0

        probability = self.__constant * ((self.__mu ** x) / factorial(x))

        return probability

    def calculateMean(self) -> None:
        '''Calculate the E(X) of the geometric distribution'''

        self.mean = self.__mu

    def calculateVariance(self) -> None:
        '''Calculate the V(X) of the geometric distribution'''

        self.var = self.__mu

    def calculateStdDev(self) -> None:
        '''Calculate the S(X) of the geometric distribution'''

        self.stdDev = sqrt(self.var)


class DiscreteUniform(Discrete):
    '''Generates a discrete uniform distribution with range m to n
    arguments:
      m, lower bound, integer
      n, upper bound, integer
    '''

    def __init__(self, m: int, n: int) -> None:
        '''Add docstring'''

        self.__m: int = m
        self.__n: int = n
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()
        self.displaySummary()

    def calculateP(self, x: int) -> float:
        '''Calculates P(X)'''

        return 1 / (self.__n - self.__m + 1)

    def calculateMean(self) -> None:
        '''Calculate the E(X) of the geometric distribution'''

        self.mean = 0.5 * (self.__m + self.__n)

    def calculateVariance(self) -> None:
        '''Calculate the V(X) of the geometric distribution'''

        self.var = ((1 / 12)
                    * ((self.__n - self.__m) * (self.__n - self.__m + 2)))

    def calculateStdDev(self) -> None:
        '''Calculate the S(X) of the distribution'''

        self.stdDev = sqrt(self.var)


class Exponential():
    '''
    Generates an exponential distribution with parameter 'lambda' as L.
    '''

    def __init__(self, L: float) -> None:
        '''Constructor for the Exponential class'''

        self.L = L
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

    def calculateProbability(self, x1: float, x2: float = None) -> None:
        '''Calculates the probability in a range.
        x1 must be defined. x2 is optional.
        If just x1:
          return =, <=, <, >=, >=
        Else:
          return x1 <= X <= x2, x1 <= X < x2, x1 < X <= x2, x1 < X < x2
        '''

        strX1: str = str(round(x1, 4))
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
            strX2: str = str(round(x2, 4))

            p1 = self.calculateF(x2) - self.calculateF(x1)
            strP1: str = str(round(p1, 6))
            print('P(' + strX1 + ' <= X <= ' + strX2 + ') = ' + strP1)

    def displayMean(self) -> None:
        '''Prints the E(X) of the distribution to 4dp'''

        print('E(X) =', round(self.mean, 4))

    def displayVariance(self) -> None:
        '''Prints the V(X) of the distribution to 4dp'''

        print('V(X) =', round(self.var, 4))

    def displayStdDev(self) -> None:
        '''Prints the S(X) of the binomial distribution to 4dp'''

        print('S(X) =', round(self.stdDev, 4))

    def calculateP(self, x: int) -> float:
        '''Calculates P(X)'''

        probability: float = 0

        probability = self.L * e ** (-1 * self.L * x)

        return probability

    def calculateF(self, x: float) -> float:
        '''Calculates F(X)'''

        F: float = 0

        F = 1 - e ** (-1 * self.L * x)

        return F

    def calculateMean(self) -> None:
        '''Calculate the E(X)'''

        self.mean = 1 / self.L

    def calculateVariance(self) -> None:
        '''Calculate the V(X)'''

        self.var = 1 / (self.L ** 2)

    def calculateStdDev(self) -> None:
        '''Calculate the S(X) of the distribution'''

        self.stdDev = 1 / self.L
