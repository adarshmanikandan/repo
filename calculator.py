import sys

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    if len(sys.argv) == 4:
        a, op, b = float(sys.argv[1]), sys.argv[2], float(sys.argv[3])
        ops = {"add": add, "sub": subtract, "mul": multiply, "div": divide}
        print(f"Result: {ops[op](a, b)}")
        return
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
    print("10 / 0 =", divide(10, 0))

if __name__ == "__main__":
    main()
