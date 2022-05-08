
class ImperialDroid:
    __DroidID = ''
    __DroidType = ''

    def __init__(self, DroidID, DroidType):
        self.__DroidID = DroidID
        self.__DroidType = DroidType

        self.c = Cranial(self.__DroidID)
        self.t = Torso(self.__DroidID)
        self.la = LeftArm(self.__DroidID)
        self.ra = RightArm(self.__DroidID)
        self.ll = LeftLeg(self.__DroidID)
        self.rl = RightLeg(self.__DroidID)

    def displayInfo(self):
        self.c.displayInfo()
        self.t.displayInfo()
        self.la.displayInfo()
        self.ra.displayInfo()
        self.ll.displayInfo()
        self.rl.displayInfo()

    def runDiagnostic(self):
        if self.c.getOperational() and self.t.getOperational() and self.la.getOperational() \
                and self.ra.getOperational() and self.ll.getOperational() and self.rl.getOperational():
            print(f"{self.__DroidID} is Functioning Normally")
        else:
            print(f"{self.__DroidID} is Malfunctioning")

    def getDroidID(self):
        return self.__DroidID

    def setDroidID(self, v):
        self.__DroidID = v

    def getDroidType(self):
        return self.__DroidType

    def setDroidType(self, v):
        self.__DroidType = v


class SentryDroid_A(ImperialDroid):
    def __init__(self, DroidID):
        super().__init__(DroidID=DroidID, DroidType="Alpha")

    def displayInfo(self):
        print(f"***Sentry Droid {super().getDroidType()}***")
        print(f"Droid ID: {super().getDroidID()}")
        print(f"Droid Type: {super().getDroidType()}")
        super().displayInfo()


class SentryDroid_B(ImperialDroid):
    def __init__(self, DroidID):
        ImperialDroid.__init__(DroidID=DroidID, DroidType="Beta")

    def displayInfo(self):
        print(f"***Sentry Droid {super().getDroidType()}***")
        print(f"Droid ID: {super().getDroidID()}")
        print(f"Droid Type: {super().getDroidType()}")
        super().displayInfo()


class SentryDroid_C(ImperialDroid):
    def __init__(self, DroidID):
        ImperialDroid.__init__(DroidID=DroidID, DroidType="Gamma")

    def displayInfo(self):
        print(f"***Sentry Droid {super().getDroidType()}***")
        print(f"Droid ID: {super().getDroidID()}")
        print(f"Droid Type: {super().getDroidType()}")


class Body:
    def __init__(self, IDNumber, BType):
        self.__IDNumber = IDNumber
        self.__BType = BType

    def displayInfo(self):
        pass

    def getIDNumber(self):
        return self.__IDNumber

    def setIDNumber(self, v):
        self.__IDNumber = v

    def getBType(self):
        return self.__BType

    def setBType(self, v):
        self.__BType = v


class Cranial(Body):
    def __init__(self, IDNumber):
        super().__init__(IDNumber, BType="Cranial")
        self.__Operational = True

    def displayInfo(self):
        print(f"Head Operational: {self.getOperational()}")

    def getOperational(self):
        return self.__Operational

    def setOperational(self, v):
        self.__Operational = v


class Torso(Body):
    def __init__(self, IDNumber):
        super().__init__(IDNumber, BType="Torso")
        self.__Operational = True

    def getOperational(self):
        return self.__Operational

    def setOperational(self, v):
        self.__Operational = v

    def displayInfo(self):
        print(f"Upper Torso Operational: {self.getOperational()}")


class Leg:
    def __init__(self, IDNumber, LType):
        self.__IDNumber = IDNumber
        self.__LType = LType

    def displayInfo(self):
        pass

    def getIDNumber(self):
        return self.__IDNumber

    def setIDNumber(self, v):
        self.__IDNumber = v

    def getLType(self):
        return self.__LType

    def setLType(self, v):
        self.__LType = v


class LeftLeg(Leg):
    def __init__(self, IDNumber):
        super().__init__(IDNumber, LType="Left Leg")
        self.__Operational = True

    def displayInfo(self):
        print(f"Left Leg Operational: {self.getOperational()}")

    def getOperational(self):
        return self.__Operational

    def setOperational(self, v):
        self.__Operational = v


class RightLeg(Leg):
    def __init__(self, IDNumber):
        super().__init__(IDNumber, LType="Right Leg")
        self.__Operational = True

    def displayInfo(self):
        print(f"Right Leg Operational: {self.getOperational()}")

    def getOperational(self):
        return self.__Operational

    def setOperational(self, v):
        self.__Operational = v


class Arm:
    def __init__(self, IDNumber, AType):
        self.__IDNumber = IDNumber
        self.__AType = AType

    def displayInfo(self):
        pass

    def getIDNumber(self):
        return self.__IDNumber

    def setIDNumber(self, v):
        self.__IDNumber = v

    def getAType(self):
        return self.__AType

    def setAType(self, v):
        self.__AType = v


class LeftArm(Arm):
    def __init__(self, IDNumber):
        super().__init__(IDNumber, AType="Left Arm")
        self.__Operational = True

    def getOperational(self):
        return self.__Operational

    def setOperational(self, v):
        self.__Operational = v

    def displayInfo(self):
        print(f"Left Arm Operational: {self.getOperational()}")


class RightArm(Arm):
    def __init__(self, IDNumber):
        super().__init__(IDNumber, AType="Right Arm")
        self.__Operational = True

    def displayInfo(self):
        print(f"Right Arm Operational: {self.getOperational()}")

    def getOperational(self):
        return self.__Operational

    def setOperational(self, v):
        self.__Operational = v


class DroidFactory:
    def __init__(self, IDNumber, BuildType):
        self.__IDNumber = IDNumber
        self.__BuildType = BuildType

    def displayInfo(self):
        pass

    def getIDNumber(self):
        return self.__IDNumber

    def setIDNumber(self, v):
        self.__IDNumber = v

    def getBuildType(self):
        return self.__BuildType

    def setBuildType(self, v):
        self.__BuildType = v


class Sentry_AFactory(DroidFactory):
    def __init__(self, IDNumber):
        super().__init__(IDNumber, BuildType="Alpha Droids")

    def buildDroids_A(self, count):
        dl = []
        for i in range(count):
            t = SentryDroid_A("X")
            dl.append(t)
        return dl

    @staticmethod
    def displayDroids(dl):
        for i in dl:
            i.displayInfo()


class Sentry_BFactory(DroidFactory):
    def __init__(self, IDNumber):
        super().__init__(IDNumber, BuildType="Beta Droids")

    def buildDroids_B(self, count):
        dl = []
        for i in range(count):
            t = SentryDroid_B("X")
            dl.append(t)
        return dl

    @staticmethod
    def displayDroids(dl):
        for i in dl:
            i.displayInfo()


class Sentry_CFactory(DroidFactory):
    def __init__(self, IDNumber):
        super().__init__(IDNumber, BuildType="Gamma Droids")

    def buildDroids_C(self, count):
        dl = []
        for i in range(count):
            t = SentryDroid_C("X")
            dl.append(t)
        return dl

    @staticmethod
    def displayDroids(dl):
        for i in dl:
            i.displayInfo()


def main():
    SAF = Sentry_AFactory("F-2")
    DL = SAF.buildDroids_A(2)
    Sentry_AFactory.displayDroids(DL)


main()
