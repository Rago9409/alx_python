"""
    This program code  represents a square.

    Attributes:
        __size (int): The size of the square.

    """
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    """
    def __init__(self, size=0):
        """
        The constructor for Square class.

        Parameters:
            size (int): The size of the square.

        """
        self.size = size

    @property
    def size(self):
         """
    This function  represents a square setting property.

    Attributes:
        __size (int): The size of the square.

    """
         return self.__size
    

    @size.setter
    def size(self, value):
         """
    This function represents a square with  setting property.

    Attributes:
        __size (int): The size of the square.

    """
         if not isinstance(value, int):
                 """  This Checks  a square value is integer.

    Attributes:
        __size (int): The size of the square.

    """
         raise TypeError("size must be an integer")
        elif value < 0:
    """
    This checks  a square value not integer.

    Attributes:
        __size (int): The size of the square.

    """
    raise ValueError("size must be >= 0")
    self.__size = value

    def area(self):
        """
        This method calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
    def my_print(self):
        """
        This method prints the square with the character #.

        """
        if self.__size == 0:
            """
        This function prints the empty line.

        """
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                    print()
