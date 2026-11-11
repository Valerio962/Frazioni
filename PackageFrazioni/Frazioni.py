def MCD(a, b):
    if a<0:a=-a
    if b<0:b=-b
    if a==0 or b==0 :return 1
    mcd=1
    for i in range(1, min(a, b)+1):
        if a%i==0 and b%i==0:
            mcd=i
    return mcd

class Frazione:
    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore

    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"
    
    def __repr__(self):
        return f"Frazione({self.numeratore}, {self.denominatore})"
    
    def riduci(self):
        mcd = MCD(self.numeratore, self.denominatore)
        self.numeratore //= mcd
        self.denominatore //= mcd
        return self
    
    def __getattr__(self, name):
        if name == "denominatore" and self.denominatore == 0:
            raise ValueError("Denominatore non può essere zero.")
        if name == "valore":
            return self.numeratore/self.denominatore
        return -1

    def __add__(self, other):
        if isinstance(other, Frazione):
            new_numeratore = (self.numeratore * other.denominatore) + (other.numeratore * self.denominatore)
            new_denominatore = self.denominatore * other.denominatore
            return Frazione(new_numeratore, new_denominatore)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Frazione' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Frazione):
            new_numeratore = (self.numeratore * other.denominatore) - (other.numeratore * self.denominatore)
            new_denominatore = self.denominatore * other.denominatore
            return Frazione(new_numeratore, new_denominatore)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Frazione' and '{}'".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Frazione):
            new_numeratore = self.numeratore * other.numeratore
            new_denominatore = self.denominatore * other.denominatore
            return Frazione(new_numeratore, new_denominatore)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Frazione' and '{}'".format(type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, Frazione):
            new_numeratore = self.numeratore * other.denominatore
            new_denominatore = self.denominatore * other.numeratore
            return Frazione(new_numeratore, new_denominatore)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Frazione' and '{}'".format(type(other).__name__))
        
