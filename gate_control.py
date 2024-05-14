import cv2
import fbase

def detect_and_decode_qr_codes(frame):
    
    qr_detector = cv2.QRCodeDetector()

    # Analiizar frame
    resultado, decoded_info, points, straight_qrcode = qr_detector.detectAndDecodeMulti(frame)
    # Se resultado diferente de zero entao detetou qr code
    # decoded_info: lista de strings com a info descodificada dos possiveis varios qr codes detetados
    # points: lista de coordenadas dos vertices dos qr codes
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

        # Sair do loop clicando no q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fechar janelas e parar de capturar imagem
    cap.release()
    cv2.destroyAllWindows()

def process_qr_code_data(data):
    # Para ja ainda nao se faz nada com o que é retirado do qr code
    print("Processing QR Code data:", data)

if __name__ == "__main__":
    main()
