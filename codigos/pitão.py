import qrcode

# URL onde o Flask estará rodando com o site
url = ""

# Gerar o QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Criar uma imagem do QR code
img = qr.make_image(fill="black", back_color="white")

# Salvar a imagem do QR code
img.save("qrcode_audio.png")