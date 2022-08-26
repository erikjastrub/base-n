from numericsystemerrors import DuplicateError, InvalidBasesError

class NumericSystem:
    """A numeric system with a custom base, 
    instantiated by supplying the list of bases used to represent values"""

    # A string outlining the characters used to represent the range of values covered by the numeric system
    # E.g Hex (Base16) has bases of "0123456789ABCDEF"
    # E.g Denary (Base10) has bases of "0123456789"
    # E.g Binary (Base2) has bases of "01"
    bases: str

    # The base/subscript of the numeric system
    subscript: int

    # Optional character used to identify whether a value is negative or not
    # If not supplied, then the numeric system will be assumed to only represent positive values
    negative_base: str

    # A map, caching the character to the value it is representing in the numeric system
    char_to_value: dict

    def __init__(self, bases: str, negative_base: str = ''):

        self.bases: str = bases
        self.subscript: int = len(bases)

        if self.subscript < 2:

            raise InvalidBasesError

        self.negative_base: str = negative_base

        
        self.char_to_value = {}
        for i, c in enumerate(bases):

            # One character should represent one value in a One-To-One relationship
            if c in self.char_to_value or c == self.negative_base: 
                
                raise DuplicateError

            self.char_to_value[c] = i

    def encode(self, value: int) -> str:
        """Given a value, will return the base-n represenation of it"""
        
        negative = False
        if value < 0:

            if not self.negative_base: 
                
                raise ValueError("Numeric system cannot represent negative values")

            negative = True

            # Make value positive to operate on the magnitude of the value
            value *= -1

        encoded_value = ""
        while value != 0:
            
            # Modding the value by the base will extract the right-most value in the integer
            encoded_value = self.bases[value % self.subscript] + encoded_value

            # Remove the right-most value from the integer
            value //= self.subscript

        return self.negative_base + encoded_value if negative else encoded_value

    def decode(self, value: str) -> int:
        """Given a value represented in the custom numeric system, will return the base10 value for it"""

        length = len(value)

        # By setting the base to length-1, we can iterate forward
        # removing the cost of computation to reverse the string to iterate backwards
        base, sign = length-1, 1
        total = index = 0

        if value and value[0] == self.negative_base:

            index = 1
            base -= 1
            sign = -1
            
        while index < length:

            try: 
                    
                total += self.char_to_value[value[index]] * (self.subscript ** base)
                    
            except KeyError: 
                    
                raise ValueError("Unknown character found in value")
            
            else:

                index += 1
                base -= 1

        return total * sign