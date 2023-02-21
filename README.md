
# Proyecto Individual  - Data Engeneering y Machine Learning
Desarrollado por Maurén Hermosillo



## Consigna
A lo largo de de este proyecto veremos cómo se realizó un proyecto de Data Engineer y Machine Learning, en uno de los sectores empresariales más demandados en los últimos años, me refiero a las **plataformas de streaming**, la solicitud del proyecto se divide en dos importantes partes:

## 1ra. Data Engeneering
* Extraer datos de archivos
* Transformaciones
* Modelado de datos
* Montar API local

## 2da. Machine Learning
* Consumir los datos limpios
* EDA (analisis exploratorio de datos)
* Modelado
* Entrenamiento con datos limpios
* Predicciones con nuevos datos.

El resultado de todo esto, tendrá que ser un sistema de recomendación de películas y series en las plataformas de streaming principales, amazon, disney, netflix y hulu.
<hr> 

### Proceso de "ETL" (Extract, transform, load) en VisualStudioCode - Python:

**Nota:** Los archivos originales, así como los archivos que fueron resultando a lo largo de este proyecto, estarán alojados en este Drive**** para su consulta, ya que por el tamaño no es viable que esten en [github] https://github.com/Maurengit/Proyecto_Individual_1_DTS/tree/master

`EXTRACCIÓN DE DATOS`
1. Se utilizó Visual Studio con el lenguaje de programación Pyton y la librería pandas.
2. Se ingestaron los archivos csv proporcionados por el cliente, estaban divididos en dos grupos, el primero con información de las plataformas, Amazon, Disney, Netflix y Hulu, y el segundo con los ratings dados por usuarios.
3. Se hizo la ingesta en dataframes para su análisis exploratorio y conocer sus características principales


`TRANSFORMACIONES`
1. Generación del campo id
2. Reemplazo valores nulos del campo Rating por "g"
3. Conversión de date_added al formato adecuado (AAAA-mm-dd)
4. Conversión de campos de texto a minuscula
5. Separación de columna "duration" en dos ("duration_int" y "duration_type")
6.  Unificar 4 plataformas a través de la función “concat” en un dataframe único "gdf_completo" facilitando el código de las consultas a desarrollar
7.  Exportar CSV final completo.csv y por el peso del archivo se transformó a un .parquet con el mismo nombre con todas las transformaciones **** Drive
Todo lo descrito anteriormente se puede revisar en el archivo [Explorando-merge.ipynb]https://github.com/Maurengit/Proyecto_Individual_1_DTS/blob/master/Explorando_merge.ipynb
  
  <hr> 

## Desarrollo API:

`CONSULTAS A REALIZAR`

1. Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))
2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))
3. Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))
4. Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))

Se puede revisar el código de las funciones en el archivo [consultas01.ipynb]https://github.com/Maurengit/Proyecto_Individual_1_DTS/blob/master/consultas01.ipynb


<hr>

### Deployment: Se utilizó el framework FastAPI, junto con uvicorn para perminirnos trabajar en un ambiente local y posteriormnete Se utilizó Deta.space para un ambiente público. 
1. Generación de archivo [main.py]https://github.com/Maurengit/Proyecto_Individual_1_DTS/blob/master/main.py
2. Importación de las librerías a utilizar
3. Declaración de la creación de la API 
4. Declaración de la ruta de acceso para la base de datos (consultas.cvs)
5. Creación de un directorio índex con mensaje de bienvenida a la interfaz
6. Desarrollo de las consultas
7. Creación de una cuenta en Deta.space
8. Publicación al público de las consultas, se puede revisar en este [enlace:] https://deta.space/discovery/r/k56gavvdiltpbpz5 ingrese /docs

**Nota:** Para realizar las consultas en deta.space considere:
**Platform -Plataformas** únicamente y con minúsculas, amazon, disney, netflix y hulu
**Year - Año** El formato es numérico, ejemplo: 2021
**Score** Se refiere al puntaje dado por el usuario, esto en un rango del 1 al 5
**Duracion - type** Se realiza únicamnete en minutos, ejemlo: min

<hr>


## 2da. Machine Learning

`CONSUMIR LOS DATOS LIMPIOS`
1. Debido al tamaño del dataset con todos los datos se hizo un archivo .parquet que es un archivo optimizado y es mas eficaz siendo binario, esto nos ayuda a optimizar las consultas, lo hacemos mediante la librería de pyarrow  Drive****

`EDA (analisis exploratorio de datos)`
1. Se ingesta nuestro archivo completo.parquet
2. se utilizó la libreria dataprep para el Anális Exploratorio de Datos, esta librería nos brinda un análisis general de manera visual datos estructurados y sin estructurar para el análisis y detección de anomalías.
3. Se puede ver en el archivo [EDA.ipynb]https://github.com/Maurengit/Proyecto_Individual_1_DTS/blob/master/EDA.ipynb
4. Se realizó una exportación a un archivo html, para que sea más fácil su navegacion [reporte_eda.html]https://github.com/Maurengit/Proyecto_Individual_1_DTS/blob/master/reporte_eda.html

`MODELADO`
1. Para el modelado nos ayudamos de la librería Surprise en conjunto con pandas
2. Y como el desarrollo de modelos es muy demandante para los equipos, también se utilizó google colab Drive...  y lo pase también a github Modelo.ipynb  ....
3. Se siguió trabajando con el archivo completo.parquet, que contiene todos los datos Drive ****
4. Se verifica que no existan datos nulos, y se toma la decisión que para el desarrollo de este modelo sólamente se requeren tres campos de del dataset que son: id (identificador único de películas), userId(identificador único de cada usuario) y calificación (o score que es la puntuación que cada usuario le dió a determinadas películas o series)
5. Para sistema de recomendaciones funciona muy bien SVD (Singular Value Decomposition) SVD es una técnica matemática poderosa que se utiliza en los sistemas de recomendación para analizar la matriz de interacciones entre los usuarios y los elementos y descomponerla en matrices más simples que contienen información sobre los patrones de comportamiento de los usuarios y las características de los elementos. Esto permite mejorar la precisión y eficiencia del sistema de recomendación al reducir el ruido y la redundancia en la matriz de interacciones.

`ENTRENAMIENTO DE DATOS LIMPIOS`
1. Se dividieron los datos en conjuntos de entrenamiento y prueba, para esto se hicieron varias divisiones, para pruebas 1%, 5%, 15%, 25% y 50%
2. El mejor resultado fue el 25% y es el que se presenta
3. Una vez que se entrenó el modelo se guardó para ser utilizado en un futuro. modelo_SVD_entrenado.pkl ****

`PREDICCIONES DE NUEVOS DATOS`
1. Una vez entrenado el modelo podemos utilizarlo para hacer predicciones
2. Se hace al azar un predicción para usuario y película

`EVALUACION`
1. Se evalúa el modelo en el conjunto de prueba
2. Se imprime la precisión del modelo por el accuracy.rmse

`OPTIMIZACIÓN DE HIPERPÁMETROS`
1. Se realiza un validación cruzada esto nos sirve para evaluar modelos de ML mediante el entrenamiento de varios modelos de ML en subconjuntos de los datos de entrada disponibles y evaluarlos con el subconjunto complementario de los datos, nos ayuda a detectar sobre ajustes.



#### [Link a video explicativo confeccionado para equipo de data analytics](https://www.youtube.com/watch?v=o7A5xAoOQqE "Proyecto Individual data engineer - Henry's bootcamp")

<hr> 
