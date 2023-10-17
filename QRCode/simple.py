import qrcode as qr

image = qr.make(input('enter you link:-- '))
type(image)
image.save(input('enter you file name:-- '))

