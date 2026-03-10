# SEO Audit Agent 

Este projeto contém um **agente de AI em DSPy** para auxiliar em auditorias de SEO. de websites. A ferramenta conta com um crawler para capturar a estrutura da pagina, integração com o google search console e com o Google Trends.


## Estrutura

- `crawler.py`: script principal que realiza a coleta de dados do site.
- `requirements.txt`: dependências do Python necessárias.

## Como usar

1. Crie um ambiente virtual e instale as dependências:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Execute o crawler:
   ```powershell
   python crawler.py
   ```

## Preparação para GitHub

- Adicione todos os arquivos ao repositório:
  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  ```
- Crie o repositório no GitHub e conecte-o:
  ```bash
  git remote add origin <url-do-repositorio>
  git push -u origin main
  ```

## Ignorar arquivos

O arquivo `.gitignore` já inclui configurações comuns para projetos Python, incluindo ambientes virtuais, caches e arquivos temporários.
