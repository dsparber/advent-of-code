class Parser:

    @staticmethod
    def parse_package(bits):
        version = int(bits[0:3], base=2)
        type_id = int(bits[3:6], base=2)

        match type_id:
            case 4: remaining_bits, version_sum = Parser.parse_literal(bits[6:])
            case _: remaining_bits, version_sum = Parser.parse_operator(bits[6:])

        return remaining_bits, version_sum + version

    @staticmethod
    def parse_literal(bits):
        numeric_bitstring = ""
        for offset in range(0, len(bits), 5):
            numeric_bitstring += bits[offset + 1:offset + 5]
            if bits[offset] == '0':
                value = int(numeric_bitstring, base=2)
                return bits[offset+5:], 0

    @staticmethod
    def parse_operator(bits):
        length_type_id = bits[0]
        match length_type_id:
            case '0': return Parser.sub_packets_length_in_bits(bits[1:])
            case '1': return Parser.sub_packets_number(bits[1:])

    @staticmethod
    def sub_packets_length_in_bits(bits):
        length = int(bits[:15], base=2)
        bits = bits[15:]
        version_sum = 0
        while length > 0:
            remaining_bits, v_sum = Parser.parse_package(bits)
            version_sum += v_sum
            length -= len(bits) - len(remaining_bits)
            bits = remaining_bits

        return bits, version_sum

    @staticmethod
    def sub_packets_number(bits):
        number = int(bits[:11], base=2)
        bits = bits[11:]
        version_sum = 0
        for _ in range(number):
            bits, v_sum = Parser.parse_package(bits)
            version_sum += v_sum

        return bits, version_sum


with open('input') as f:
    hex_string = f.readlines()[0].strip()

    bitstring = "".join([f"{int(char, base=16):04b}" for char in hex_string])
    _, version_sum = Parser.parse_package(bitstring)
    print(version_sum)
