count = 0

for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        count += 1

print(f"Jest {count} takich liczb")