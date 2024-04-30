# import requests
# import pandas as pd
# import os
# from datetime import datetime
# import schedule
# import time
# import json

# def get_pagespeed_pagina(url):
#     print("Entrando en get PageSpeed")

#     # Definir la URL base para la API de PageSpeed
#     base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

#     # Definir las estrategias y categorías para las métricas
#     estrategias = ["mobile", "desktop"]
#     categorias = ["performance", "accessibility", "best-practices", "seo"]

#     # Inicializar una lista para almacenar los resultados de las métricas
#     resultados = []

#     try:
#         print("Antes del bucle")

#         # Iterar sobre las estrategias (mobile y desktop)
#         for version in estrategias:
#             # Construir los parámetros de la solicitud para la API de PageSpeed
#             params = {"url": url, "strategy": version, "category": categorias}
            
#             # Hacer la solicitud a la API de PageSpeed utilizando la función make_request definida anteriormente
#             response = requests.get(base_url, params=params)
#             response.raise_for_status()
#             data = response.json()

#             print("Dentro del bucle")

#             # Agregar resultados al diccionario de resultados
            
#             resultados.append({
#                 "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "url": url,
#                 "Plataforma": version,
#                 "Performance": data["lighthouseResult"]["categories"]["performance"]["score"],
#                 "Accesibility": data["lighthouseResult"]["categories"].get("accessibility", {}).get("score", ''),
#                 "Best Practices": data["lighthouseResult"]["categories"].get("best-practices", {}).get("score", ''),
#                 "SEO": data["lighthouseResult"]["categories"].get("seo", {}).get("score", ''),
#                 "First Contentful Paint (FCP)": data['lighthouseResult']['audits']['first-contentful-paint']['displayValue'],
#                 "Total Blocking Time (TBT)": data['lighthouseResult']['audits']['total-blocking-time']['displayValue'],
#                 "Speed Index (SI)": data['lighthouseResult']['audits']['speed-index']['displayValue'],
#                 "Largest Contentful Paint (LCP)": data['lighthouseResult']['audits']['largest-contentful-paint']['displayValue'],             
#                 "Cumulative Layout Shift (CLS)": data['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue'],     
#                 "First Input Delay (FID)": data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['percentile'] / 1000,
#                 "Interaction to Next Paint (INP)": data["lighthouseResult"]["audits"].get("interactive", {}).get("displayValue", ''),
#                 "Time to First Byte (TTFB)": data['loadingExperience']['metrics']['EXPERIMENTAL_TIME_TO_FIRST_BYTE']['percentile'] / 1000
#             })

#         print(f"Obteniendo datos para la URL: {url}")

#     # Capturar excepciones relacionadas con solicitudes, claves no encontradas, tipos incorrectos y errores HTTP
#     except requests.exceptions.RequestException as e:
#         print(f"Error al obtener datos de la API de PageSpeed para la URL {url}: {e}")
#     except (KeyError, TypeError) as e:
#         print(f"Error al procesar datos de la API de PageSpeed para la URL {url}: {e}")
#     except requests.exceptions.HTTPError as e:
#         print(f"Error HTTP al obtener datos de la API de PageSpeed para la URL {url}: {e}")

#     # Imprimir mensaje de finalización y devolver la lista de resultados
#     print("Finalizado PageSpeed")
#     return resultados


# def save_to_csv(df):
#     file_path = "corewebvitals.csv"
#     try:
        
#         df.to_csv(file_path, index=False, mode='a', header=not os.path.exists(file_path), encoding='utf-8-sig')

#     except Exception as e:
#         print(f"Error al guardar en el archivo CSV: {e}")

# def job(urls):
#     resultados_globales = []

#     for url in urls:
#         resultados = get_pagespeed_pagina(url)
#         resultados_globales.extend(resultados)

#     df = pd.DataFrame(resultados_globales)
#     print("DataFrame creado correctamente")

#     save_to_csv(df)
#     print("Datos guardados en el archivo CSV")
    
# urls = [
#     "https://amp.theguardian.com/technology/2024/jan/19/tesla-battery-dying-cold-weather-charging-winter",
   
#     ]

# job(urls)
# schedule.every().day.at("09:00").do(job, urls=urls)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

#     # Ejecutar manualmente la función job


squares = [1, 4, 9, 16, 25]
print(squares[-3:])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
carro = 'letters'
print(carro)
['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
letters
['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters
[]