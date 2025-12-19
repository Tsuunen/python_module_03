import sys

if (__name__ == "__main__"):
    print("=== Command Quest ===")
    if (len(sys.argv) <= 1):
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
    else:
        print("Program name:", sys.argv[0])
        print("Arguments received:", len(sys.argv) - 1)
        i = 0
        for arg in sys.argv:
            if (i > 0):
                print(f"Argument {i}: {arg}")
            i += 1
    print("Total arguments:", len(sys.argv))
