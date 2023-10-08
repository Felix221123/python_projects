#this project generates a qr code based on the url provided 
import qrcode

def generate():
    print('\n')
    print('Prepare the url you would like to make as a QR code ')
    print('\n')
    user_url = input('paste the url here...')
    image = qrcode.make(user_url)
    image.save('myqrcode.png')
    print('\n')
    print('check your files for the image of the qr code')


generate()
    