from ..command import Command
from ..eventpackage import EventPackage
import math

class CalculateCommand(Command):
    #constants
    CHARINPUT = 0
    NUMINPUT = 1
    MATHINPUT = 2

    mathCmds = [
        "sqrt",
        "ceil",
        "floor",
        "deg",
        "rad",
        "abs",
        "exp",
        "log",
        "cos",
        "sin",
        "tan",
        "acos",
        "asin",
        "atan",
        "cosh",
        "sinh",
        "tanh",
        "acosh",
        "asinh",
        "atanh"
    ]
    mathSymbols = [
        "+",
        "-",
        "*",
        "/",
        "^",
        "(",
        ")",
        "%"
    ]

    def __init__(self):
        self.name = "Calculate"
        self.help = "1. string of math to calculate."
        self.author = "skuld"
        self.last_updated = "Oct. 08, 2018"

        self.state = self.CHARINPUT
        self.mathArr = []
        self.error = ""

    def isNumber(self,c):
        a = ord(c)
        output = False
        if a >= 48 and a <= 57:
            output = True
        elif a==46:
            output = True
        return output

    def doMathCmd(self, arr, n, s):
        #print("do math cmd:", arr, n, s)
        s = s + 1
        inv = 0
        outv = 0
        if n+1 > len(arr):
             return ( "error", s )
        if arr[n+1] in self.mathCmds:
             ret = doMathCmd( arr, n+1, s)
             inv = ret[0]
             s = ret[1]
        else:
             inv = arr[n+1]
        #do the math coommand.
        if arr[n] == "sqrt":
            outv = math.sqrt(inv)
        elif arr[n] == "ceil":
            outv = math.ceil(inv)
        elif arr[n] == "floor":
            outv = math.floor(inv)
        elif arr[n] == "deg":
            outv = math.degrees(inv)
        elif arr[n] == "rad":
            outv = math.radians(inv)
        elif arr[n] == "abs":
            outv = math.fabs(inv)
        elif arr[n] == "exp":
            outv = math.exp(inv)
        elif arr[n] == "log":
            outv = math.log(inv)
        #so much trig
        elif arr[n] == "cos":
            outv = math.cos(inv)
        elif arr[n] == "sin":
            outv = math.sin(inv)
        elif arr[n] == "tan":
            outv = math.tan(inv)
        elif arr[n] == "acos":
            outv = math.acos(inv)
        elif arr[n] == "asin":
            outv = math.asin(inv)
        elif arr[n] == "atan":
            outv = math.atan(inv)
        elif arr[n] == "cosh":
            outv = math.cosh(inv)
        elif arr[n] == "sinh":
            outv = math.sinh(inv)
        elif arr[n] == "tanh":
            outv = math.tanh(inv)
        elif arr[n] == "acosh":
            outv = math.acosh(inv)
        elif arr[n] == "asinh":
            outv = math.asinh(inv)
        elif arr[n] == "atanh":
            outv = math.atanh(inv)

        return (outv,s)

    def calcArray(self,arr):
        #somewhere in this it needs to determine things like:
        # 2pi and 2(2) as 2*pi and 2*(2)

        #print("1st pass", arr)
        #pass to make negative numbers:
        arrb = []
        n = 0
        while n < len(arr):
            if arr[n] == '-':
                if n + 1 <= len(arr):
                    v = 0 - arr[n+1]
                    arrb.append(v)
                    n=n+2
                else:
                    return "ERROR"
            else:
                arrb.append(arr[n])
                n=n+1
        arr = arrb

        #print("next pass:", arr)
        #pass for math commands
        arrb = []
        n = 0
        while n < len(arr):
            cmd = arr[n]
            if cmd in self.mathCmds:
                res = self.doMathCmd( arr, n, 0 )
                arrb.append(res[0])
                n = n + res[1] + 1
            else:
                arrb.append( cmd )
                n = n + 1
        arr = arrb

        #print("next pass:", arr)
        #pass for ^
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

        #print("next pass:", arr)
        #pass for *, / and %
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
            elif arr[n] == '%':
                m = len(arrb) - 1
                if m < 0:
                    self.error = "Error before %"
                    return
                if n+1 > len(arr):
                    self.error = "Error at %"
                    return
                arrb[m] = math.fmod( arrb[m], arr[n+1] )
                n=n+2
            else:
                arrb.append(arr[n])
                n=n+1
        arr = arrb

        #print("next pass:", arr)
        #pass for + and -
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
            elif arr[n] < 0: #subtraction was converted to negative numbers
                m = len(arrb) - 1
                if m >= 0:
                    if n+1 > len(arr):
                        self.error = "Error at -"
                        return
                    arrb[m] = arrb[m] + arr[n]
                    n=n+1
                else:
                    arrb.append(arr[n])
                    n=n+1
            else:
                arrb.append(arr[n])
                n=n+1
        arr = arrb

        return arr[0]

    def parseFormula(self, formula):
        buf = ""
        arr = []
        n = 0

        def addMathCmd():
            nonlocal buf
            nonlocal arr
            cmd = buf.strip().lower()
            if cmd in self.mathCmds:
                arr.append(cmd)
            elif cmd == "pi":
                res = math.pi
                arr.append( res )
            elif cmd == "e":
                res = math.e
                arr.append( res )
            buf=""
            return

        def addNumber():
            nonlocal buf
            nonlocal arr
            arr.append(float(buf))
            buf=""
            return

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
                    buf+=c;

            elif self.state == self.NUMINPUT:
                if self.isNumber(c):
                    buf = buf+c
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
                        self.state = self.NUMINPUT
                        return (arr,n)
                    else:
                        arr.append(c)
                        n = n + 1
                    self.state = self.CHARINPUT
                else:
                    self.state = self.CHARINPUT
        if self.state == self.NUMINPUT:
            addNumber()
        if self.state == self.CHARINPUT:
            addMathCmd()

        return (arr,n)

    def run(self, event_pack: EventPackage):
        buf = ""
        arr = []
        self.state = self.CHARINPUT
        self.mathArr = []
        self.error = ""

        output = ""

        farr = event_pack.body
        farr.pop(0)
        formula = "".join(farr).replace(" ","")

        #print("formula: ",formula)

        try:
            self.mathArr = self.parseFormula(formula)[0]
            output = self.calcArray(self.mathArr)
        except Exception as e:
            output = e

        return str(output)
