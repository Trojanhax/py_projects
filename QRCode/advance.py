import qrcode as qr
from PIL import Image

# Create a QRCode object
qrc = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Prompt the user for input
link = input('Enter your link: ')

# Add the data to the QR code
qrc.add_data(link)
qrc.make(fit=True)

# Create the QR code image
img = qrc.make_image(fill_color='red', back_color='green')

# Save the image to a file
img.save('you.png')
