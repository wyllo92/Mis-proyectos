# # import requests
# # from bs4 import BeautifulSoup
# # import pandas as pd
# # import os
# # from datetime import datetime
# # from urllib.parse import urljoin
# # import urllib.parse


# # def get_first_article_url(url, link_selectors):
# #     response = requests.get(url)
# #     soup = BeautifulSoup(response.content, 'html.parser')

# #     # Busca los enlaces de artículos usando el selector proporcionado
# #     article_links = soup.select(link_selectors)

# #     if article_links:
# #         first_article_url = article_links[0]['href']
# #         return first_article_url
# #     else:
# #         print(f"No se encontraron enlaces de artículos utilizando el selector: {link_selectors}")
# #         return None


# # def get_pagespeed_metrics(url):
# #     base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

# #     estrategias = ["mobile", "desktop"]
# #     categorias = ["performance", "accessibility", "best-practices", "seo",]

# #     resultados = []

# #     try:
# #         for version in estrategias:
# #             params = {
# #                 "url": url,
# #                 "strategy": version,
# #                 "category": categorias
# #             }
# #             response = requests.get(base_url, params=params)
# #             response.raise_for_status()
# #             data = response.json()

# #             performance_score = data["lighthouseResult"]["categories"]["performance"]["score"]
# #             accesibility = data["lighthouseResult"]["categories"].get("accessibility", {}).get("score", '')
# #             best_practices = data["lighthouseResult"]["categories"].get("best-practices", {}).get("score", '')
# #             seo = data["lighthouseResult"]["categories"].get("seo", {}).get("score", '')
# #             fcp = data['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
# #             tbt = data['lighthouseResult']['audits']['total-blocking-time']['displayValue']
# #             si = data['lighthouseResult']['audits']['speed-index']['displayValue']
# #             lcp = data['lighthouseResult']['audits']['largest-contentful-paint']['displayValue']
# #             cls = data['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue']
# #             fid = data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['percentile'] / 1000
# #             inp = data["lighthouseResult"]["audits"].get("interactive", {}).get("displayValue", '')
# #             ttfb = data['loadingExperience']['metrics']['EXPERIMENTAL_TIME_TO_FIRST_BYTE']['percentile'] / 1000

# #             fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# #             resultados.append({
# #                 "Fecha": fecha_actual,
# #                 "url": url,
# #                 "Plataforma": version,
# #                 "Performance": performance_score,
# #                 "Accesibility": accesibility,
# #                 "Best Practices": best_practices,
# #                 "SEO": seo,
# #                 "First Contentful Paint (FCP)": fcp,
# #                 "Total Blocking Time (TBT)": tbt,
# #                 "Speed Index (SI)": si,
# #                 "Largest Contentful Paint (LCP)": lcp,             
# #                 "Cumulative Layout Shift (CLS)": cls,     
# #                 "First Input Delay (FID)": fid,
# #                 "Interaction to Next Paint (INP)": inp,
# #                 "Time to First Byte (TTFB)": ttfb
# #             })
# #         print(f"Obteniendo datos para la URL: {url}")
# #     except requests.exceptions.RequestException as e:
# #         print(f"Error al obtener datos de la API de PageSpeed para la URL {url}: {e}")
# #     except KeyError as e:
# #         print(f"Error de clave al procesar datos de la API de PageSpeed para la URL {url}: {e}")
# #     except TypeError as e:
# #         print(f"Error de tipo al procesar datos de la API de PageSpeed para la URL {url}: {e}")       
# #     except requests.exceptions.HTTPError as e:
# #         print(f"Error HTTP al obtener datos de la API de PageSpeed para la URL {url}: {e}")
# #     return resultados



# # def save_to_csv(df, file_name):
# #     try:
# #         # Utilizar urllib.parse para convertir el nombre proporcionado en un nombre de archivo seguro
# #         safe_file_name = urllib.parse.quote(file_name, safe='')
# #         file_path = f"{safe_file_name}_corewebvitals.csv"
        
