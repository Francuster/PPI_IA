import cv2
import numpy as np

# Base de datos de imágenes de huellas digitales (simulada)
database = {
    'usuario1': cv2.imread('img/huella1.jpg', cv2.IMREAD_GRAYSCALE),
    'usuario2': cv2.imread('img/huella2.jpg', cv2.IMREAD_GRAYSCALE),
    'usuario3': cv2.imread('img/huella3.jpg', cv2.IMREAD_GRAYSCALE)
}

def compare_fingerprints(fingerprint1, fingerprint2):
    # Calculamos la diferencia absoluta entre las dos imágenes
    difference = cv2.absdiff(fingerprint1, fingerprint2)
    return np.sum(difference)

def authenticate_fingerprint(input_fingerprint):
    min_difference = 150000 #float('inf')
    authenticated_user = None

    for username, stored_fingerprint in database.items():
        difference = compare_fingerprints(input_fingerprint, stored_fingerprint)
        
        if difference <= min_difference:
            min_difference = difference
            authenticated_user = username

    return authenticated_user


#input_fingerprint = cv2.imread('img/huella_a_comparar.jpg', cv2.IMREAD_GRAYSCALE)

def decode_and_verify(image_file):
    # Read the image file directly from memory
    nparr = np.fromstring(image_file.read(), np.uint8)
    input_fingerprint = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    # Autenticación de la huella digital capturada
    authenticated_user = authenticate_fingerprint(input_fingerprint)

    return authenticated_user;

def auth(input):
    try:
        # Simulación de captura de huella digital (cargando una imagen)
        input_fingerprint = cv2.imread(input, cv2.IMREAD_GRAYSCALE)
        # Autenticación de la huella digital capturada
        authenticated_user = authenticate_fingerprint(input_fingerprint)

        if authenticated_user:
            print(f'Autenticación exitosa. Bienvenido, {authenticated_user}.')
        else:
            print('Autenticación fallida. Usuario no reconocido.')
    except:
        print('direccion de imagen invalida.')

def login():
    print("Hi! Please enter your fingerprint img path bellow. Type 'quit' to exit.")
    while True:
        user_input = input("Fingerprint path: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        auth(user_input)

# Run the chatbot
if __name__ == "__main__":
    login()