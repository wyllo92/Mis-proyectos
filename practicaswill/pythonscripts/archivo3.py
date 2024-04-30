import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime
from urllib.parse import urljoin, quote
from retrying import retry
import time


def get_url_home_article(main_page_urls, link_selectors):
    urls_totals = []

    for main_page_url, link_selector in zip(main_page_urls, link_selectors):
        try:
            response = requests.get(main_page_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            article_links = soup.select(link_selector)

            if article_links:
                url_del_articulo = urljoin(main_page_url, article_links[0]['href'])
                urls_totals.append(url_del_articulo)
            else:
                print(f"No se encontraron enlaces de artículos utilizando el selector: {link_selector}")

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de la página principal {main_page_url}: {e}")
            time.sleep(2)
        except Exception as e:
            print(f"Error durante el procesamiento de la URL: {main_page_url}. Detalles: {e}")
            time.sleep(2)

    print("Finalizado artículo")
    return main_page_urls + urls_totals


def get_amp_version(urls):
    url_resultados = []

    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            enlace_amp = soup.find('link', {'rel': 'amphtml'})

            if enlace_amp:
                url_resultados.append(enlace_amp.get('href'))

        except requests.exceptions.RequestException as e:
            print(f'Error al realizar la solicitud para {url}: {e}')
            time.sleep(2)

    print("Finalizado AMP")
    return url_resultados


@retry(wait_fixed=2000, stop_max_attempt_number=3)
def make_request(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response


def get_pagespeed_metrics(urls):
    print("Entrando en get PageSpeed")

    base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    estrategias = ["mobile", "desktop"]
    categorias = ["performance", "accessibility", "best-practices", "seo"]
    resultados = []

    try:
        print("Antes del bucle")

        # Obtener el índice de la URL en la lista para determinar la estrategia a partir de la URL número 17
        index_url = main_page_urls.index(urls)

        # Iterar sobre las estrategias (mobile y desktop)
        for index, version in enumerate(estrategias):
            # Utilizar ambas estrategias para las primeras 16 URLs
            if index == 1 and index_url >= 16:
                break

            params = {"url": urls, "strategy": version, "category": categorias}
            
            response = make_request(base_url, params=params)
            data = response.json()

            print("Dentro del bucle")

            # Agregar resultados al diccionario de resultados
            
            resultados.append({
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "url": urls,
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
                "First Input Delay (FID)": data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['percentile']/1000,
                "Interaction to Next Paint (INP)": data['loadingExperience']['metrics']['INTERACTION_TO_NEXT_PAINT']['percentile'],
                "Time to First Byte (TTFB)": data['loadingExperience']['metrics']['EXPERIMENTAL_TIME_TO_FIRST_BYTE']['percentile']/1000
            })

        print(f"Obteniendo datos para la URL: {urls}")

    # Capturar excepciones relacionadas con solicitudes, claves no encontradas, tipos incorrectos y errores HTTP
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API de PageSpeed para la URL {urls}: {e}")
    except (KeyError, TypeError) as e:
        print(f"Error al procesar datos de la API de PageSpeed para la URL {urls}: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP al obtener datos de la API de PageSpeed para la URL {urls}: {e}")

    # Imprimir mensaje de finalización y devolver la lista de resultados
    print("Finalizado PageSpeed")
    return resultados


def save_to_csv(df, file_name):
    try:
        safe_file_name = quote(file_name, safe='')
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

    print("Finalizado job")

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
    "a[href^='/cali/'][target='_self']",
    "a[href^='/bogota/']",
    "a[href^='https://www.bluradio.com/deportes/']",
    "a.dcr-lv2v9o",
    "a.fs-wi__img-link.fs-img-link",
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
    "eltiempo_articulo",
    "blueradio_articulo",
    "theguardian_articulo",
    "elcomercio_articulo",
    "lanacion_articulo",
    "pulzo_amp",
    "infobae_amp",
    "elpais_amp",
    "eltiempo_amp",
    "blueradio_amp",
    "theguardian_amp",
]

main_page_urls = get_url_home_article(main_page_urls, link_selectors)
url_para_amp = main_page_urls[8:]
main_page_urls += get_amp_version(url_para_amp)
print(main_page_urls)
job(main_page_urls, custom_file_names)
