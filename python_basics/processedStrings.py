def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(foo('Hola', 'chau', 'eugecapa'))