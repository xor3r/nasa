import ctypes


class Node:
    def __init__(self, item, next=None):
        """
        Produces a newly constructed empty node.
        __init__: Any -> Node
        Fields: item stores any value
            next points to the next node in the list
        """
        self.item = item
        self.next = next

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.item)


class Multiset:
    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def __len__(self):
        length = 0
        head = self._head
        while head is not None:
            length += 1
            head = head.next
        return length

    def remove_all(self):
        removed = list()
        current = self._head
        removed.append(self._head.item)
        while current.next is not None:
            removed.append(current.next.item)
            current = current.next
        self._head = None
        return tuple(removed)

    def __str__(self):
        line = '{'
        current = self._head
        while current is not None:
            line += str(current.item) + ', '
            current = current.next
        return line + '}'

    def __getitem__(self, index):
        """Returns certain item according to index"""
        assert 0 <= index < len(self), "Array subscript out of range"
        i = 0
        while i != index:
            self._head = self._head.next


    def __iter__(self):
        """Iterator"""
        return self

    def __next__(self):
        """Returns next value from array"""
        if self._head is not None:
            item = self._head.item
            self._head = self._head.next
            return item
        else:
            raise StopIteration


class DynamicArray:
    """Dynamic array class creator"""
    def __init__(self):
        """Constructor for class DynamicArray"""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __setitem__(self, k, obj):
        """Assign item to the index"""
        if k > self._capacity:
            self._resize(k + 1)
        self._A[k] = obj

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]  # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = tuple(map(float, obj))
        self._n += 1

    def _resize(self, c):  # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    @staticmethod
    def _make_array(c):  # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        for j in range(self._n, k, -1):  # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value  # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value( or  raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:  # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item

                return  # exit immediately
        raise ValueError("value not found")  # only reached if no match
