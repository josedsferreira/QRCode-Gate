import cv2
import fbase
import gate
from time import time
from time import sleep
import threading

# Tempo para atualizar o codigo da gate
code_time = 60 * 10  # 10 mins
# Tempo de espera entre leitura de frames
loop_wait = 0.1
loop_wait_bool = False # Para desativar ou ativar a espera entre frames

time_of_auth = time()

def detect_and_decode_qr_codes(frame):
    
    qr_detector = cv2.QRCodeDetector()

    # Analiizar frame
    resultado, decoded_info, vertices, straight_qrcode = qr_detector.detectAndDecodeMulti(frame)
    # Se resultado diferente de zero entao detetou qr code
    # decoded_info: lista de strings com a info descodificada dos possiveis varios qr codes detetados
    # vertices: lista de coordenadas dos vertices dos qr codes
    # straight_qrcode: lista de numpy arrays que representam a imagem de um qr code

    # Printar info do qrcode e retornar
    if resultado != 0:
        for info in decoded_info:
            print("Detected QR Code:", info)
        return decoded_info
    else:
        return None

def main():
    # Começar captura de imaagem
    cap = cv2.VideoCapture(0)

    # começar o temporizador
    start_time = time()
    while True:
        


        # Capturar frame-by-frame
        resultado, frame = cap.read()

        # Verificar se frame foi capturado
        if not resultado:
            print("Failed to capture frame")
            break

        # mostrar frame
        cv2.imshow('Frame', frame)

        # Detetar QR Code e descodificar
        decoded_info = detect_and_decode_qr_codes(frame)

        # Process the data contained in the QR codes (replace this with your specific functionality)
        if decoded_info:
            for info in decoded_info:
                process_qr_code_data(info)

        # Atualizar o codigo a cada 10 mins
        elapsed_time = time() - start_time
        if elapsed_time > code_time:
            fbase.update_code() # Atualizar codigo na base de dados
            start_time = time() # Reset do temporizador

        # Sair do loop clicando no q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Esperar entre frames se loop_wait_bool for True, para poupança de recursos
        if loop_wait_bool:
            sleep(loop_wait)

    # Fechar janelas e parar de capturar imagem
    cap.release()
    cv2.destroyAllWindows()

def process_qr_code_data(data):
    #print("Processing QR Code data:", data)
    global time_of_auth
    if fbase.is_authorized(data):
        if time() - time_of_auth < 10:
            return
        else: time_of_auth = time()
        print("Authorized")
        threading.Thread(target=gate.openGate).start()
    else:
        print("Not Authorized")
    

if __name__ == "__main__":
    main()
