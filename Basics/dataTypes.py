
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


#1. Text Type: str
text = "Hello, Python!"
print("Text (str):", text)
print("Type:", type(text))  # Output: <class 'str'>
print()

#2. Numeric Types: int, float, complex
num_int = 5
num_float = 5.5
num_complex = 3 + 4j
print("Integer (int):", num_int)
print("Type:", type(num_int))  # Output: <class 'int'>
print("Float (float):", num_float)
print("Type:", type(num_float))  # Output: <class 'float'>
print("Complex (complex):", num_complex)
print("Type:", type(num_complex))  # Output: <class 'complex'>
print()

#3. Sequence Types: list, tuple, range
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_range = range(5)
print("List (list):", my_list)
print("Type:", type(my_list))  # Output: <class 'list'>
print("Tuple (tuple):", my_tuple)
print("Type:", type(my_tuple))  # Output: <class 'tuple'>
print("Range (range):", my_range)
print("Type:", type(my_range))  # Output: <class 'range'>
print()

#4.Mapping Type: dict
my_dict = {"name": "Alice", "age": 30}
print("Dictionary (dict):", my_dict)
print("Type:", type(my_dict))  # Output: <class 'dict'>
print()

#5.Set Types: set, frozenset
my_set = {1, 2, 3}
my_frozenset = frozenset([1, 2, 3])
print("Set (set):", my_set)
print("Type:", type(my_set))  # Output: <class 'set'>
print("Frozenset (frozenset):", my_frozenset)
print("Type:", type(my_frozenset))  # Output: <class 'frozenset'>
print()

#6.Boolean Type: bool
my_bool = True
print("Boolean (bool):", my_bool)
print("Type:", type(my_bool))  # Output: <class 'bool'>
print()

#7.Binary Types: bytes, bytearray, memoryview
my_bytes = b"Hello"
my_bytearray = bytearray(5)
my_memoryview = memoryview(my_bytes)
print("Bytes (bytes):", my_bytes)
print("Type:", type(my_bytes))  # Output: <class 'bytes'>
print("Bytearray (bytearray):", my_bytearray)
print("Type:", type(my_bytearray))  # Output: <class 'bytearray'>
print("Memoryview (memoryview):", my_memoryview)
print("Type:", type(my_memoryview))  # Output: <class 'memoryview'>
print()

#8.None Type: NoneType
my_none = None
print("NoneType:", my_none)
print("Type:", type(my_none))  # Output: <class 'NoneType'>
