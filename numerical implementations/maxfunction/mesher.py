def mesher(a, b, n):

    i = 0
    mesh = []
    while (i <= n):
        mesh.extend([a + i*((b - a)/(n))])
        i = i + 1

    return mesh
