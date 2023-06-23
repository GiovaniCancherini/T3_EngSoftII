# Imagem base
FROM python:3.10

# Diretório de trabalho
WORKDIR /home

# Copiar arquivos necessários
COPY requirements.txt .
COPY src/main.py .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Definir variáveis de ambiente
ENV FLASK_APP=main.py

# Expôr a porta do servidor
EXPOSE 5000

# Comando para executar o servidor
CMD ["flask", "run", "--host=0.0.0.0"]
