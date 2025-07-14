# Algoritmo de Dijkstra Paralelo
 
Este proyecto implementa el algoritmo de Dijkstra con paralelismo explícito utilizando Python y el módulo `multiprocessing`. Fue desarrollado como parte del trabajo recuperativo para la asignatura **Computación Paralela y Distribuida** de la Universidad Tecnológica Metropolitana.
 
## Profesor
 
Sebastián Salazar Molina  
Departamento de Computación e Informática  
Universidad Tecnológica Metropolitana
 
## Fecha de entrega
 
15 de julio de 2025 - 23:59:59 (hora continental de Chile)
 
---
 
## Descripción
 
El programa permite calcular la ruta más corta desde un vértice origen hacia todos los demás vértices de un grafo dirigido y con pesos positivos. Se lee la matriz de adyacencia desde línea de comandos, así como el vértice inicial y la ruta donde se guardará la salida.
 
La sección de **relajación de vecinos** está paralelizada con `multiprocessing.Pool`, lo que permite aprovechar arquitecturas multicore.
 
---
 
## Requisitos
 
- Python 3.8 o superior
- Compatible con:
  - Windows (usando `multiprocessing.Manager`)
  - Linux / Ubuntu 24.04 LTS (descomentando `set_start_method('fork')`)
 
---
 
## Ejecución
 
### Sintaxis:
 
```bash
python dijkstra_parallel.py "[[matriz_de_adyacencia]]" vertice_inicial "ruta_archivo_salida"

### Ejemplo
```bash
python dijkstra_parallel.py "[[0,10,0,0,5],[0,0,1,0,2],[0,0,0,4,0],[7,0,6,0,0],[0,3,9,2,0]]" 0 "resultados.txt"

### Resultados:
Vértice         Distancia desde el origen
0               0
1               8
2               9
3               7
4               5

 
