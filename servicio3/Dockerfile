# Usamos la imagen base de Python con Alpine
FROM python:3.9-alpine

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /servicio3

# Copiamos el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instalamos las dependencias
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos al directorio de trabajo
COPY . .

# Exponemos el puerto 5000 para que sea accesible desde fuera del contenedor
EXPOSE 5002

# Comando para ejecutar la aplicación
CMD ["python3", "app.py"]