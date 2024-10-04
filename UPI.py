import qrcode
from PIL import Image

# Input UPI ID
upi_id = input("Enter your UPI ID: ")

# Construct UPI URLs
phone_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Function to generate and save QR code
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    img.show()

# Generate and save QR codes for each UPI service
generate_qr_code(phone_pay_url, 'phonepay_qr.png')
generate_qr_code(paytm_pay_url, 'paytm_qr.png')
generate_qr_code(google_pay_url, 'googlepay_qr.png')
