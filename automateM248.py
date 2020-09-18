from math import comb, exp, sqrt, factorial


class Probability:
    '''Add docstring'''

    def displaySummary(self) -> None:
        '''Display the summary statistics for a distribution'''

        print('Summary statistics of the distribution')
        print('--------------------------------------')
        self.displayMean()
        self.displayVariance()
        self.displayStdDev()

    def getP(self, x: int) -> None:
        '''Displays the probability of a given value.'''

        strX: str = str(x)
        strP: str = str(self.dictPMF[x])

        print('P(X = ' + strX + ') = ' + strP)

    def getF(self, x: int) -> None:
        '''Displays the F(X)'''

        strX: str = str(x)
        strP: str = str(self.dictCDF[x])

        print('F(' + strX + ') = ' + strP)

    def displayMean(self) -> None:
        '''Prints the E(X) of the distribution to 4dp'''

        print('E(X) =', self.mean)

    def displayVariance(self) -> None:
        '''Prints the V(X) of the distribution to 4dp'''

        print('V(X) =', round(self.var, 4))

    def displayStdDev(self) -> None:
        '''Prints the S(X) of the binomial distribution to 4dp'''

        print('S(X) =', round(self.stdDev, 4))

    def calculateProbability(self) -> None:
        '''Calculates the probability in a range'''

        form: str = 'z'

        while form != '0':
            form = input('What is the form of the probability: ')

            x1: int = 0
            x2: int = 0

            # case analysis
            # 1. P(X = x)
            if form == '1':
                # What is X_1?
                x1 = int(input('What is x?: '))
                p1 = self._calculateP(x1)

                # convert numerical values to strings for printing
                strX1 = str(x1)
                strP1 = str(round(p1, 6))

                # print answers
                print('P(X = ' + strX1 + ') = ' + strP1)

                # end loop
                form = '0'

            # 2. P(X <= x)
            elif form == '2':
                # What is X_1?
                x1 = int(input('What is x?: '))
                F1 = self._calculateF(x1)

                # convert numerical values to strings for printing
                strX1 = str(x1)
                strF1 = str(round(F1, 6))

                # print answers
                print('P(X <= ' + strX1 + ') = ' + strF1)
                form = '0'

            # 3. P(X < x)
            elif form == '3':
                # What is X_1?
                x1 = int(input('What is x?: '))

                # decrement x1 by 1
                x1_1 = x1 - 1
                F1 = self._calculateF(x1_1)

                # convert numerical values to strings for printing
                strX1 = str(x1)
                strF1 = str(round(F1, 6))

                # print answers
                print('P(X < ' + strX1 + ') = ' + strF1)
                form = '0'

            # 4. P(X >= x)
            elif form == '4':
                # What is X_1?
                x1 = int(input('What is x?: '))

                # transform to F(X)
                x1_1 = x1 - 1
                F1 = 1 - self._calculateF(x1_1)

                # convert numerical values to strings for printing
                strX1 = str(x1)
                strF1 = str(round(F1, 6))

                # print answers
                print('P(X >= ' + strX1 + ') = ' + strF1)

                form = '0'

            # 5. P(X > x)
            elif form == '5':
                # What is X_1?
                x1 = int(input('What is x?: '))

                # transform to F(X)
                F1 = 1 - self._calculateF(x1)

                # convert numerical values to strings for printing
                strX1 = str(x1)
                strF1 = str(round(F1, 6))

                # print answers
                print('P(X > ' + strX1 + ') = ' + strF1)
                form = '0'

            # 6. P(x1 <= X <= x2)
            elif form == '6':
                # What is X_1?
                x1 = int(input('What is x_1?: '))
                F1 = self._calculateF(x1)
                strX1 = str(x1)

                # What is X_2?
                x2 = int(input('What is x_2?: '))
                F2 = self._calculateF(x2)
                strX2 = str(x2)

                # calculate probability
                F: float = F2 - F1
                roundF: float = round(F, 6)
                strF = str(roundF)

                # print answers
                print('P(' + strX1 + ' <= X <= ' + strX2 + ') = ' + strF)
                form = '0'

            # 7. P(x1 < X <= x2)
            elif form == '7':
                # What is X_1?
                x1 = int(input('What is x?: '))
                F1 = self._calculateF(x1)
                strX1 = str(x1)

                # What is X_2?
                x2 = int(input('What is x_2?: '))
                F2 = self._calculateF(x2)
                strX2 = str(x2)

                # calculate probability
                F: float = F2 - F1
                roundF: float = round(F, 6)
                strF = str(roundF)

                # print answers
                print('P(' + strX1 + ' < X <= ' + strX2 + ') = ' + strF)
                form = '0'

            # 8. P(x1 <= X < x2)
            elif form == '8':
                # What is X_1?
                x1 = int(input('What is x?: '))
                #
                F1 = self._calculateF(x1-1)
                strX1 = str(x1)

                # What is X_2?
                x2 = int(input('What is x_2?: '))
                F2 = self._calculateF(x2-1)
                strX2 = str(x2)

                # calculate probability
                F: float = F2 - F1
                roundF: float = round(F, 6)
                strF = str(roundF)

                # print answers
                print('P(' + strX1 + ' <= X < ' + strX2 + ') = ' + strF)
                form = '0'

            # 9. P(x1 < X < x2)
            elif form == '9':
                # What is X_1?
                x1 = int(input('What is x?: '))
                # P(X > x1) == 1 - F(X <= x1)
                F1 = self._calculateF(x1)
                strX1 = str(x1)

                # What is X_2?
                x2 = int(input('What is x_2?: '))
                # P(X < x2) == F(X <= (x2-1))
                F2 = self._calculateF(x2-1)
                strX2 = str(x2)

                # calculate probability
                F: float = F2 - F1
                roundF: float = round(F, 6)
                strF = str(roundF)

                # print answers
                print('P(' + strX1 + ' < X < ' + strX2 + ') = ' + strF)

                form = '0'

            # 0. quit
            elif form == '0':
                # quit loop
                form = '0'

            # else
            else:
                # do someting
                print('Command not recongised')

    def toString(x: int, p: float) -> dict:
        '''Returns a dict of strings'''

        dictString: dict = dict()

        dictString[x] = str(x)
        dictString[p] = str(round(p, 6))