# #         df.to_csv(file_path, index=False, mode='a', header=not os.path.exists(file_path), encoding='utf-8-sig')
# #         print(f"Datos guardados en el archivo CSV: {file_path}")
# #     except Exception as e:
# #         print(f"Error al guardar en el archivo CSV: {e}")


        

# # def job(main_page_urls):
# #     for main_page_url in main_page_urls:
# #         try:
# #             resultados_globales = get_pagespeed_metrics(main_page_url)
            
# #             if resultados_globales:
# #                 df = pd.DataFrame(resultados_globales)

# #                 # Obtén el nombre del archivo basado en la URL
# #                 file_name = f"{main_page_url.replace('/', '_').replace('.', '_')}"
                
# #                 save_to_csv(df, file_name)
                
# #         except Exception as e:
# #             print(f"Error durante el procesamiento de la URL: {main_page_url}. Detalles: {e}")

    
# # def urls_articulos(main_page_urls, link_selectors):
# #     urls_de_articulos = []
    
# #     for main_page_url, link_selector in zip(main_page_urls, link_selectors):
# #         try:
# #             url_del_articulo = get_first_article_url(main_page_url, link_selector)
            
# #             if url_del_articulo:
# #                 url_completa = urljoin(main_page_url, url_del_articulo)
# #                 urls_de_articulos.append(url_completa)
                
# #         except requests.exceptions.RequestException as e:
# #             print(f"Error al obtener datos de la página principal {main_page_url}: {e}")
# #         except Exception as e:
# #             print(f"Error durante el procesamiento de la URL: {main_page_url}. Detalles: {e}")

# #     main_page_urls.extend(urls_de_articulos)
    
# #     return main_page_urls
    

# # main_page_urls = [
# #     "https://www.pulzo.com",
# #     "https://www.infobae.com/colombia/",
# #     "https://www.elpais.com.co/",
# #     "https://www.eltiempo.com",
# #     "https://www.bluradio.com",
# #     "https://www.theguardian.com/international",
# #     "https://elcomercio.pe",
# #     "https://www.lanacion.com.ar"
# # ]

# # link_selectors = [
# #     "a[href^='/deportes/']",
# #     "a[href^='/colombia/']",
# #     "a[href^='/cali/']",
# #     "a[href^='/colombia/otras-ciudades/']",
# #     "a[href^='https://www.bluradio.com/deportes/']",
# #     "a[href^='/technology/']",
# #     "a[href^='/deporte-total/futbol-peruano/']",
# #     "a[href^='/deportes/']"
# # ]

# # main_page_urls = urls_articulos(main_page_urls, link_selectors)
# # print(main_page_urls)

# # job(main_page_urls)


# # schedule.every().day.at("09:00").do(job, urls=[main_page_url])

# # while True:
# #     schedule.run_pending()
# #     time.sleep(1)



# codigo de prueba con funciones para el amp
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import os
# from datetime import datetime
# from urllib.parse import urljoin, quote

# def get_first_article_url(url, link_selector):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Busca los enlaces de artículos usando el selector proporcionado
#     article_links = soup.select(link_selector)

#     if article_links:
#         first_article_url = article_links[0]['href']
#         return first_article_url
#     else:
#         print(f"No se encontraron enlaces de artículos utilizando el selector: {link_selector}")
#         return None

# def get_amp_article_urls(urls, link_selectors):
#     amp_urls = []

#     for url, link_selector in zip(urls, link_selectors):
#         try:
#             amp_url = get_amp_article_url(url, link_selector)

#             if amp_url:
#                 amp_urls.append(amp_url)

#         except requests.exceptions.RequestException as e:
#             print(f"Error al obtener datos de la página principal {url}: {e}")
#         except Exception as e:
#             print(f"Error durante el procesamiento de la URL: {url}. Detalles: {e}")

