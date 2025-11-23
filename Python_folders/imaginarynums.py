real_num = int(input("Enter a real number: "))
imaginary_num = int(input("Enter another number: "))
complex_num = complex(real_num, imaginary_num)

output = f"""
Full Complex Number: {complex_num}
Real Part: {complex_num.real:.0f}
Imaginary Part: {complex_num.imag:.0f}
"""
print(output.strip())