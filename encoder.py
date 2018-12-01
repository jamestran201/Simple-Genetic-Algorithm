class GeneEncoder:
    """
    This class can be used to convert a real value within a given range
    to a binary string and vice versa
    """

    def __init__(self, min_value, max_value, n_bits, precision):
        """
        Class constructor

        Parameters
        ----------
        min_value : float
            The minimum value in the range
        max_value : float
            The maximum value in the range
        n_bits : int
            The number of bits in the binary string
        precision : int
            Number of decimals to keep for the real value
        """

        self.min_value = float(min_value)
        self.max_value = float(max_value)
        self.n_bits = n_bits
        self.precision = precision
    
    def real_to_binary(self, value):
        """
        Convert a real value to a binary string. The input value
        should be within the range min_value and max_value

        Parameters
        ----------
        value : float
            A real value within the range [min_value, max_value]
        
        Returns
        -------
        A binary string that represents the input value
        """

        assert (value >= self.min_value) and (value <= self.max_value),\
                "The given value is outside of the range [{}, {}]".format(self.min_value, self.max_value)

        value = round(value, self.precision)
        t = (value - self.min_value) * (2**self.n_bits - 1) / (self.max_value - self.min_value)
        t = int(round(t, 0))

        return "{0:0{width}b}".format(t, width=self.n_bits)

    def binary_to_real(self, binary_str):
        """
        Convert a binary string to a real value within the range [min_value, max_value]

        Parameters
        ----------
        binary_str : str
            A binary string of length n_bits
        
        Returns
        -------
        A real value
        """

        assert (len(binary_str) == self.n_bits), "The string length must be {}".format(self.n_bits)

        value = self.min_value + (self.max_value - self.min_value) / (2**self.n_bits - 1) * int(binary_str, 2)
        return round(value, self.precision)
        
    def binary_to_gray(self, binary_str):
        """
        Convert a binary string to Gray code

        Parameters
        ----------
        binary_str : str
            A binary string of length n_bits
        
        Returns
        -------
        The Gray code string representing the input binary string
        """

        assert (len(binary_str) == self.n_bits), "The string length must be {}".format(self.n_bits)

        gray_str = []
        gray_str.append(binary_str[0])

        for i in range(1, len(binary_str)):
            gray_str.append( str( int(binary_str[i-1]) ^ int(binary_str[i]) ) )

        return "".join(gray_str)

    def gray_to_binary(self, gray_str):
        """
        Convert Gray code to the corresponding binary string

        Parameters
        ----------
        gray_str : str
            A binary string in Gray code
        
        Returns
        -------
        The binary string corresponding to the Gray code string
        """

        assert (len(gray_str) == self.n_bits), "The string length must be {}".format(self.n_bits)

        binary_str = []
        binary_str.append(gray_str[0])

        for i in range(1, len(gray_str)):
            binary_str.append( str( int(gray_str[i]) ^ int(binary_str[i-1]) ) )

        return "".join(binary_str)

    def real_to_gray(self, value):
        """
        Convert a real value within the range [min_value, max_value]
        to its Gray code representation

        Parameters
        ----------
        value : float
            A real value within the range [min_value, max_value]
        
        Returns
        -------
        The Gray code representation of the input value
        """

        assert (value >= self.min_value) and (value <= self.max_value),\
                "The given value is outside of the range [{}, {}]".format(self.min_value, self.max_value)

        binary_str = self.real_to_binary(value)
        gray_str = self.binary_to_gray(binary_str)
        return gray_str
    
    def gray_to_real(self, gray_str):
        """
        Convert a Gray code string to its real value

        Parameters
        ----------
        gray_str : str
            A Gray code string of length n_bits
        
        Returns
        -------
        The real value corresponding to the Gray code
        """

        assert (len(gray_str) == self.n_bits), "The string length must be {}".format(self.n_bits)

        binary_str = self.gray_to_binary(gray_str)
        value = self.binary_to_real(binary_str)
        return value

def binary_to_bipolar(input_str):
    """
    Given a binary string, convert it to either -1 or 1
    """
    
    result=[]
    for s in input_str:
        if s == "0":
            result.append(-1)
        else:
            result.append(1)

    return result