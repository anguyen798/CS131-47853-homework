class SodaCan :
    def __init__(self, height, radius) :
        self.height = height
        self.radius = radius
    
    def getSurfaceArea(self): 
        import math
        pi = math.radians(180)
        surfArea =  (2 * pi * self.radius * self.height) + (2 * pi * self.radius * self.radius)
        result = surfArea 
        print("%.2f" % result)
        return result 

    
    def getVolume(self): 
        import math 
        pi = math.radians(180)
        volume = (pi * self.radius * self.radius * self.height )
        result = volume
        print("%.2f" % result)
        return volume 
        
