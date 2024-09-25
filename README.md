# LAB-calificaciones
## Implementado por Oscar AG
**Autor**: Toñi Reina **Revisores**: Alfonso Bengoa, Fermín Cruz  **Fecha última modificación**: 22/09/2023

Crea tres módulos en un proyecto Python (`calificaciones.py`,`calificaciones_test.py` y `calificaciones_ui.py`) e implementa los siguientes ejercicios. Separa la definición de las funciones, incluyéndolas en el módulo `calificaciones.py`, de la invocación para probar esas funciones, incluyéndolas en el módulo `calificaciones_test.py`.

### Ejercicio 1 

Se quiere ayudar a los alumnos de Fundamentos de Programación a calcular su nota en la asignatura. Para resolver un problema, antes hay que entenderlo, así que, antes de implementar los apartados siguientes, vamos a explicar el problema a resolver.


#### Apartado a

Escribe una función en el módulo 'calificaciones'  llamada `nota_teoria` que, dadas las notas de los dos exámenes teóricos de un cuatrimestre, permita calcular la nota que un alumno tiene en el bloque teórico de ese cuatrimestre. La nota se calcula como la media de las notas de ambos cuatrimestres. Una nota con valor None indica que el alumno no se ha presentado al examen, y se considerará como un cero.

_Pruebas_:
Pruebe la función en el módulo `calificaciones_test.py` con los siguientes valores, siendo los dos números que están antes de la flecha las notas del primer y segundo exámen teórico, respectivamente, y el valor situado a la derecha de la flecha la nota obtenida.
```
9.1, 7.2 ==> 8.15
4.0, 6.0 ==> 5.0
4.0, 3.0 ==> 3.5
None, 3.0 ==>1.5
9.0, None ==> 4.5
None, None ==> 0.0
```

#### Apartado b

Escribe una función en el módulo 'calificaciones' llamada `nota_cuatrimestre` que, dadas una tupla con dos elementos (las notas de los exámenes teóricos de un cuatrimestre), y la nota del exámen práctico,
devuelva la nota obtenida en ese cuatrimestre. La nota del cuatrimestre, siempre que la media de los dos cuestionarios teóricos (llamémosla NT) sea superior o igual a 4, se calcula como 0,2* (NT) + 0,8 * P, siendo P la nota del examen práctico. Si la media no es superior a 4, la nota del cuatrimestre es 0. Un valor None en una nota indica que el alumno no se ha presentado al examen, y se considerará como un cero.


_Pruebas_:
Pruebe la función en el módulo `calificaciones_test.py` con los siguientes valores, siendo los números situados a la izquierda de la flecha las notas del primer examen teórico, del segundo y del examen práctico, respectivamente. La nota obtenida es el número situado a la derecha de la flecha.
```
9.1, 7.2, 8.1 ==> 8.110000000000001
4.0, 6.0, 5.0 ==> 5.0
4.0, 3.0, None ==> 0
None, 3.0, None  ==>0
9.0, None, 4.5 ==> 4.5
```
#### Apartado c

Escribe una función en el módulo 'calificaciones' llamada `nota_continua` que, dadas una tupla con las notas de los 4 exámenes teóricos del curso, y otra tupla con la nota de los 
dos exámenes prácticos, devuelva la nota obtenida por evaluación continua. La nota de la evaluación continua se calcula como la media de las notas de los dos cuatrimestres,
siempre que la nota de ambos cuatrimestres sea superior a 4. Si en alguno de los dos cuatrimestres la nota es inferior a 4, entonces la nota es el mínimo entre 4 y la nota media de los cuatrimestres. El valor None en una nota indica que el alumno no se ha presentado al examen, y se considerará como cero.

_Pruebas_:
Pruebe la función en el módulo `calificaciones_test.py` con los siguientes valores, siendo los números situados a la izquierda de la flecha las notas del primer examen teórico, del segundo y del examen práctico, respectivamente. La nota obtenida es el número situado a la derecha de la flecha.
```
    notas teoría:  9.6, 9.9,10.0, 9.8 notas_práctico: 9.7,9.5 ==> 9.645
    notas teoría: 4.4, 4.9, 5.1, 4.7 notas_práctico: 4.6,4.8 ==> 4.715
    notas teoría: 4.0, 6.0, 4.0, 3.0 notas_práctico: 5.0, None ==> 2.5
    notas teoría: 9.0, None, 4.0, 3.0 notas_práctico: 4.5, None ==> 2.25
```

#### Apartado d

Escribe una función en el módulo 'calificaciones_ui' llamada `solicita_notas` que solicite por teclado el nombre de un estudiante, las notas de los 4 cuestionarios de teoría y la de los 2 exámenes
prácticos y devuelva una tupla con todos los datos leídos (los campos de la tupla deben estar en el mismo orden en el que se han leído).  Implementa una segunda función llamada mostrar_notas que tome como entrada una tupla con los datos leidos por teclado y los muestre por consola.

En el mismo módulo invoque a estas funciones para solicitar a un usuario sus notas, y mostrarle sus resultados por consola, de la siguiente forma:

```
Introduzca su nombre: Toñi
Introduzca la nota del examen teórico 1 (- si no se ha presentado):
6.5
Introduzca la nota del examen teórico 2 (- si no se ha presentado):
7.8
Introduzca la nota del examen teórico 3 (- si no se ha presentado):
5.6
Introduzca la nota del examen teórico 4 (- si no se ha presentado):
6.0
Introduzca la nota del examen práctico 1 (- si no se ha presentado):
6.1
Introduzca la nota del examen práctico 2 (- si no se ha presentado):
5.0
Hola, Toñi
Tus notas del primer cuatrimestre son:
 teoria 7.15, práctica 6.1, cuatrimestre 6.3100000000000005
Tus notas del segundo cuatrimestre son:
 teoria 5.8, práctica 5.0, cuatrimestre 5.16
Tu nota final de la asignatura es 5.735
```
