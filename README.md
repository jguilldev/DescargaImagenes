Descarga y procesamiento de imágenes de artistas musicales
Este script automatiza la descarga de imágenes de artistas musicales, detecta y recorta los rostros de las imágenes descargadas, y guarda las imágenes procesadas en un formato uniforme.

Descripción
El código:

Utiliza la librería simple_image_download para descargar imágenes de Internet.
Detecta rostros en las imágenes utilizando un modelo Haar Cascade de OpenCV.
Recorta los rostros detectados y los redimensiona a dimensiones uniformes (256x256 píxeles).
Almacena las imágenes procesadas en una estructura de carpetas organizada por artista.
Este script es útil para proyectos que requieren un dataset de rostros de artistas musicales u otros artistas, ya sea para reconocimiento facial, entrenamiento de modelos de aprendizaje automático, o proyectos de arte generativo.

Requisitos previos
Python 3.8 o superior.

Librerías necesarias
Las siguientes librerías son necesarias para ejecutar el código:

OpenCV
simple_image_download
Instalación
Sigue estos pasos para instalar las dependencias:

Clona este repositorio o descarga el archivo del script.

Abre una terminal en la carpeta donde está el archivo.

Instala las librerías necesarias ejecutando:

ejecuta desde la terminal:

pip install opencv-python simple_image-download

Uso:
Asegúrate de que el archivo esté en la misma carpeta que este README.

Modifica la lista de artistas en el script para incluir los nombres de los artistas de los que quieras 

descargar imágenes:
Modifica esta linea en el archivo descarga.py por los artistas de tu gusto

artists = ["Freddie Mercury", "Kurt Cobain", "David Bowie", "Ozzy Osbourne", "Amy Winehouse"]

Ejecuta el script en tu terminal con el comando:

python descargas.py
Las imágenes procesadas se guardarán en la carpeta ./images, organizadas por artista.

Notas
La carpeta simple_images contiene las imágenes descargadas sin procesar. Si quieres eliminarlas después de procesarlas, puedes hacerlo manualmente.

Asegúrate de tener una conexión a Internet activa, ya que las imágenes se descargan directamente desde la web.