class Binomial(Probability):
    '''Generates a binomial distribution B(n, p).'''

    def __init__(self, sampleSize: int, probability: float):
        '''Add docstring'''

        self.n: int = sampleSize
        self.p: float = probability
        self.q: float = 1 - probability
        self._calculateMean()
        self._calculateVariance()
        self._calculateStdDev()

    def _calculateP(self, x: int) -> float:
        '''Calculates P(X)'''

        # calculate the number of combinations
        combinations: int = comb(self.n, x)
        # calculate p^x
        pX: float = self.p ** x
        # calculate q^{1-x}
        qNX: float = self.q ** (self.n - x)
        # calculate probability of i successes in n trials
        probability: float = combinations * pX * qNX

        return probability

    def _calculateF(self, x: int) -> float:
        '''Calculates F(X)'''

        i: int = 0
        F_x: float = 0

        while i <= x:
            p_i = self._calculateP(i)
            F_x = F_x + p_i
            i = i + 1

        return F_x

    def _calculateMean(self) -> float:
        '''Calculate the E(X) of the binomial distribution'''

        self.mean = self.n * self.p

    def _calculateVariance(self) -> float:
        '''Calculate the V(X) of the binomial distribution'''

        self.var = self.n * self.p * self.q

    def _calculateStdDev(self) -> None:
        '''Calculate the V(X) of the binomial distribution to 4dp'''

        self.stdDev = sqrt(self.var)


class Geometric(Probability):
    '''Add docstring'''

    def __init__(self, probability: float):
        '''Add docstring'''

        self.p: float = probability
        self.q: float = 1 - probability
        self._calculateMean()
        self._calculateVariance()
        self._calculateStdDev()

    def _calculateP(self, x: int) -> float:
        '''Calculates P(X)'''

        probability: float = 0

        probability = self.q ** (x - 1) * self.p

        return probability

    def _calculateF(self, x: int) -> float:
        '''Calculates F(X)'''

        F_x: float = 0

        F_x = 1 - (self.q ** x)

        return F_x

    def _calculateMean(self) -> float:
        '''Calculate the E(X) of the geometric distribution'''

        self.mean = self.p ** (-1)

    def _calculateVariance(self) -> float:
        '''Calculate the V(X) of the geometric distribution'''

        self.var = self.q / (self.p ** 2)

    def _calculateStdDev(self) -> None:
        '''Calculate the S(X) of the geometric distribution'''

        self.stdDev = sqrt(self.var)


class Poisson(Probability):
    '''Add docstring'''

    def __init__(self, mu: float) -> None:
        '''Add docstring'''

        self.mu: float = mu
        self.negMu: float = -1 * mu
        self.constant: float = exp(self.negMu)
        self._calculateMean()
        self._calculateVariance()
        self._calculateStdDev()

    def _calculateP(self, x: int) -> float:
        '''Calculates P(X)'''

        probability: float = 0

        probability = self.constant * ((self.mu ** x) / factorial(x))

        return probability

    def _calculateF(self, x: int) -> float:
        '''Calculates F(X)'''

        F_x: float = 0

        i: int = 0

        loopSum: float = 0

        while i <= x:
            # calculate the elment of the sum
            elem = (self.mu ** i) / factorial(i)
            # add to the running sum
            loopSum = loopSum + elem
            # increment i
            i = i + 1

        F_x = self.constant * loopSum

        return F_x

    def _calculateMean(self) -> float:
        '''Calculate the E(X) of the geometric distribution'''

        self.mean = self.mu

    def _calculateVariance(self) -> float:
        '''Calculate the V(X) of the geometric distribution'''

        self.var = self.mu

    def _calculateStdDev(self) -> None:
        '''Calculate the S(X) of the geometric distribution'''

        self.stdDev = sqrt(self.var)


class discreteUniform(Probability):
    '''Add docstring'''

    def __init__(self, m: int, n: int) -> None:
        '''Add docstring'''

        self.m: float = m
        self.n: float = n
        self._calculateMean()
        self._calculateVariance()
        self._calculateStdDev()

    def _calculateP(self, x: int) -> float:
        '''Calculates P(X)'''

        probability: float = 0

        denominator: int = (self.n - self.m + 1)

        probability = 1 / denominator

        return probability

    def _calculateF(self, x: int) -> float:
        '''Calculates F(X)'''

        F_x: float = 0

        i: int = self.m

        while i <= x:
            # calculate the elment of the sum
            elem = self._calculateP(i)
            # add to the running sum
            F_x = F_x + elem
            # increment i
            i = i + 1

        return F_x

    def _calculateMean(self) -> None:
        '''Calculate the E(X) of the geometric distribution'''

        self.mean = 0.5 * (self.m + self.n)

    def _calculateVariance(self) -> None:
        '''Calculate the V(X) of the geometric distribution'''

        self.var = (1 / 12) * ((self.n - self.m) * (self.n - self.m + 2))

    def _calculateStdDev(self) -> None:
        '''Calculate the S(X) of the distribution'''

        self.stdDev = sqrt(self.var)
