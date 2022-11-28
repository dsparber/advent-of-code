from functools import reduce


class Parser:

    @staticmethod
    def parse_package(bits):
        type_id = int(bits[3:6], base=2)
        match type_id:
            case 4: return Parser.parse_literal(bits[6:])
            case _: return Parser.parse_operator(bits[6:], type_id)

    @staticmethod
    def parse_literal(bits):
        numeric_bitstring = ""
        for offset in range(0, len(bits), 5):
            numeric_bitstring += bits[offset + 1:offset + 5]
            if bits[offset] == '0':
                return bits[offset+5:], int(numeric_bitstring, base=2)

    @staticmethod
    def parse_operator(bits, type_id):
        length_type_id = bits[0]
        match length_type_id:
            case '0': bits, values = Parser.sub_packets_length_in_bits(bits[1:])
            case _: bits, values = Parser.sub_packets_number(bits[1:])

        match type_id:
            case 0: value = sum(values)
            case 1: value = reduce(lambda x, y: x * y, values)
            case 2: value = min(values)
            case 3: value = max(values)
            case 5: value = 1 if values[0] > values[1] else 0
            case 6: value = 1 if values[0] < values[1] else 0
            case 7: value = 1 if values[0] == values[1] else 0

        return bits, value

    @staticmethod
    def sub_packets_length_in_bits(bits):
        length = int(bits[:15], base=2)
        bits = bits[15:]
        values = []
        while length > 0:
            remaining_bits, value = Parser.parse_package(bits)
            length -= len(bits) - len(remaining_bits)
            bits = remaining_bits
            values.append(value)

        return bits, values

    @staticmethod
    def sub_packets_number(bits):
        number = int(bits[:11], base=2)
        bits = bits[11:]
        values = []
        for _ in range(number):
            bits, value = Parser.parse_package(bits)
            values.append(value)

        return bits, values


with open('input') as f:
    hex_string = f.readlines()[0].strip()

    bitstring = "".join([f"{int(char, base=16):04b}" for char in hex_string])
    _, version_sum = Parser.parse_package(bitstring)
    print(version_sum)
