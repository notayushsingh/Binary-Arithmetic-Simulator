# Binary Arithmetic Simulator

A Python-based binary arithmetic simulator that performs addition using fundamental digital logic gates.

## Features

- Decimal to binary conversion
- Binary to decimal conversion
- Logic gate implementations (AND, OR, XOR)
- Half adder implementation
- Full adder implementation
- Fixed-width binary addition
- Overflow detection

## Concepts Used

- Python classes and static methods
- Binary number systems
- Boolean logic
- Digital logic circuits
- Half adders and full adders
- Fixed-width arithmetic

## What This Calculator Does

✔ Binary addition using logic gates only 

✔ Configurable bit-width arithmetic 

✔ Unsigned overflow detection 

✔ Manual binary ↔ decimal conversion 

✔ Supports arbitrarily large inputs (clamped by bit-width)

## What This Calculator Doesn't Do Yet

✖ No subtraction (two’s complement not implemented yet) 

✖ No signed integers (only unsigned arithmetic) 

✖ No multiplication or division 

✖ No floating-point arithmetic

These are intentionally left out for future extension.

## Architecture Summary

```
Decimal Input
     ↓
Binary Conversion
     ↓
Bit Clamping (Fixed Width)
     ↓
Logic Gates → Adders → Carry Propagation
     ↓
Overflow Detection
     ↓
Binary Result
     ↓
Decimal Output
```

Each stage is explicit and inspectable.

## Usage

```python
from main import Calculator

result = Calculator.add_fixed(10, 20, bit_width=8)

print(result)
```

Example output:

```python
{
    'result': 30,
    'overflow': False,
    'bit_width': 8
}
```

## Future Improvements

- Support for negative numbers
- Subtraction using binary logic
- Additional arithmetic operations
- Input validation

## License

This project is licensed under the MIT License.