#     return amp_urls


# def get_pagespeed_metrics(url):
#     base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

#     estrategias = ["mobile", "desktop"]
#     categorias = ["performance", "accessibility", "best-practices", "seo"]

#     resultados = []

#     try:
#         for version in estrategias:
#             params = {
#                 "url": url,
#                 "strategy": version,
#                 "category": categorias
#             }
#             response = requests.get(base_url, params=params)
#             response.raise_for_status()
#             data = response.json()

#             resultados.append({
#                 "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "url": url,
#                 "Plataforma": version,
#                 "Performance": data["lighthouseResult"]["categories"]["performance"]["score"],
#                 "Accesibilidad": data["lighthouseResult"]["categories"].get("accessibility", {}).get("score", ''),
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
#     except requests.exceptions.RequestException as e:
#         print(f"Error al obtener datos de la API de PageSpeed para la URL {url}: {e}")
#     except KeyError as e:
#         print(f"Error de clave al procesar datos de la API de PageSpeed para la URL {url}: {e}")
#     except TypeError as e:
#         print(f"Error de tipo al procesar datos de la API de PageSpeed para la URL {url}: {e}")
#     except requests.exceptions.HTTPError as e:
#         print(f"Error HTTP al obtener datos de la API de PageSpeed para la URL {url}: {e}")
#     return resultados


# def save_to_csv(df, file_name):
#     try:
#         # Utilizar urllib.parse para convertir el nombre proporcionado en un nombre de archivo seguro
#         safe_file_name = quote(file_name, safe='')
#         file_path = f"{safe_file_name}_corewebvitals2.csv"

#         # Verificar si el archivo CSV existe antes de intentar escribir en él
#         if not os.path.exists(file_path):
#             df.to_csv(file_path, index=False, encoding='utf-8-sig')
#             print(f"Archivo CSV creado: {file_path}")
#         else:
#             df.to_csv(file_path, index=False, mode='a', header=False, encoding='utf-8-sig')
#             print(f"Datos adicionales guardados en el archivo CSV: {file_path}")
#     except Exception as e:
#         print(f"Error al guardar en el archivo CSV: {e}")

# def job(main_page_urls, custom_file_names):
#     # Obtener las primeras 8 URLs como URLs de home
#     home_urls = main_page_urls[:8]

#     # Iterar sobre todas las URLs proporcionadas
#     for main_page_url, custom_file_name in zip(main_page_urls, custom_file_names):
#         try:
#             # Obtener las métricas de PageSpeed para la URL actual
#             resultados_globales = get_pagespeed_metrics(main_page_url)

#             # Verificar si se obtuvieron métricas
#             if resultados_globales:
#                 # Crear un DataFrame con las métricas
#                 df = pd.DataFrame(resultados_globales)

#                 # Determinar el nombre de archivo
#                 file_name = "home" if main_page_url in home_urls else custom_file_name

#                 # Llamar a save_to_csv con el nombre de archivo
#                 save_to_csv(df, file_name)

#         except Exception as e:
#             # Manejar cualquier error durante el procesamiento de la URL
#             print(f"Error durante el procesamiento de la URL: {main_page_url}. Detalles: {e}")


# def urls_articulos(main_page_urls, link_selectors):
#     urls_de_articulos = []

#     for main_page_url, link_selector in zip(main_page_urls, link_selectors):
#         try:
#             url_articulo = get_first_article_url(main_page_url, link_selector)

#             if url_articulo:
#                 url_completa = urljoin(main_page_url, url_articulo)
#                 urls_de_articulos.append(url_completa)

#         except requests.exceptions.RequestException as e:
#             print(f"Error al obtener datos de la página principal {main_page_url}: {e}")
#         except Exception as e:
#             print(f"Error durante el procesamiento de la URL: {main_page_url}. Detalles: {e}")

