# %%
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV de vuelos
df_vuelos = pd.read_csv('C:/Users/crist/OneDrive/Documentos/Septimo Cuatrimestre/Examen Primer Parcial/flights.csv')
df_vuelos.head()

# Mostrar el dataframe de vuelos
print(df_vuelos)

# %%
# Verificación de valores faltantes en el conjunto de datos
valores_faltantes = df_vuelos.isnull().sum()

# Mostrar valores faltantes
valores_faltantes

# Imputación de valores faltantes en 'DepDel15' en función de 'DepDelay'
df_vuelos['DepDel15'] = df_vuelos['DepDelay'].apply(lambda x: 1 if x >= 15 else 0)

# Comprobación de valores atípicos en DepDelay y ArrDelay usando estadísticas descriptivas
estadisticas_retrasos = df_vuelos[['DepDelay', 'ArrDelay']].describe()

# Mostrar las estadísticas descriptivas de las columnas de retrasos
estadisticas_retrasos

# Filtrar filas donde DepDelay o ArrDelay sea mayor a 600 minutos (valores atípicos)
df_limpio = df_vuelos[(df_vuelos['DepDelay'] <= 600) & (df_vuelos['ArrDelay'] <= 600)]

# Verificar las nuevas estadísticas después de eliminar valores atípicos
estadisticas_retrasos_limpios = df_limpio[['DepDelay', 'ArrDelay']].describe()

# Mostrar las estadísticas actualizadas
estadisticas_retrasos_limpios

# Agrupar por aerolínea para comparar el rendimiento en retraso de llegada
retraso_llegada_aerolinea = df_limpio.groupby('Carrier')['ArrDelay'].mean().sort_values(ascending=False)

# Agrupar por día de la semana para ver si hay diferencias en los retrasos de llegada
retraso_llegada_dia_semana = df_limpio.groupby('DayOfWeek')['ArrDelay'].mean().sort_values()

# Agrupar por aeropuerto de origen para encontrar el aeropuerto con mayor retraso promedio de salida
retraso_salida_aeropuerto = df_limpio.groupby('OriginAirportName')['DepDelay'].mean().sort_values(ascending=False).head(10)

# Mostrar resultados
retraso_llegada_aerolinea, retraso_llegada_dia_semana, retraso_salida_aeropuerto

# %%
# 1. Gráfico de barras - Retraso promedio de llegada por aerolínea
print("Retraso de llegada por aerolínea:\n", retraso_llegada_aerolinea)
plt.figure(figsize=(10, 6))
retraso_llegada_aerolinea.plot(kind='bar', color='skyblue')
plt.title('Retraso promedio de llegada por aerolínea')
plt.ylabel('Retraso promedio de llegada (min)')
plt.xticks(rotation=90)
plt.show()

# %%
# 2. Gráfico circular - Retraso promedio de llegada por día de la semana
print("Retraso de llegada por día de la semana:\n", retraso_llegada_dia_semana)
plt.figure(figsize=(6, 6))
retraso_llegada_dia_semana.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'gold', 'lightgreen', 'lightskyblue', 'lightpink', 'orange', 'lightblue'])
plt.title('Distribución de retraso de llegada por día de la semana')
plt.ylabel('')
plt.show()

# %%
# 3. Gráfico de dispersión - DepDelay vs ArrDelay
print("Gráfico de dispersión de DepDelay vs ArrDelay:")
plt.figure(figsize=(10, 6))
plt.scatter(df_limpio['DepDelay'], df_limpio['ArrDelay'], alpha=0.2)
plt.title('DepDelay vs ArrDelay')
plt.xlabel('Retraso de salida (min)')
plt.ylabel('Retraso de llegada (min)')
plt.show()

# %%
# 4. Histograma - Distribución de DepDelay
print("Distribución de DepDelay:")
plt.figure(figsize=(10, 6))
df_limpio['DepDelay'].plot(kind='hist', bins=30, color='purple')
plt.title('Distribución de retrasos de salida')
plt.xlabel('Retraso de salida (min)')
plt.show()

# %%
# 5. Gráfico de líneas - Retraso de llegada por día de la semana
print("Gráfico de líneas - Retraso promedio de llegada por día de la semana:")
plt.figure(figsize=(10, 6))
retraso_llegada_dia_semana.plot(kind='line', marker='o', color='green')
plt.title('Retraso promedio de llegada por día de la semana')
plt.ylabel('Retraso promedio de llegada (min)')
plt.xlabel('Día de la semana')
plt.show()

# %%
# 6. Diagrama de cajas - DepDelay por aerolínea
print("Diagrama de cajas - Retraso de salida por aerolínea:")
plt.figure(figsize=(10, 6))
df_limpio.boxplot(column='DepDelay', by='Carrier', grid=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución del retraso de salida por aerolínea')
plt.suptitle('')  # Eliminar el título automático del diagrama de cajas
plt.xlabel('Aerolínea')
plt.ylabel('Retraso de salida (min)')
plt.show()

# %%
