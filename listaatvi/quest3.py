def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def arranjo(n, p):
    return fatorial(n) // fatorial(n - p)

def combinacao(n, r):
    return fatorial(n) // (fatorial(r) * fatorial(n - r))
n = 5
p = 3
r = 2
    
print(f"Arranjo A({n},{p}) = {arranjo(n, p)}")
print(f"Combinação C({n},{r}) = {combinacao(n, r)}")
