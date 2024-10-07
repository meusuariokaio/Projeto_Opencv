#Transformar inverter preto/branco
from deoldify import device
from deoldify.device_id import DeviceId
import torch

# Escolha o dispositivo (GPU ou CPU)
device.set(device=DeviceId.GPU0)
if not torch.cuda.is_available():
    print("GPU não disponível. Usando CPU.")
    device.set(device=DeviceId.CPU)

from deoldify.visualize import *
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

colorizer = get_image_colorizer(artistic=True)

# Caminho para a imagem em preto e branco
source_path = 'caminho/para/sua/imagem_preto_e_branco.jpg'
render_factor = 35  # Ajuste este valor conforme necessário

# Colorir a imagem
result_path = colorizer.get_transformed_image(path=source_path, render_factor=render_factor)
