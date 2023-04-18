from src.counter import Counter
        
def tallying() :
    tally = Counter()
    tally.reset()
    tally.click()
    tally.click()
    
    result = tally.getValue()
    print("Value:", result)
    
    #tally.reset()
    
    tally.click()
    result = tally.getValue()
    print("Value:", result)

class BankAccount :
    def __init__(self) :
        self._balance = 0.0

def other() :    
    a = 5
    b = 'Hello World'
    c = [1, 2, 3]
    d = False
    e = range(4)
    f = (1, 2, 3)
    g = complex(1, -1)
    
    for var in [a, b, c, d, e, f, g] :
        print(var.__class__)
        
        
class TrafficLight:
    '''This is an updated traffic light class'''

    # Class variable
    traffic_light_address = 'NYC_Cranberry_Hicks'

    def __init__(self, color):

        # Instance variable assigned inside the class constructor
        self.color = color

    def action(self):
        if self.color=='red':

            # Instance variable assigned inside a class method
            self.next_color = 'yellow'
            print('Stop & wait')
        elif self.color=='yellow':
            self.next_color = 'green'
            print('Prepare to stop')
        elif self.color=='green':
            self.next_color = 'red'
            print('Go')
        else:
            self.next_color = 'Brandy'
            print('Stop drinking 😉')

# Creating class objects
for c in ['red', 'yellow', 'green', 'fuchsia']:
    c = TrafficLight(c)
    print(c.traffic_light_address)
    print(c.color)
    c.action()
    print(c.next_color)
    print('\n')