import soporte

print('_____________     FASE 1. EXPLORACIÓN INICIAL Y LIMPIEZA DE DATOS     __________________')

print('________  APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME FELICIDAD 2023   __________')

#Llamamos a la función de leer el excel del ranking.
df_2023 = soporte.leer_csv('../data/input_data/DataForFigure21WHR2023.xls')
df_2023
print('Las 5 primeras filas del DataFrame del RANKING DE FELICIDAD 2023 son:\n')
print(df_2023.head())
print('.....................................................')

#Llamamos a la función para ver la info del ranking.
print('La INFORMACIÓN del DataFrame del RANKING DE FELICIDAD 2023 es:\n')
soporte.info_df(df_2023)
print('.....................................................')

#Llamamos a la función para ver el porcentaje de nulos de ranking.
print('El porcentaje de nulos numéricos por columna que hay en el RANKING DE FELICIDAD 2023 es:\n')
columnas_nulos_numericos = soporte.nulos_numericos(df_2023)
columnas_nulos_numericos
print('.....................................................')

#Llamamos a la función para ver como se distribuyen los valores dentro de estas categórias, y tratar de imputar los nulos numéricos.
print('La distribución de los valores únicos en las COLUMNAS CON NULOS NUMÉRICOS es de:\n')
soporte.distribucion_valores(df_2023, columnas_nulos_numericos)
print('.....................................................')

#Llamamos a la función para calcular la media y la mediana de las columnas con nulos.
soporte.media_mediana(df_2023, 'Healthy life expectancy', 'Explained by: Healthy life expectancy', 'Dystopia + residual')
print('.....................................................')

#Llamamos a la función para imputar las medianas a las columnas con nulos numéricos.
columnas_imputar = ['Healthy life expectancy', 'Explained by: Healthy life expectancy', 'Dystopia + residual']
soporte.imputar_mediana(df_2023, columnas_imputar)

#Llamamos a la función para igualar nombre columnas.
soporte.igualar_columnas(df_2023)

print('_________________   ALMACENAMIENTO DATAFRAME RANKING 2023   ________________________')

#Llamamos a la función para guardar el DF 2023 resultante en la carpeta output_data.
soporte.guardar_df(df_2023, 'ranking_2023')





print('________  APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME FELICIDAD HISTÓRICO   __________')

#Llamamos a la función de leer el excel del ranking.
df_historico = soporte.leer_csv('../data/input_data/DataForTable21WHR2023.xls')
df_historico
print('Las 5 primeras filas del DataFrame del RANKING DE FELICIDAD HISTÓRICO son:\n')
print(df_historico.head())
print('.....................................................')

#Llamamos a la función para ver la info del ranking.
print('La INFORMACIÓN del DataFrame del RANKING DE FELICIDAD HISTÓRICO es:\n')
soporte.info_df(df_historico)
print('.....................................................')

#Llamamos a la función para ver el porcentaje de nulos de ranking.
print('El porcentaje de nulos numéricos por columna que hay en el RANKING DE FELICIDAD HISTÓRICO es:\n')
columnas_nulos_numericos = soporte.nulos_numericos(df_historico)
columnas_nulos_numericos
print('.....................................................')

#Llamamos a la función para ver como se distribuyen los valores dentro de estas categórias, y tratar de imputar los nulos numéricos.
print('La distribución de los valores únicos en las COLUMNAS CON NULOS NUMÉRICOS es de:\n')
soporte.distribucion_valores(df_historico, columnas_nulos_numericos)
print('.....................................................')

#Llamamos a la función para calcular la media y la mediana de las columnas con nulos.
soporte.media_mediana(df_historico, 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Positive affect', 'Negative affect')
print('.....................................................')

#Llamamos a la función para imputar las medianas a las columnas con nulos numéricos.
columnas_imputar = ['Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Positive affect', 'Negative affect']
soporte.imputar_mediana(df_historico, columnas_imputar)

#Llamamos a la función para igualar nombre columnas.
soporte.igualar_columnas(df_historico)

print('_________________   ALMACENAMIENTO DATAFRAME RANKING 2023   ________________________')

#Llamamos a la función para guardar el DF 2023 resultante en la carpeta output_data.
soporte.guardar_df(df_historico, 'ranking_historico')