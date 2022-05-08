class TurboProp:
    aircraftCount = 0

    def __init__(self, variant, modelNumber, aircraftTailNumber, crew,\
                 passengerCapacity, passengers, length, wingSpan, height,\
                 currentSpeed, currentAltitude, isLanded, isAirborne):
        TurboProp.aircraftCount += 1
        self.variant = variant
        self.modelNumber = modelNumber
        self.aircraftTailNumber = aircraftTailNumber
        self.crew = crew
        self.passengerCapacity = passengerCapacity
        self.passengers = passengers
        self.length = length
        self.wingSpan = wingSpan
        self.height = height
        self.currentSpeed = currentSpeed
        self.currentAltitude = currentAltitude
        self.isLanded = isLanded
        self.isAirborne = isAirborne

    def displayACInfo(self):
        print(10*"-", f"Aircraft Status For: {self.aircraftTailNumber}", 10*"-")
        print(f"Variant: {self.variant}\n"\
              f"Model Number: {self.modelNumber}\n"\
              f"AC Tail Number: {self.aircraftTailNumber}")

    def displayACStatus(self):
        print(10*"-", f"Aircraft Status For: {self.aircraftTailNumber}", 10*"-")
        print(f"Speed: {self.currentSpeed}\n"\
              f"Altitude: {self.currentAltitude}\n"\
              f"In Flight {self.isAirborne}")

    def displayPassengerInfo(self):
        for i in self.passengers:
            i.displayPassengerInfo()

    def TakeOff(self):
        if self.isAirborne:
            print("Aircraft is already airborne")
        else:
            self.currentSpeed = 75
            self.currentAltitude = 200
            self.isLanded = False
            self.isAirborne = True
            print(f"{self.aircraftTailNumber} has taken off")

    def Land(self):
        if not self.isAirborne:
            print("Aircraft is already landed")
        else:
            self.currentSpeed = 0
            self.currentAltitude = 0
            self.isLanded = True
            self.isAirborne = False
            print(f"{self.aircraftTailNumber} is landed")


class Passenger:
    passengerCount = 0

    def __init__(self, IDNumber, SeatNumber):
        Passenger.passengerCount += 1
        self.__IDNumber = IDNumber
        self.__SeatNumber = SeatNumber

    def displayPassengerInfo(self):
        print(f"Passenger ID: {self.getIDNumber()}")
        print(f"Passenger Seat: {self.getSeatNumber()}")

    def getIDNumber(self):
        return self.__IDNumber

    def setIDNumber(self, v):
        self.__IDNumber = v

    def getSeatNumber(self):
        return self.__SeatNumber

    def setSeatNumber(self, v):
        self.__SeatNumber = v


P = [Passenger("P-01", "1A"), Passenger("P-02", "1B"),
     Passenger("P-03", "2A"), Passenger("P-01", "2B")]

T = TurboProp("BeechCraft200", "BC-001", "US-BC-01", 2, 10, P, 43.5, 57.5, 14.33, 130, 5000, False, True)

T.displayACStatus()
T.displayPassengerInfo()
T.Land()
T.displayACStatus()
T.TakeOff()
T.displayACStatus()