#     main_page_urls.extend(urls_de_articulos)

#     return main_page_urls

# def urls_amp(main_page_urls, link_selectors):
#     amp_urls = []

#     for main_page_url, link_selector in zip(main_page_urls, link_selectors):
#         try:
#             amp_url = get_amp_article_url(main_page_url, link_selector)

#             if amp_url:
#                 amp_urls.append(amp_url)

#         except requests.exceptions.RequestException as e:
#             print(f"Error al obtener datos de la página principal {main_page_url}: {e}")
#         except Exception as e:
#             print(f"Error durante el procesamiento de la URL: {main_page_url}. Detalles: {e}")
            
#     main_page_urls.extend(amp_urls)

#     return main_page_urls



# main_page_urls = [
#     "https://www.pulzo.com",
#     "https://www.infobae.com/colombia/",
#     "https://www.elpais.com.co/",
#     "https://www.eltiempo.com",
#     "https://www.bluradio.com",
#     "https://www.theguardian.com/international",
#     "https://elcomercio.pe",
#     "https://www.lanacion.com.ar"
# ]

# link_selectors = [
#     "a[href^='/deportes/']",
#     "a[href^='/colombia/']",
#     "a[href^='/cali/']",
#     "a[href^='/colombia/otras-ciudades/']",
#     "a[href^='https://www.bluradio.com/deportes/']",
#     "a[href^='/technology/']",
#     "a[href^='/deporte-total/futbol-peruano/']",
#     "a[href^='/deportes/']"
# ]

# # Lista de nombres personalizados para cada URL
# custom_file_names = [
#     "pulzo_articulo",
#     "infobae_articulo",
#     "elpais_articulo",
#     "eltiempo_articulo",
#     "bluradio_articulo",
#     "theguardian_articulo",
#     "elcomercio_articulo",
#     "lanacion_articulo",
# ]

# main_page_urls = urls_articulos(main_page_urls, link_selectors)
# main_page_urls = urls_amp(main_page_urls, link_selectors)

# # Obtener las URLs AMP de las URLs principales
# amp_urls = get_amp_article_urls(main_page_urls, link_selectors)
# print(amp_urls)

# job(main_page_urls, custom_file_names)






import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime
from urllib.parse import urljoin
import urllib.parse


def get_first_article_url(url, link_selectors):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Busca los enlaces de artículos usando el selector proporcionado
    article_links = soup.select(link_selectors)

    if article_links:
        first_article_url = article_links[0]['href']
        return first_article_url
    else:
        print(f"No se encontraron enlaces de artículos utilizando el selector: {link_selectors}")
        return None


def get_pagespeed_metrics(url):
    base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

    estrategias = ["mobile", "desktop"]
    categorias = ["performance", "accessibility", "best-practices", "seo",]

    resultados = []

    try:
        for version in estrategias:
            params = {
                "url": url,
                "strategy": version,
                "category": categorias
            }
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()


            resultados.append({
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "url": url,
                "Plataforma": version,
                "Performance": data["lighthouseResult"]["categories"]["performance"]["score"],
                "Accesibility": data["lighthouseResult"]["categories"].get("accessibility", {}).get("score", ''),
                "Best Practices": data["lighthouseResult"]["categories"].get("best-practices", {}).get("score", ''),
                "SEO": data["lighthouseResult"]["categories"].get("seo", {}).get("score", ''),
                "First Contentful Paint (FCP)": data['lighthouseResult']['audits']['first-contentful-paint']['displayValue'],
                "Total Blocking Time (TBT)": data['lighthouseResult']['audits']['total-blocking-time']['displayValue'],
                "Speed Index (SI)": data['lighthouseResult']['audits']['speed-index']['displayValue'],
                "Largest Contentful Paint (LCP)": data['lighthouseResult']['audits']['largest-contentful-paint']['displayValue'],             
                "Cumulative Layout Shift (CLS)": data['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue'],     
                "First Input Delay (FID)": data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['percentile'] / 1000,
                "Interaction to Next Paint (INP)": data["lighthouseResult"]["audits"].get("interactive", {}).get("displayValue", ''),
                "Time to First Byte (TTFB)": data['loadingExperience']['metrics']['EXPERIMENTAL_TIME_TO_FIRST_BYTE']['percentile'] / 1000
            })
        print(f"Obteniendo datos para la URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API de PageSpeed para la URL {url}: {e}")
    except KeyError as e:
        print(f"Error de clave al procesar datos de la API de PageSpeed para la URL {url}: {e}")
    except TypeError as e:
        print(f"Error de tipo al procesar datos de la API de PageSpeed para la URL {url}: {e}")       
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP al obtener datos de la API de PageSpeed para la URL {url}: {e}")
    return resultados



