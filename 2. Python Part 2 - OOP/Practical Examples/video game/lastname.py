class Pack:
    _owner = ''
    _pType = ''
    _compartment = []

    def __init__(self, owner, pType):
        pass

    def addItem(self, v):
        pass

    def removeItem(self, v):
        pass

    def displayPackContents(self):
        pass


class AssultPack(Pack):
    _pType = "Assault Pack"

    def __init__(self, owner):
        Pack.__init__(self)


class ScoutPack(Pack):
    _pType = "Scout Pack"

    def __init__(self, owner):
        Pack.__init__(self)


class Weapon:
    _ID = ''
    _model = ''
    _ammoCapacity = 0
    _currentAmmo = 0
    _maxRange = 0

    def __init__(self, ID, model, ammoCapacity, maxRange):
        pass

    def displayWeaponInfo(self):
        pass



class Blaster(Weapon):
    _model = "Blaster"
    _ammoCapacity = 50
    _maxRange = 100



