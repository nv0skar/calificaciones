# Oscar AG - 2024

from calificaciones import nota_teoria, nota_cuatrimestre, nota_continua

def test_nota_teoria():
    assert nota_teoria([9.1, 7.2]) == 8.15
    assert nota_teoria([4, 3]) == 3.5
    assert nota_teoria([None, 3]) == 1.5
    assert nota_teoria([9.0, None]) == 4.5
    assert nota_teoria([None, None]) == 0

def test_nota_cuatrimestre():
    assert nota_cuatrimestre(([9.1, 7.2], [8.1])) == 8.11
    assert nota_cuatrimestre(([4.0, 3.0], [None])) == 0
    assert nota_cuatrimestre(([None, 3.0], [None])) == 0
    assert nota_cuatrimestre(([9.0, None], [4.5])) == 4.5

def test_nota_continua():
    assert nota_continua(([9.6, 9.9, 10, 9.8], [9.7, 9.5])) == 9.64
    assert nota_continua(([4.4, 4.9, 5.1, 4.7], [4.6, 4.8])) == 4.71
    assert nota_continua(([4, 6, 4, 3], [5, None])) == 2.5
    assert nota_continua(([9, None, 4, 3], [4.5, None])) == 2.25

if __name__ == '__main__':
    test_nota_teoria()
    test_nota_cuatrimestre()
    test_nota_continua()
    print("-> tests passed!")