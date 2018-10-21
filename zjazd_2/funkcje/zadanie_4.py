def masowa_zamiana(*args, **kwargs):
    for arg in args:
        for kwarg in kwargs:
            if kwarg in arg:
                print(arg.replace(f'${kwarg}', str(kwargs[kwarg])))

masowa_zamiana("Tekst1$cena", "Tekst2$costam", "Tekst3$cena", cena=10, costam=5)
