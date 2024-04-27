import hashlib
from bitarray import bitarray
from prettytable import PrettyTable

class BloomFilter:
    def __init__(self, filter_size):
        self.filter_size = filter_size
        self.bitset = bitarray(filter_size)
        self.bitset.setall(False)

    def add(self, key):
        hash1 = self.hash_function1(key)
        hash2 = self.hash_function2(key)
        hash3 = self.hash_function3(key)
        self.bitset[hash1] = True
        self.bitset[hash2] = True
        self.bitset[hash3] = True

    def contains(self, key):
        hash1 = self.hash_function1(key)
        hash2 = self.hash_function2(key)
        hash3 = self.hash_function3(key)
        return self.bitset[hash1] and self.bitset[hash2] and self.bitset[hash3]

    def display_bitset(self):
        bitset_str = ''.join('1' if bit else '0' for bit in self.bitset)
        print("Bitset:", bitset_str)

    def hash_function1(self, key):
        hash_obj = hashlib.sha256()
        hash_obj.update(key.encode())
        return int(hash_obj.hexdigest(), 16) % self.filter_size

    def hash_function2(self, key):
        hash_obj = hashlib.md5()
        hash_obj.update(key.encode())
        return int(hash_obj.hexdigest(), 16) % (self.filter_size - 1)

    def hash_function3(self, key):
        hash_obj = hashlib.sha1()
        hash_obj.update(key.encode())
        return int(hash_obj.hexdigest(), 16) % (self.filter_size - 2)


def bloom_join(employees, departments):
    FILTER_SIZE = 10
    bloom_filter = BloomFilter(FILTER_SIZE)
    for row in departments:
        key, dept = row.split(",")  # Splitting row into key and value
        if dept.strip() == "Marketing":  # Check if department is "Marketing"
            bloom_filter.add(key)

    result = []
    for row in employees:
        key, name = row.split(",")  # Splitting row into key and value
        if bloom_filter.contains(key):
            result.append((key, name, get_dept(key, departments)))

    bloom_filter.display_bitset()  # Display the bitset after adding elements

    return result

def get_dept(key, departments):
    for row in departments:
        row_key, dept = row.split(",")  # Splitting row into key and value
        if row_key == key:
            return dept
    return None

if __name__ == "__main__":
    employees = [
        "201, Shreyash",
        "202, Karan",
        "203, Aryan",
        "204, Virat",
        "205, Rohit"
    ]
    departments = [
        "201, Marketing",
        "202, Marketing",
        "204, HR",
        "206, Marketing",
        "207, Finance"
    ]

    result = bloom_join(employees, departments)

    # Create a PrettyTable object
    table = PrettyTable(['Key', 'Name', 'Department'])

    # Add rows to the table
    for row in result:
        table.add_row(row)

    # Print the table
    print(table)
