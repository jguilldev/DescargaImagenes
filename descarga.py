import os
import cv2
from simple_image_download import simple_image_download as simp

# En el siguiente array se debe introducir el nombre de los personajes de los que se quieren descargar
# las imagenes
artists = ["Freddie Mercury", "Kurt Cobain", "David Bowie", "Ozzy Osbourne", "Amy Winehouse"]

# Instruccion de creacion de carpetas para crear las imagenes
BASE_DIR = "./images"
os.makedirs(BASE_DIR, exist_ok=True)

# Inicializa el descargador
downloader = simp.simple_image_download()

# Se necesita un modelo Haar Cascade (entrenamiento de reconocimiento facial) para detectar
# los rostros de los artistas
HAAR_CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)

# Se redimensiona el tamaño de las imagenes para hacerlos uniformes
IMG_SIZE = (256, 256)

#La siguiente es la funcion de deteccion de rostros y recorte de las fotos al tamaño deseado
def process_image(image_path, output_dir):
    try:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detecta rostros mediante el uso de harr (modelo de entrenamiento)
        faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Si se detecta al menos un rostro
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                # Recorta el primer rostro detectado
                face = img[y:y+h, x:x+w]
                resized_face = cv2.resize(face, IMG_SIZE)

                # Guarda la imagen procesada
                output_path = os.path.join(output_dir, os.path.basename(image_path))
                cv2.imwrite(output_path, resized_face)
                print(f"Imagen procesada: {output_path}")
                break  # Solo usamos el primer rostro detectado

    except Exception as e:
        print(f"Error procesando la imagen {image_path}: {e}")

# Descarga y procesa imágenes para cada uno de los artistas
for artist in artists:
    print(f"Descargando imágenes para: {artist}")

    # Crea la carpeta del artista, para luego guardar la imagen
    artist_dir = os.path.join(BASE_DIR, artist.replace(" ", "_"))
    os.makedirs(artist_dir, exist_ok=True)

    try:
        # Descarga 20 imágenes por artista (es posible, que algunas no se visualicen correctamente se deben revisar)
        downloader.download(artist, 20)

        # Busca imágenes descargadas en `simple_images`
        downloaded_images = [
            os.path.join("simple_images", file)
            for file in os.listdir("simple_images")
            if file.lower().startswith(artist.lower().replace(" ", "_"))
        ]

        if not downloaded_images:
            print(f"No se encontraron imágenes para {artist}.")
            continue

        # Procesa cada imagen descargada
        for image_path in downloaded_images:
            process_image(image_path, artist_dir)

    except Exception as e: #mensaje para el manejo de errores
        print(f"Error descargando imágenes para {artist}: {e}")

print("Proceso completado para todos los artistas.")#mensaje de finalizacion de todo el programa correctamente
