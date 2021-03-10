class Mod:
    def __init__(self, value, modulus):
        self._modulus = Mod._validate_modulus(modulus)
        self._value = Mod._validate_value(value) % self._modulus # Store value as the residue.
        
    @staticmethod
    def _validate_value(value):
        if not isinstance(value, int):
            raise TypeError('Value must be an integer.')
        return value
    
    @staticmethod
    def _validate_modulus(modulus):
        modulus = Mod._validate_value(modulus)
        if modulus < 1:
            raise ValueError('Modulus must be positive.')
        return modulus
        
    @property
    def value(self):
        return self._value
    
    @property
    def modulus(self):
        return self._modulus
    
    def int_to_mod(self, value):
        return Mod(value, self.modulus)
    
    def validate_mod_math(self, other):
        if self.modulus != other.modulus:
            raise ValueError('Both Mod objects must have the same modulus to support this operation.')
            
    def _math_prep(self, other):
        if isinstance(other, int):
            other = self.int_to_mod(other)
        if isinstance(other, Mod):
            self.validate_mod_math(other)
            return other
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Mod):
            return self.modulus == other.modulus and self.value == other.value
        elif isinstance(other, int):
            return self.value == other % self.modulus
        return NotImplemented
    
    def __hash__(self):
        return hash((self.value, self.modulus))
    
    def __int__(self):
        return self.value
    
    def __repr__(self):
        return f'Mod(value={self.value}, modulus={self.modulus})'
    
    def __add__(self, other):
        other = self._math_prep(other)
        return Mod(self.value + other.value, self.modulus)
    
    def __sub__(self, other):
        other = self._math_prep(other)
        return Mod(self.value - other.value, self.modulus)
        
    def __mul__(self, other):
        other = self._math_prep(other)
        return Mod(self.value * other.value, self.modulus)
    
    def __pow__(self, other):
        other = self._math_prep(other)
        return Mod(self.value ** other.value, self.modulus)