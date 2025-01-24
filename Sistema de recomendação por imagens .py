import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Carregar modelo pré-treinado VGG16 (sem a camada de classificação)
model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

def preprocess_image(image_path):
    """ Pré-processa uma imagem para extração de características """
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def extract_features(image_path):
    """ Extrai as características da imagem utilizando o modelo """
    img_array = preprocess_image(image_path)
    features = model.predict(img_array)
    features = features.flatten()  # Achatar o vetor de características
    return features

# Diretório de imagens
image_folder = 'images/'  # Substituir pelo caminho correto
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder)]

# Extrair características de todas as imagens
features_list = np.array([extract_features(img) for img in image_files])

# Comparação de similaridade com uma imagem de referência
query_image = 'images/query.jpg'  # Substituir pelo caminho correto
query_features = extract_features(query_image)

# Calcular similaridade usando distância do cosseno
similarities = cosine_similarity([query_features], features_list)

# Obter as imagens mais similares
sorted_indices = np.argsort(similarities[0])[::-1]
top_n = 5  # Número de imagens mais similares a exibir

# Mostrar resultados
plt.figure(figsize=(10, 5))
for i in range(top_n):
    img_path = image_files[sorted_indices[i]]
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.subplot(1, top_n, i + 1)
    plt.imshow(img)
    plt.title(f'Similaridade: {similarities[0][sorted_indices[i]]:.2f}')
    plt.axis('off')
plt.show()