def save_to_csv(df, file_name):
    try:
        # Utilizar urllib.parse para convertir el nombre proporcionado en un nombre de archivo seguro
        safe_file_name = urllib.parse.quote(file_name, safe='')
        file_path = f"{safe_file_name}_corewebvitals.csv"
        
        df.to_csv(file_path, index=False, mode='a', header=not os.path.exists(file_path), encoding='utf-8-sig')
        print(f"Datos guardados en el archivo CSV: {file_path}")
    except Exception as e:
        print(f"Error al guardar en el archivo CSV: {e}")


def job(main_page_urls, custom_file_names):
    home_urls = main_page_urls[:8]

    for main_page_url, custom_file_name in zip(main_page_urls, custom_file_names):
        try:
            resultados_globales = get_pagespeed_metrics(main_page_url)

            if resultados_globales:
                df = pd.DataFrame(resultados_globales)
                file_name = "home" if main_page_url in home_urls else custom_file_name
                save_to_csv(df, file_name)

        except Exception as e:
            print(f"Error durante el procesamiento de la URL: {main_page_url}. Detalles: {e}")

    
def urls_articulos(main_page_urls, link_selectors):
    urls_de_articulos = []

    for main_page_url, link_selector in zip(main_page_urls, link_selectors):
        try:
            url_del_articulo = get_first_article_url(main_page_url, link_selector)

            if url_del_articulo:
                url_completa = urljoin(main_page_url, url_del_articulo)
                urls_de_articulos.append(url_completa)

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de la página principal {main_page_url}: {e}")
        except Exception as e:
            print(f"Error durante el procesamiento de la URL: {main_page_url}. Detalles: {e}")

    return main_page_urls + urls_de_articulos
    

main_page_urls = [
    "https://www.pulzo.com",
    "https://www.infobae.com/colombia/",
    "https://www.elpais.com.co/",
    "https://www.eltiempo.com",
    "https://www.bluradio.com",
    "https://www.theguardian.com/international",
    "https://elcomercio.pe",
    "https://www.lanacion.com.ar"
]

link_selectors = [
    "a[href^='/deportes/']",
    "a[href^='/colombia/']",
    "a[href^='/cali/']",
    "a[href^='/colombia/otras-ciudades/']",
    "a[href^='https://www.bluradio.com/deportes/']",
    "a[href^='/technology/']",
    "a[href^='/deporte-total/futbol-peruano/']",
    "a[href^='/deportes/']"
]

custom_file_names = [
    "pulzo",
    "infobae",
    "elpais",
    "eltiempo",
    "blueradio",
    "theguardian",
    "elcomercio",
    "lanacion",   
    "pulzo_articulo",
    "infobae_articulo",
    "elpais_articulo",
    "eltiempo_aruculo",
    "blueradio_ariculo",
    "theguardian_articulo",
    "elcomercio_articulo",
    "lanacion_articulo",   
]

main_page_urls = urls_articulos(main_page_urls, link_selectors)
print(main_page_urls)

job(main_page_urls, custom_file_names)


