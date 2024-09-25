# Oscar AG - 2024

try: from typing import List, Tuple # For static type checking
except: pass

THEORIC_EXAMS_PERIOD = 2
PRACTICE_EXAMS_PERIOD = 1

Marks = List[float | None]

def nota(marks: Marks, precision=2) -> float:
    '''
    From a list of marks calculate the average with the given precision
    '''
    # Strip None(s) and convert them to 0
    for ix, elem in enumerate(marks):
        if elem == None: marks[ix] = 0
    return round(sum(marks) / len(marks), precision)

nota_teoria = nota
nota_practica = nota

def nota_cuatrimestre(compound: Tuple[Marks, Marks], precision=2) -> float | None: 
    '''
    Compute the four-month period mark
    (This allows `nota del examen práctico` to be greater than 1)
    '''
    (theoric_exams, practices_exams) = compound
    (average_theoric_exams, average_practices_exams) = (nota_teoria(theoric_exams, precision), nota_teoria(practices_exams, precision)) # Calculate averages...
    final = round(.2 * average_theoric_exams + .8 * average_practices_exams, precision) # Apply weighting
    return final if final >=4 else 0

def nota_continua(compound: Tuple[Marks, Marks], precision=2) -> float | None:
    '''
    Given two four-month period, compute the whole year's mark.
    ** This function will assume that each four-month period has `THEORIC_EXAMS_PERIOD` theoric exams and `PRACTICE_EXAMS_PERIOD` practice exam **
    '''
    # Check whether the input complies with the expected one...
    if len(compound[0]) > THEORIC_EXAMS_PERIOD * 2 or len(compound[1]) > PRACTICE_EXAMS_PERIOD * 2: raise BaseException
    first_half = (compound[0][0:THEORIC_EXAMS_PERIOD], compound[1][0:PRACTICE_EXAMS_PERIOD])
    second_half = (compound[0][THEORIC_EXAMS_PERIOD::], compound[1][PRACTICE_EXAMS_PERIOD::])
    (mark_first_half, mark_second_half) = (nota_cuatrimestre(first_half), nota_cuatrimestre(second_half))
    marks = [mark_first_half, mark_second_half]
    final = round(sum(marks) / len(marks), precision)
    if mark_first_half >= 4 and mark_second_half >= 4: return final
    else: return min([4, final])
