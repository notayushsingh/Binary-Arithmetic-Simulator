class Calculator:
# --------INTERNAL-------
    @staticmethod
    def _AND(a,b):
        return 1 if a==1 and b ==1 else 0
    
    @staticmethod
    def _OR(a,b):
        return 1 if a==1 or b ==1 else 0

    @staticmethod
    def _XOR(a,b):
        return 1 if a != b else 0

    @staticmethod
    def _half_adder(a,b):
        return Calculator._XOR(a,b), Calculator._AND(a,b)

    @staticmethod
    def _full_adder(a,b,carry_in):
        sum1, carry1 = Calculator._half_adder(a,b)
        sum2, carry2 = Calculator._half_adder(sum1, carry_in)
        # carry_out = Calculator._OR(carry1, carry2)
        return sum2, Calculator._OR(carry1, carry2)

# ----------PUBLIC----------
    @staticmethod
    def decimal_to_binary(n):
        bits = []
        while n > 0:
            bits.append(n % 2)
            n = n//2
        return bits if bits else [0]

    @staticmethod
    def binary_to_decimal(bits):
        value = 0 
        power = 1 
        for bit in bits:
            if bit == 1:
                value += power 
            power *= 2
        return value

    @staticmethod
    def add_binary_fixed(a_bits, b_bits,bit_width):
        result = []
        carry = 0 
        overflow = False

        for i in range(max_len):
            a = a_bits[i] if i < len(a_bits) else 0
            b = b_bits[i] if i < len(b_bits) else 0

            sum_bit, carry = Calculator._full_adder(a,b,carry)
            result.append(sum_bit)

        if carry == 1:
            overflow = True
            # result.append(1)

        return result, overflow 

    @staticmethod
    def clamp_bits(bits, bit_width):
        return bits[:bit_width]

    @staticmethod
    def add_fixed(x,y,bit_width=16):
        a_bits = Calculator.clamp_bits(
            Calculator.decimal_to_binary(x),
            bit_width
        )

        b_bits = Calculator.clamp_bits(
            Calculator.decimal_to_binary(y), 
            bit_width
        )
    
        sum_bits, overflow = Calculator.add_binary_fixed(
            a_bits,
            b_bits,
            bit_width
        )

        result = Calculator.binary_to_decimal(sum_bits)

        return {
            "result": result,
            "overflow": overflow,
            "bit_width": bit_width
        }
