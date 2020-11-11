import sys
from PIL import Image
from imagem import Imagem

def main():
    img = Imagem(sys.argv[1])
    img.ampliar()
    print("\n[1] Detector de bordas")
    print("[2] Máscara Box Blurring")
    print("[3] Máscara Gaussian Blur\n")
    aux = int(input("Digite o número da opção desejada: "))
    if aux == 1:
        img.detector_bordas()
    elif aux == 2:
        img.box_blurring()
    elif aux == 3:
        img.gaussian_blur()    
    
    img.exibir_imagens()


if __name__ == "__main__":
    main()