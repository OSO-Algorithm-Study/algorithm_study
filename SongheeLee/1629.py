import sys
input = sys.stdin.readline

def mul_mod(base, exponent):

    term = mul_mod(base, exponent//2)

    if exponent == 1:
        return base % C

    elif exponent % 2 == 0:
        return (term * term) % C
    
    else:
        return (base * term * term) % C

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(mul_mod(A, B))

