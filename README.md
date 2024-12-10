
# INSTALACIÓN

## PARTE 1: Obtener los archivos del repositorio

OPCIÓN A (Para principiantes): Descarga directa
1. Ve al repositorio en GitHub
2. Haz clic en botón verde "Code"
3. Selecciona "Download ZIP"
4. Descomprime el archivo en tu computadora

OPCIÓN B (Para usuarios con conocimientos técnicos): Clonar repositorio
1. Asegúrate de tener Git instalado
2. Abre la terminal/Anaconda Prompt
3. Navega a la carpeta donde quieres guardar el proyecto
```bash
cd C:\Users\TuNombre\Documentos
```
4. Clona el repositorio:
```bash
git clone https://github.com/usuario/nombre-repositorio.git
```

## PARTE 2: Preparar entorno de trabajo
(Los pasos siguientes son idénticos para ambos métodos)

5. Abrir Anaconda Prompt
6. Crear entorno virtual
```bash
conda create -n proyecto_test python=3.11
```
7. Activar entorno
```bash
conda activate proyecto_test
```
8. Navegar a carpeta del proyecto
```bash
cd ruta/a/tu/proyecto
```
9. Instalar dependencias
```bash
pip install -r requirements.txt
```
10. Iniciar Jupyter
```bash
jupyter notebook
```

CONSEJOS:
- Si usas la opción de descarga, tendrás una carpeta con los archivos
- Si clonas, git descargará directamente los archivos
- Ambos métodos logran el mismo resultado

¿Te gustaría que profundice en alguno de estos pasos?
