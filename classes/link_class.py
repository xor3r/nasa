import ctypes


class Array:
    """Class for representing array in Python"""
    def __init__(self, size):
		"""Constructor for class Array"""
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)

    # Returns the size of the array.
    def __len__(self):
		"""Checks length of an array"""
        return self._size

    # Gets the contents of the index element.
    def __getitem__(self, index):
		"""Returns certain item"""
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    # Puts the value in the array element at index position.
    def __setitem__(self, index, value):
		"""Sets certain item's value"""
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    # Clears the array by setting each element to the given value.
    def clear(self, value):
		"""Clears whole array"""
        for i in range(len(self)):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
		"""Returns iterative object"""
        return _ArrayIterator(self._elements)


# An iterator for the Array ADT.
class _ArrayIterator:
	"""Class for representing array's iterator"""
    def __init__(self, the_array):
		"""Constructor for class _ArrayIterator"""
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
		"""Returns iterative object of class"""
        return self

    def __next__(self):
		"""Gets next item"""
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration
