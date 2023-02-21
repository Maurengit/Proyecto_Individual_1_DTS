from fastapi import FastAPI 
import pandas as pd

# se instancia clase FastAPI
app = FastAPI(title= 'Maurén Hermosillo', description='Proyecto sobre modelo IA recomendación de plataformas')



#Se carga el dataset que contiene los datos a trabajar
test = pd.read_csv('consultas.csv')

#Consulta 1
#Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. 
#(la función debe llamarse get_max_duration(year, platform, duration_type))


@app.get("/get_max_duration/")
async def get_max_duration(platform:str, duration_type:str, year:int):
    if platform == "netflix":
            df_durat = test[(test["type"] == "movie") & (test["release_year"] == year) & (test["duration_type"] == duration_type) & (test["id"].str.findall("n"))] # Se hace el filtro con las 3 condiciones por plataf
    elif platform == "disney":
            df_durat = test[(test["type"] == "movie") & (test["release_year"] == year) & (test["duration_type"] == duration_type) & (test["id"].str.findall("d"))]
    elif platform == "hulu":
            df_durat = test[(test["type"] == "movie") & (test["release_year"] == year) & (test["duration_type"] == duration_type) & (test["id"].str.findall("h"))]
    elif platform == "amazon":
            df_durat = test[(test["type"] == "movie") & (test["release_year"] == year) & (test["duration_type"] == duration_type) & (test["id"].str.findall("a"))]
    else:
            return "Lo siento, sólo tengo informacion sobre netflix, disney, hulu y amazon"
    
    result = df_durat[df_durat["duration_int"] == (df_durat["duration_int"].max())] # se evalúa el valor más alto
    return f'La Película de {platform} con mayor duración en {duration_type} del año {year} es: {result.iloc[0, 1]}' # accedemos al valor específico, título de la peli


#Consulta 2
#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año 
# (la función debe llamarse get_score_count(platform, scored, year))

@app.get("/get_score_count/")
async def get_score_count(platform:str, scored:int, year:int):
    df5 = test[(test["calificacion"] > scored ) & (test["release_year"] == year)]  #Filtro de busqueda por calificación y Año
    if platform == "netflix":
        df_gsc = df5[(df5["type"] == "movie") & (df5["id"].str.findall("n"))]       # Se hace busca la letra específica en una cadena te texto y se guarda en un df
    elif platform == "amazon":
        df_gsc = df5[(df5["type"] == "movie") & (df5["id"].str.findall("a"))] 
    elif platform == "hulu":
        df_gsc = df5[(df5["type"] == "movie") & (df5["id"].str.findall("h"))]
    elif platform == "disney":
        df_gsc = df5[(df5["type"] == "movie") & (df5["id"].str.findall("d"))]
    else:
        return "Revisa tu búsqueda, algo no está funcionando"

    return f'La cantidad de peliculas de {platform} del año {year} con puntaje {scored} es de: {df_gsc.shape[0]}'


#Consulta 3
#Cantidad de películas por plataforma con filtro de PLATAFORMA. 
# (La función debe llamarse get_count_platform(platform))

@app.get("/get_count_platform/")
async def get_count_platform(platform:str):
    if platform == "amazon":
        df_encontrado = test[test['id'].str.contains("a")] #Encuentra concidencia de la letra a en el df test columna id y lo guarda en df_encontrado
    elif platform == "disney":
        df_encontrado = test[test['id'].str.contains("d")]
    elif platform == "hulu":
        df_encontrado = test[test['id'].str.contains("h")]
    elif platform == "netflix":
        df_encontrado = test[test['id'].str.contains("n")]
    else:
        return 'Esa plaforma no la conozco, sólo tengo informacion sobre netflix, disney, hulu y amazon'
    
    result = df_encontrado['id'].count() #Cuenta los valores accediedo accediendo al primer elemento de la serie, que es el número de filas que cumplen con la condición

    return f'El catálogo tiene de la plataforma {platform} un total de {result} películas'

#Consulta 4
#Actor que más se repite según plataforma y año. 
# (La función debe llamarse get_actor(platform, year))

@app.get("/get_actor/")
async def get_actor(platform:str, year:int):
    if platform == "netflix":
            df_actor = test[(test["release_year"] == year) & (test["id"].str.contains("n"))] # Se hace el filtro con las 2 condiciones por plataf
    elif platform == "disney":
            df_actor = test[(test["release_year"] == year) & (test["id"].str.contains("d"))]
    elif platform == "hulu":
            df_actor = test[(test["release_year"] == year) & (test["id"].str.contains("h"))]
    elif platform == "amazon":
            df_actor = test[(test["release_year"] == year) & (test["id"].str.contains("a"))]
    else:
            return "Lo siento, sólo tengo informacion sobre netflix, disney, hulu y amazon"

    actores = str(df_actor['cast'])
    actores = actores.split(', ') #se separan los valores
    name_dict = {}
    for name in actores:
        if name in name_dict:
                name_dict[name] += 1
        else:
                name_dict[name] = 1
    result = max(name_dict, key=name_dict.get)


    return f'El actor que más de repite en result en el año {year} de la plataforma {platform} es:{result}'