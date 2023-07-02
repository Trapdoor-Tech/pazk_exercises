def multilinear_extension(f_values, r, p):
    l = len(r)
    result = 0
    # Iterate through all w in {0, 1}^l
    for i in range(2**l):
        # Convert i to binary representation to get w
        w = [int(x) for x in format(i, '0' + str(l) + 'b')]
        term = f_values[i]
        # Calculate χₑ(w)(x₁, ..., xₗ)
        for j in range(l):
            term *= (r[j] * w[j] + (1 - r[j]) * (1 - w[j]))
        # Sum it up
        result += term
        result %= p # Reduce modulo p
    return result

# Example usage:
p = 11 # Choose a prime
# Function f: {0, 1}^2 -> F_p
# f(0, 0) = 1, f(0, 1) = 2, f(1, 0) = 3, f(1, 1) = 4
f_values = [3, 4, 1, 2]
# Evaluate the multilinear extension at r = (1, 2) in F_p
r = [2, 4]
output = multilinear_extension(f_values, r, p)
print("f̃(r) =", output)