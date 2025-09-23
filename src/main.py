#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python src/main.py <op> <a> <b>")
        print("op: add | sub")
        sys.exit(1)

    op, a_str, b_str = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("Error: a와 b는 숫자여야 한다.")
        sys.exit(1)

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    else:
        print("Error: 현재 버전은 add|sub만 지원한다.")
        sys.exit(1)

    print(int(result) if float(result).is_integer() else result)

if __name__ == "__main__":
    main()
