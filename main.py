print("Program starting.")

number = int(input("Insert a positive integer: "))

sequence = [number]
steps = 0

if number > 0:
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        sequence.append(number)
        steps += 1

print(" -> ".join(str(n) for n in sequence))
print(f"Sequence had {steps} total steps.")

print("\nProgram ending.")