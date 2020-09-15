from math import comb, sqrt


class Probability:
    '''Add docstring'''

    def displaySummary(self) -> None:
        '''Display the summary statistics for a distribution'''

        print('Summary statistics of the distribution')
        print('-----')
        self.displayMean()
        self.displayVariance()
        self.displayStdDev()

    def getP(self, x: int) -> None:
        '''Displays the probability of a given value.

        What about infinite series?'''

        strX: str = str(x)
        strP: str = str(self.dictPMF[x])

        print('P(X = ' + strX + ') = ' + strP)

    def getF(self, x: int) -> None:
        '''Displays the probability of a given value'''


class Binomial(Probability):
    '''Add docstring'''

    def __init__(self, sampleSize: int, probability: float):
        '''Add docstring'''

        self.n: int = sampleSize
        self.p: float = probability
        self.q: float = 1 - probability
        self.generatePMF()
        self.generateCDF()
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()

    def generatePMF(self) -> None:
        '''Generates the pdf of the given distribution'''

        pmf: list = list()
        dictPMF: dict = dict()

        for i in range(0, (self.n) + 1):
            # calculate the number of combinations
            combinations: int = comb(self.n, i)
            # calculate p^x
            pX: float = self.p ** i
            # calculate q^{1-x}
            qNX: float = self.q ** (self.n - i)
            # calculate probability of i successes in n trials
            probability: float = combinations * pX * qNX
            # round the probability to 6dp
            roundProbability: float = round(probability, 6)
            # add to list
            elem: list = [i, (self.n - i), roundProbability]
            # add to PDF
            pmf.append(elem)
            # add to dictPMF
            dictPMF[i] = roundProbability

        self.pmf: list = pmf
        self.dictPMF: dict = dictPMF

    def displayPMF(self) -> None:
        '''Displays a table of the pmf from 0 to n'''

        print('x // (n - x) // p(x)')
        print('------------------------')
        for elem in self.pmf:
            print(elem[0], ' // ', elem[1], ' // ', elem[2])

    def generateCDF(self) -> None:
        '''Generates the cdf of the given distribution'''

        listCDF: list = list()
        cDF: float = 0
        reverseCDF: float = 1

        elemCDF: list = list()

        for elem in self.pmf:
            elemCDF: list = list()
            # add p(i) to CDF
            cDF = round(cDF + elem[2], 6)
            # subtract p(i) from reverseCDF
            reverseCDF = round(reverseCDF - elem[2], 6)
            elemCDF = [elem[0], cDF, reverseCDF]
            listCDF.append(elemCDF)

        self.cDF: list = listCDF

    def displayCDF(self) -> None:
        '''Displays a table of the cdf from 0 to n'''

        print('x // F(x) // 1 - (F(x)')
        print('------------------------')
        for elem in self.cDF:
            print(elem[0], ' // ', elem[1], ' // ', elem[2])

    def calculateMean(self) -> float:
        '''Calculate the E(X) of the binomial distribution'''

        self.mean = self.n * self.p

    def displayMean(self) -> None:
        '''Returns the E(X) of the binomial distribution'''

        print('E(X) =', self.mean)

    def calculateVariance(self) -> float:
        '''Calculate the V(X) of the binomial distribution'''

        self.var = self.n * self.p * self.q

    def displayVariance(self) -> None:
        '''Returns the V(X) of the binomial distribution'''

        print('V(X) =', round(self.var, 4))

    def calculateStdDev(self) -> None:
        '''Calculate the V(X) of the binomial distribution to 4dp'''

        self.stdDev = sqrt(self.var)

    def displayStdDev(self) -> None:
        '''Returns the S(X) of the binomial distribution to 4dp'''

        print('S(X) =', round(self.stdDev, 4))


class Geometric(Probability):
    '''Add docstring'''

    def __init__(self, sampleSize: int, probability: float):
        '''Add docstring'''

        self.n: int = sampleSize
        self.p: float = probability
        self.q: float = 1 - probability
        self.generatePMF()
        self.generateCDF()
        self.calculateMean()
        self.calculateVariance()
        self.calculateStdDev()

    def generatePMF(self) -> None:
        '''Generates the pdf of the given distribution'''

        pmf: list = list()
        dictPMF: dict = dict()

        for i in range(0, (self.n) + 1):
            # calculate the number of combinations
            combinations: int = comb(self.n, i)
            # calculate p^x
            pX: float = self.p ** i
            # calculate q^{1-x}
            qNX: float = self.q ** (self.n - i)
            # calculate probability of i successes in n trials
            probability: float = combinations * pX * qNX
            # round the probability to 6dp
            roundProbability: float = round(probability, 6)
            # add to list
            elem: list = [i, (self.n - i), roundProbability]
            # add to PDF
            pmf.append(elem)
            # add to dictPMF
            dictPMF[i] = roundProbability

        self.pmf: list = pmf
        self.dictPMF: dict = dictPMF

    def displayPMF(self) -> None:
        '''Displays a table of the pmf from 0 to n'''

        print('x // (n - x) // p(x)')
        print('------------------------')
        for elem in self.pmf:
            print(elem[0], ' // ', elem[1], ' // ', elem[2])

    def generateCDF(self) -> None:
        '''Generates the cdf of the given distribution'''

        listCDF: list = list()
        cDF: float = 0
        reverseCDF: float = 1

        elemCDF: list = list()

        for elem in self.pmf:
            elemCDF: list = list()
            # add p(i) to CDF
            cDF = round(cDF + elem[2], 6)
            # subtract p(i) from reverseCDF
            reverseCDF = round(reverseCDF - elem[2], 6)
            elemCDF = [elem[0], cDF, reverseCDF]
            listCDF.append(elemCDF)

        self.cDF: list = listCDF

    def displayCDF(self) -> None:
        '''Displays a table of the cdf from 0 to n'''

        print('x // F(x) // 1 - (F(x)')
        print('------------------------')
        for elem in self.cDF:
            print(elem[0], ' // ', elem[1], ' // ', elem[2])

    def calculateMean(self) -> float:
        '''Calculate the E(X) of the binomial distribution'''

        self.mean = self.n * self.p

    def displayMean(self) -> None:
        '''Returns the E(X) of the binomial distribution'''

        print('E(X) =', self.mean)

    def calculateVariance(self) -> float:
        '''Calculate the V(X) of the binomial distribution'''

        self.var = self.n * self.p * self.q

    def displayVariance(self) -> None:
        '''Returns the V(X) of the binomial distribution'''

        print('V(X) =', round(self.var, 4))

    def calculateStdDev(self) -> None:
        '''Calculate the V(X) of the binomial distribution to 4dp'''

        self.stdDev = sqrt(self.var)

    def displayStdDev(self) -> None:
        '''Returns the S(X) of the binomial distribution to 4dp'''

        print('S(X) =', round(self.stdDev, 4))
