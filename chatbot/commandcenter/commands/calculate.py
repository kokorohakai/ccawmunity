from ..command import Command
from ..eventpackage import EventPackage

class CalculateCommand(Command):
    #constants
    CHARINPUT = 0
    NUMINPUT = 1
    MATHINPUT = 2

    mathCmds = [
        "sqrt",
        "cos",
        "sin",
        "tan",
        "csc",
        "sec",
        "abs",
        "cotan"
    ]
    mathSymbols = [
        "+",
        "-",
        "*",
        "/",
        "^",
        "(",
        ")"
    ]

    def __init__(self):
        self.name = "Calculate"
        self.help = "1. string of math to calculate."
        self.author = "skuld"
        self.last_updated = "Oct. 08, 2018"
        self.state = self.CHARINPUT
        self.mathArr = []
        self.buf = ""
        self.error = ""

    def isNumber(self,c):
        a = ord(c)
        output = False
        if a >= 48 and a <= 57:
            output = True
        elif a==46:
            output = True
        return output

    def calcArray(self,arr):

        #1st pass for ^
        arrb = []
        n = 0
        while n < len( arr ):
            if arr[n] == '^':
                m = len(arrb) - 1
                if m < 0:
                    self.error = "Error before ^"
                    return
                if n+1 > len(arr):
                    self.error = "Error at ^"
                    return
                arrb[m] = arrb[m] ** arr[n+1]
                n=n+2
            else:
                arrb.append(arr[n])
                n=n+1
        arr = arrb

        #2nd pass for * and /
        arrb = []
        n = 0
        while n < len( arr ):
            if arr[n] == '*':
                m = len(arrb) - 1
                if m < 0:
                    self.error = "Error before *"
                    return
                if n+1 > len(arr):
                    self.error = "Error at *"
                    return
                arrb[m] = arrb[m] * arr[n+1]
                n=n+2
            elif arr[n] == '/':
                m = len(arrb) - 1
                if m < 0:
                    self.error = "Error before /"
                    return
                if n+1 > len(arr):
                    self.error = "Error at /"
                    return
                arrb[m] = arrb[m] / arr[n+1]
                n=n+2
            else:
                arrb.append(arr[n])
                n=n+1
        arr = arrb

        #final pass for + and -
        arrb = []
        n = 0
        while n < len( arr ):
            if arr[n] == '+':
                m = len(arrb) - 1
                if m < 0:
                    self.error = "Error before +"
                    return
                if n+1 > len(arr):
                    self.error = "Error at +"
                    return
                arrb[m] = arrb[m] + arr[n+1]
                n=n+2
            elif arr[n] == '-':
                m = len(arrb) - 1
                if m < 0:
                    self.error = "Error before -"
                    return
                if n+1 > len(arr):
                    self.error = "Error at -"
                    return
                arrb[m] = arrb[m] - arr[n+1]
                n=n+2
            else:
                arrb.append(arr[n])
                n=n+1
        arr = arrb
        return arr[0]

    def parseFormula(self, formula):
        def addMathCmd():
            cmd = self.buf.strip().lower()
            if cmd in self.mathCmds:
                arr.append(cmd)
            self.buf=""
            return

        def addNumber():
            arr.append(float(self.buf))
            self.buf=""
            return

        n = 0
        self.buf=""
        arr = []
        while n < len(formula):
            c = formula[n]

            if self.state==self.CHARINPUT:
                if self.isNumber(c):
                    addMathCmd()
                    self.state = self.NUMINPUT
                elif c in self.mathSymbols:
                    addMathCmd()
                    self.state = self.MATHINPUT
                else:
                    n=n+1;
                    self.buf+=c;

            elif self.state == self.NUMINPUT:
                if self.isNumber(c):
                    self.buf = self.buf+c
                    n=n+1
                else:
                    addNumber()
                    self.state = self.CHARINPUT

            elif self.state == self.MATHINPUT:
                if c in self.mathSymbols:
                    if c == "(":
                        self.state = self.CHARINPUT
                        remaining = formula[n+1:]
                        ret = self.parseFormula(remaining)
                        arr.append(self.calcArray(ret[0]))
                        n = n + ret[1] + 2
                    elif c == ")":
                        self.state = self.CHARINPUT
                        return (arr,n)
                    else:
                        arr.append(c)
                        n=n+1
                    self.state = self.CHARINPUT
                else:
                    self.state = self.CHARINPUT
        if self.state == self.NUMINPUT:
            addNumber()
        if self.state == self.CHARINPUT:
            addMathCmd()

        return (arr,n)

    def run(self, event_pack: EventPackage):
        output = ""

        farr = event_pack.body
        farr.pop(0)
        formula = "".join(farr).replace(" ","")

        #print("formula: ",formula)

        try:
            self.mathArr = self.parseFormula(formula)[0]
            #print(self.mathArr)
            output = self.calcArray(self.mathArr)
        except Exception as e:
            output = e

        return str(output)
