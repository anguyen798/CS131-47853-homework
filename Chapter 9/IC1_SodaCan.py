class SodaCan:
    def __init__(self, height, radius, canNumber):
        self.height = height
        self.radius = radius
        self.canNumber = canNumber

    def getSurfaceArea(self):
        import math
        pi = math.radians(180)
        surfArea = (2 * pi * self.radius * self.height) 
        + (2 * pi * self.radius * self.radius)
        result = "%.2f" % surfArea
        print("The surface area of can %d (h = %d, r = %d) is %s" % 
              (self.canNumber, self.height, self.radius, result))
        return float(result)

    def getVolume(self):
        import math
        pi = math.radians(180)
        volume = (pi * self.radius * self.radius * self.height)
        result = "%.2f" % volume
        print("The volume of the can %d (h = %d, r = %d) is %s" % 
              (self.canNumber, self.height, self.radius, result))
        return float(result)
