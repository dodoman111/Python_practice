class Fraction(object):
    def __init__(self,num,den):
        self.num = num
        self.den = den
        self.simplify()
        
    def toString(self):
        return str(self.num)+'/'+str(self.den)
    
    def add(self,other):
        if self.den != other.den:
            self.num = self.num * other.den
            other.num = self.den * other.num
            other.den = self.den * other.den
            return Fraction(self.num+other.num,other.den)
        else :
            return Fraction(self.num+other.num,other.den)
    def simplify(self):
        g = Fraction.gcd(self.num,self.den)
        self.num = self.num//g
        self.den = self.den//g
        return str(self.num)+'/'+str(self.den)
    
    @staticmethod
    def gcd(a,b):
        while (b!=0):
            (a,b) = (b,a%b)
        return a
