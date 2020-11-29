def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

def bylineread(filename):
    with open(filename) as f:
        line = f.readline().strip()
        while line:
            yield line
            line = f.readline().strip()


file_name = 'C:\\Users\\cnosc\\Desktop\\yield.txt'
with open(file_name, 'w') as f:
    for item in fab(100):
        f.write(str(item) + '\n')

read = bylineread(file_name)
print(read)

for item in read:
    print(item)
