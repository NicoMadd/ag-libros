# Algoritmo Genetico de Seleccion de Libros

Algoritmo Genetico para la materia IA sobre libros

### Como setear ambiente

1. Instalar Python 3.x.x (3.10.2)
2. Configurar variables
    - Crear archivo _.env_ en el root del proyecto para setear variables
        - DATA_FILENAME: Setear el nombre del archivo dataset
        - DATA_DIR: El path al directorio desde el root donde estara guardado el dataset. **El directorio debe existir antes de correr el programa.**
        - DATASET_URL: La url de donde se baja el dataset
        - STATS_DIR: Directorio donde se guardaran los stats
3. Configurar dentro del archivo main.py las condiciones con las que se dara el algoritmo. Es decir, setear los criterios de Seleccion, Cruza y Mutacion, asi tmabien como las variables de probabilidad de mutacion.

### Como usar

1. Ejecutar el archivo main.py. Este te baja el dataset si no lo tenes descargado, si encuentra el archivo usa ese. Luego ejecuta los pasos basicos del algoritmo.
2. Al terminar mostrará un grafico con los datos de las corridas y guardara en el directorio _stats_ un archivo json logueando los datos de la corrida.

### Errores

Si tira algun error de modulos es necesario instalarlos. ¿Como se hace? Si ya tenes python instalado, ejecutar \*python -m pip install **modulo\***.
