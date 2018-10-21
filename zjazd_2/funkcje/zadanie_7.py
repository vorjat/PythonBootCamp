def przytnij(data, start, stop):
    output = set()
    for i in data:
        if i >= start and i <= stop:
            output.add(i)

    print(output)


przytnij([1, 2, 3, 4, 5, 6, 7], 4, 6)

