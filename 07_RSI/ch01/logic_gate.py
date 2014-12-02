#!/usr/bin/env python3
class LogicGate:

    def __init__(self, label):
        self.name = label
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.calcLogicOutput()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            UsrPinA = input("Enter Pin A value for " + self.name + ": ")
            return int(UsrPinA) >= 1
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            UsrPinB = input("Enter Pin B value for " + self.name + ": ")
            return int(UsrPinB) >= 1
        else:
            return self.pinB.getFrom().getOutput()

    def SetSrcPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Source pins are already occupied")

class AndGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def calcLogicOutput(self):
        pinA = self.getPinA()
        pinB = self.getPinB()

        return int(pinA == 1 and pinB == 1)

class OrGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def calcLogicOutput(self):
        pinA = self.getPinA()
        pinB = self.getPinB()

        return int(pinA == 1 or pinB == 1)

class NorGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def calcLogicOutput(self):
        pinA = self.getPinA()
        pinB = self.getPinB()

        return int(not(pinA == 1 or pinB == 1))

class NandGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def calcLogicOutput(self):
        pinA = self.getPinA()
        pinB = self.getPinB()

        return int(not(pinA == 1 and pinB == 1))

class XorGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def calcLogicOutput(self):
        pinA = self.getPinA()
        pinB = self.getPinB()

        return int(pinA != pinB)


class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            UsrPin = input("Enter Pin value for " + self.name + ": ")
            return int(UsrPin) >= 1
        else:
            return self.pin.getFrom().getOutput()

    def SetSrcPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Source pins are already occupied")

class NotGate(UnaryGate):
    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def calcLogicOutput(self):
        return int(not self.getPin())

class CommonInput(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def calcLogicOutput(self):
        if self.pin == None:
            self.pin = input("Enter Pin value for " + self.name + ": ")
            self.pin = int(self.pin) >= 1
            return self.pin
        else:
            return self.pin

class Connector:
    def __init__(self, fromGate, toGate):
        self.fromGate = fromGate
        self.toGate   = toGate

        toGate.SetSrcPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate

def HalfAdder():
    g1 = CommonInput("A")
    g2 = CommonInput("B")
    g3 = XorGate("Sum")
    g4 = AndGate("Carrier")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g1, g4)
    c4 = Connector(g2, g4)
    print(g3.getOutput())
    print(g4.getOutput())

def Test1():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())


def Test2():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = NotGate("G3")
    g4 = NotGate("G4")
    g5 = AndGate("G5")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g4)
    c3 = Connector(g3, g5)
    c4 = Connector(g4, g5)
    print(g5.getOutput())


    g1 = XorGate("xor")
    print(g1.getOutput())

if __name__ == "__main__":
    #g1 = NandGate("l1")
    #print(g1.calcLogicOutput())
    #g2 = NorGate("12")
    #print(g2.calcLogicOutput())
    #Test1()
    HalfAdder()
