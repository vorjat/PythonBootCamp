print("    ", end="")
for i in range(10):
    print(f"{i:3}", end="")
print("")
print("")

for i in range(10):
    print(f"{i}   ", end="")
    for j in range(10):
        print(f"{i*j:3}", end="")
    print("")
