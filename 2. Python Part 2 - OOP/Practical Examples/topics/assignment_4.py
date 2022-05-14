class VirusDetector:
    detectorCount = 0

    def __init__(self, detectorID, detectorVersion, detectorPassword):
        VirusDetector.detectorCount += 1
        self.detectorID = detectorID
        self.detectorVersion = detectorVersion
        self.detectorPassword = detectorPassword
        self.analyzeFile
        self.codeBuffer

    def displayDetectorInfo(self):
        pass

    def readFileToCodeBuffer(self):
        pass

    def flushCodeBuffer(self):
        pass

    def analyzeCodeBuffer(self):
        pass

    def countTotalBytes(self):
        pass

    def countTotalBits(self):
        pass

    def countFalseBits(self):
        pass

    def countTrueBytes(self):
        pass

    def countFalseBytes(self):
        pass

    def countAllTrueBytes(self):
        pass

    def countAllFalseBytes(self):
        pass

    def countRecurrentTrueBytes(self):
        pass

    def countRecurrentFalseBytes(self):
        pass

    def countSymmetricBytes(self):
        pass

    def checkForMalformedByte(self):
        pass

    def checkBit(self, b):
        pass

    def detectAlphaVirus(self):
        pass

    def detectBetaVirus(self):
        pass

    def detectGammaVirus(self):
        pass

    @staticmethod
    def displayDetectorCodeBuffer():
        pass