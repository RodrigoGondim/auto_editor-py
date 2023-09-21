import os
from PIL import Image, ImageFilter
from time import sleep

# Especifique diretamente os caminhos de origem e destino
path_original = './img_original'
directory_png = './img_png'
directory_thumbnail = './img_thumbnail'
directory_filter = './img_filter'

# Welcome
print(f'{" Auto Editor Image ":~^60}')
sleep(1.2)
print(f'{" PNG ":-^60}')

# PNG
if not os.path.exists(directory_png):
    print(f'{"> Criando Pasta PNG"}')
    sleep(1.5)
    os.makedirs(directory_png)
    sleep(1.5)

# Itera sobre os arquivos no diretório de PNG
converted_img = 1
for filename in os.listdir(path_original):
    print(f'Uploading files: {converted_img} / {(len(os.listdir(path_original)))}  ')
    converted_img += 1
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(os.path.join(path_original, filename))  # Use os.path.join para formar o caminho completo
    img.save(os.path.join(directory_png, f'{clean_name}.png'), 'PNG')  # Adicione 'PNG' como formato
print('> All images are in PNG!')
sleep(1)


# Filter
print(f'{" Filter ":-^60}')
sleep(1.2)

if not os.path.exists(directory_filter):
    print(f'{"> Criando Pasta dos Filtros"}')
    sleep(1.5)
    os.makedirs(directory_filter)
    sleep(1.5)

# Itera sobre os arquivos no diretório Filtros
converted_img = 1
for filename in os.listdir(path_original):
    print(f'Applying filter to files: {converted_img} / {(len(os.listdir(path_original)))}  ')
    converted_img += 1
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(os.path.join(path_original, filename))
    img_sharpened = img.filter(ImageFilter.SHARPEN).filter(ImageFilter.DETAIL)
    img_sharpened.save(os.path.join(directory_filter, f'{clean_name}_SHARPENED_DETAIL.png'), 'PNG')
print('> All filters applied!')


# Thumbnail
print(f'{" Thumbnail ":-^60}')
sleep(1.2)

if not os.path.exists(directory_thumbnail):
    print(f'{"> Criando Pasta Thumbnail"}')
    sleep(1.5)
    os.makedirs(directory_thumbnail)
    sleep(1.5)

# Itera sobre os arquivos no diretório Thumbnail
converted_thumb = 1
for filename in os.listdir(directory_filter):
    print(f'Uploading files: {converted_thumb} / {(len(os.listdir(directory_filter)))}')
    converted_thumb += 1
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(os.path.join(directory_filter, filename))
    img.thumbnail((400, 400))
    img.save(os.path.join(directory_thumbnail, f'{clean_name}_thumbnail.png'), 'PNG')  # Adicione 'PNG' como formato

print('> All Thumbnails created!')
print(f'{" Good Job ":-^60}')
