class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"Constructor: {self.real} + {self.imag}i")

    def __del__(self):
        print(f"Destructor: {self.real} + {self.imag}i is being destroyed")

    def __add__(self, other):
        return Complex(
            self.real + other.real, 
            self.imag + other.imag)


    def __sub__(self, other):
        return Complex(self.real - other.real,
                        self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"


c1 = Complex(4, 5)
c2 = Complex(2, 3)

print("First Complex Number:", c1)
print("Second Complex Number:", c2)

c3 = c1 + c2
print("After Addition:", c3)

c4 = c1 - c2
print("After Subtraction:", c4)