import mesher


# Define the function you want to find the maximum of

def f(x):
    return 1/(x**2 + 1)

# Set your interval and mesh

mesh = mesher.mesher(-1, 1, 100)
len(mesh)
# List of outputs

i = 0
output = []
while i <= (len(mesh) - 1):
    a = mesh[i]
    output.extend([f(a)])
    i = i + 1

print(f'With a mesh size of {len(mesh) - 1}, the max of f is approximately {max(output)}')
print(f'With a mesh size of {len(mesh) - 1}, the min of f is approximately {min(output)}')

