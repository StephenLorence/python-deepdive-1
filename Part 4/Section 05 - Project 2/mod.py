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
    
    def __eq__(self, other):
        if isinstance(other, Mod):
            return self.modulus == other.modulus and self.value == other.value
        elif isinstance(other, int):
            return self.value == other % self.modulus
        return NotImplemented
    
    def __hash__(self):
        return hash((self.value, self.modulus))