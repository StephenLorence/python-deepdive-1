# inventory.py

from validators import validate_string, validate_integer

class Resource:

    def __init__(self, name, manufacturer, total=0, allocated=0):
        self._name = validate_string(name, 'Name')
        self._manufacturer = validate_string(manufacturer, 'Manufacturer')
        self._total = 0
        self._allocated = 0
        self.purchase(total, zero_allowed=True)
        self.claim(allocated, zero_allowed=True)

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def category(self):
        return self.__class__.__name__.lower()

    def purchase(self, qty, zero_allowed=False):
        self._total += validate_integer(qty, zero_allowed=zero_allowed)
        self._remaining = None
        return f'New total quantity: {self.total}'

    @property
    def allocated(self):
        return self._allocated

    def claim(self, qty, zero_allowed=False):
        qty = validate_integer(qty, zero_allowed=zero_allowed)
        if qty > self.remaining:
            raise ValueError('Not enough available stock.')
        self._allocated += qty
        self._remaining = None
        return f'New allocated quantity: {self.allocated}'

    @property
    def remaining(self):
        if self._remaining is None:
            self._remaining = self.total - self.allocated
        return self._remaining

    def freeup(self, qty):
        qty = validate_integer(qty)
        self._allocated -= qty
        self._remaining = None
        return f'New allocated quantity: {self.allocated}'

    def died(self, qty):
        qty = validate_integer(qty)
        if qty > self.total:
            raise ValueError('Cannot kill more than total stock quantity.')
        else:
            self._total -= qty
            self._remaining = None
            if self.total <= self.allocated:
                self._allocated = self.total
        print(f'{qty} unit' + ('s' if qty > 1 else '') + ' died.'
               f'\nNew total: {self.total}'
               f'\nAllocated: {self.allocated}'
               f'\nRemaining: {self.remaining}')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__class__.__name__} (name={self.name}, manufacturer={self.manufacturer})'


    
