import sys

class Crypt:
    def __init__(self):
        self.dic = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäüöÄÜÖáÁàÀéóúíÉÓÚÍèìòùÈÌÒÙâêîôûÂÊÎÔÛ¹²³¼½¬,.;-_<>|^°!"§$%&/()=?\\}][{@€#\'~+*1234567890'

    def convert_to_numbers(self, string):
        return [ord(char) + 1 for char in string]
    
    def horizontal_checksum(self, array):
        sume = 0
        for i in array:
            sume = sume + i
        return sume	
    
    def get_base_by_checksum_and_length(self, checksum, length):
        return checksum - length + 1

    def convert_to_decimal(self, array, system, little = True):
        array = array[:]
        if little:
            while not 0 in array:
                for x in range(len(array)):
                    array[x] = array[x] - 1
        
        converted = 0
        for i in range(-len(array), 0):
            converted = converted + (array[i] * (system ** ((0 - i) - 1)))
        return converted
    
    def encrypt(self, string):
        string_numbers = self.convert_to_numbers(string)
        checksum = self.horizontal_checksum(string_numbers)
        length = len(string_numbers)
        data = self.convert_to_decimal(string_numbers, self.get_base_by_checksum_and_length(checksum, length))

        return self.unify(data), self.unify(checksum) + '::' + self.unify(length)

    def convert_from_decimal(self, number, system):
        ret = [int(i) for i in self.convert_raw(number, system).split(',')]
        if ret[0] == 0:
            return ret[1:]
        else:
            return ret

    def convert_raw(self, a, b):
        add = a%b
        if a<=1:
            return str(a)
        else:
            return str(self.convert_raw(a//b,b)) + ',' + str(add)

    def from_number_to_string(self, num):
        string = ''
        for each in num:
            string += chr(each-1)
        return string

    def fill_up(self, num, length):
        while len(num) < length:
            num.reverse()
            num.append(0)
            num.reverse()
        return num

    def count_up_to(self, num, to):
        while self.horizontal_checksum(num) < to:
            for i in range(len(num)):
                num[i] = num[i] + 1
        return num

    def unify(self, number):
        converted = self.convert_from_decimal(number, len(self.dic))
        for each in range(len(converted)):
            converted[each] = self.dic[converted[each]]
        return ''.join(converted)

    def deunify(self, string):
        string = [i for i in string]
        for char in range(len(string)):
            string[char] = self.dic.index(string[char])
        number = self.convert_to_decimal(string, len(self.dic), False)
        return number

    def convert_key(self, key):
        splitted = [self.deunify(i) for i in key.split('::')]
        return splitted[0], splitted[1]

    def decrypt(self, data, key):
        checksum, length = self.convert_key(key)
        data = self.deunify(data)
        system = self.get_base_by_checksum_and_length(checksum, length)
        in_system = self.count_up_to(self.fill_up(self.convert_from_decimal(data, system), length), checksum)
        return self.from_number_to_string(in_system)