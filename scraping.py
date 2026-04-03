from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Abre o navegador automaticamente
driver = webdriver.Chrome()

# Link da pesquisa de lotes em Eusébio
url = "https://www.vivareal.com.br/venda/ceara/eusebio/lote-terreno_residencial/"
driver.get(url)

# Aguarda a página carregar completamente
time.sleep(5)

# Lista que vai guardar os dados de cada imóvel
imoveis = []

# Encontra todos os cards de imóveis na página
cards = driver.find_elements(By.CSS_SELECTOR, "li[data-cy='rp-property-cd']")

# Percorre cada card e extrai as informações
for card in cards:

    # Extrai o bairro/localização
    try:
        endereco = card.find_element(By.CSS_SELECTOR, "h2[data-cy='rp-cardProperty-location-txt']").text
        partes = endereco.split("\n")
        area = partes[0].replace("Lote/Terreno para comprar com ", "").replace(" em", "").strip()
        localizacao = partes[1] if len(partes) > 1 else "Não informado"
    except:
        area = "Não informado"
        localizacao = "Não informado"

    # Extrai o nome da rua
    try:
        rua = card.find_element(By.CSS_SELECTOR, "p[data-cy='rp-cardProperty-street-txt']").text
    except:
        rua = "Não informado"

    # Extrai o preço
    try:
        preco = card.find_element(By.CSS_SELECTOR, "div[data-cy='rp-cardProperty-price-txt'] p").text
    except:
        preco = "Não informado"

    # Adiciona os dados na lista
    imoveis.append({
        "Localização": localizacao,
        "Rua": rua,
        "Área (m²)": area,
        "Preço": preco
    })

# Organiza os dados em uma tabela
df = pd.DataFrame(imoveis)

# Mostra no terminal
print(df)
print(f"\nTotal de imóveis coletados: {len(imoveis)}")

# Salva em arquivo CSV
df.to_csv("imoveis.csv", index=False)
print("Arquivo CSV salvo com sucesso!")

# Fecha o navegador
driver.quit()