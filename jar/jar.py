class Jar:
    def __init__(self, capacity=12):
        """
        Initializes a cookie jar with the given capacity.
        Default capacity is 12 if not specified.
        Raises ValueError if capacity is not a non-negative integer.
        """
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """
        Returns a string with 🍪 symbols, representing the number of cookies in the jar.
        For example, if there are 3 cookies, returns "🍪🍪🍪".
        """
        return "🍪" * self._size

    def deposit(self, n):
        """
        Adds n cookies to the jar.
        Raises ValueError if adding n cookies would exceed the jar's capacity.
        """
        if n < 0 or self._size + n > self._capacity:
            raise ValueError("Cannot deposit that many cookies: exceeds capacity.")
        self._size += n

    def withdraw(self, n):
        """
        Removes n cookies from the jar.
        Raises ValueError if there aren't that many cookies in the jar.
        """
        if n < 0 or n > self._size:
            raise ValueError("Cannot withdraw that many cookies: not enough in the jar.")
        self._size -= n

    @property
    def capacity(self):
        """
        Returns the capacity of the jar.
        """
        return self._capacity

    @property
    def size(self):
        """
        Returns the current number of cookies in the jar.
        """
        return self._size

# # Example usage:
# if __name__ == "__main__":
#     jar = Jar(10)
#     print(jar)  # Should print an empty string
#     jar.deposit(3)
#     print(jar)  # Should print "🍪🍪🍪"
#     jar.withdraw(1)
#     print(jar)  # Should print "🍪🍪"
#     print("Capacity:", jar.capacity)  # Should print "Capacity: 10"
#     print("Size:", jar.size)  # Should print "Size: 2"
