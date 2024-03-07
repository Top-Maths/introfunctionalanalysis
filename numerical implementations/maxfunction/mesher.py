def mesher(a, b, n):

    i = 0
    mesh = []
    while (i <= n):
        mesh.extend([a + 0.5**i*(a + b)])
        i = i + 1

    print(mesh)


mesher(0, 1, 2)
