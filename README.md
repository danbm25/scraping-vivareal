# Scraping de Imóveis - Vivareal

Web scraping de lotes/terrenos à venda em Eusébio - CE usando Python e Selenium.

## 📋 Sobre o projeto

Este projeto coleta automaticamente dados de imóveis do site Vivareal, extraindo:
- 📍 Localização (bairro)
- 🏠 Endereço (rua)
- 📐 Área do lote (m²)
- 💰 Preço

## 🛠️ Ferramentas utilizadas

- Python
- Selenium (automação do navegador)
- Pandas (organização e exportação dos dados)
- Google Chrome DevTools (para inspecionar a estrutura do site)

## ⚙️ Como executar

1. Clone o repositório
2. Instale as dependências:
   pip install selenium pandas
3. Execute o script:
   python3 scraping.py
4. O arquivo imoveis.csv será gerado na pasta do projeto

## 🚧 Dificuldades encontradas

- O site usa renderização dinâmica com JavaScript, então não foi possível usar requests diretamente
- A API interna do Vivareal bloqueou requisições externas via Cloudflare (erro 403)
- Os seletores CSS precisaram ser identificados manualmente pelo DevTools

## ✅ Resultado

30 imóveis coletados com sucesso e exportados para planilha CSV.
