users = {}

with open("dane/logs.txt") as f:
    for line in f:
        username, action, time = line.split(";")
        if username not in users:
            users.update({username: 0})
        if action == "LOGIN":
            users[username] -= int(time)
        if action == "LOGOUT":
            users[username] += int(time)
print("Czas przebywania w systemie:")

for k, v in users.items():
    print(f"- {k}: {v}")
