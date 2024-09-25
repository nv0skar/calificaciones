# Oscar AG - 2024

from calificaciones import nota_teoria, nota_practica, nota_cuatrimestre, nota_continua, THEORIC_EXAMS_PERIOD, PRACTICE_EXAMS_PERIOD

import sys, time

def clear():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def ask(val: str) -> float | None:
    while True:
        mark = input('\033[1;33m\033[5m¿Cuál es su nota del {} (-)? >>\033[0m '.format(val))
        clear()
        try: return float(mark)
        except: 
            if len(mark) == 0 or mark == '-': return None
            else: 
                print("La nota introducida no es válida...")
                time.sleep(2)
                clear()

def main():
    name = input("\033[1;33m\033[5mIntroduzca su nombre >>\033[0m ")
    clear()
    
    compound = ([ask('examen teórico 1'), ask('examen teórico 2'), ask('examen teórico 3'), ask('examen teórico 4')], [ask('examen práctico 1'), ask('examen práctico 2')])

    first_half_theory_mark = nota_teoria(compound[0][0:THEORIC_EXAMS_PERIOD])
    second_half_theory_mark = nota_teoria(compound[0][THEORIC_EXAMS_PERIOD::])

    first_half_practice_mark = nota_teoria(compound[1][0:PRACTICE_EXAMS_PERIOD])
    second_half_practice_mark = nota_teoria(compound[1][PRACTICE_EXAMS_PERIOD::])

    first_half_mark = nota_cuatrimestre((compound[0][0:THEORIC_EXAMS_PERIOD], compound[1][0:PRACTICE_EXAMS_PERIOD]))
    second_half_mark = nota_cuatrimestre((compound[0][THEORIC_EXAMS_PERIOD::], compound[1][PRACTICE_EXAMS_PERIOD::]))

    final_mark = nota_continua(compound)

    print('Hola {}\nTus notas del primer cuatrimestre son: teoría \033[1m{}\033[0m, práctica \033[1m{}\033[0m, cuatrimestre \033[1m{}\033[0m\nTus notas del segundo cuatrimestre son: teoría \033[1m{}\033[0m, práctica \033[1m{}\033[0m, cuatrimestre \033[1m{}\033[0m\nTu nota final de la asignatura es \033[1m\033[1;35m{}\033[0m'.format(
        name, first_half_theory_mark, first_half_practice_mark, first_half_mark, second_half_theory_mark, second_half_practice_mark, second_half_mark, final_mark
    ))
