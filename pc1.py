#!pip install pycryptodome
#!pip install pywhatkit

#SEND OTP CODE STARTS
import pywhatkit as kit
import datetime
import time

def send_whatsapp_message(phone_number, message):
    # Get the current time
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  # Send the message 2 minutes from now

    # Send the WhatsApp message
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        time.sleep(10)  
    except Exception as e:
        print(f"An error occurred: {e}")

#SEND OTP CODE ENDS

#3DES CODE STARTS

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64

# Triple DES key generation
def generate_triple_des_key():
    key = get_random_bytes(24)  
    return key

def encrypt_triple_des(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_text = plaintext + (8 - len(plaintext) % 8) * ' '  
    encrypted_text = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted_text).decode()

def generate_otp(length):
    otp = get_random_bytes(length)
    msg = "Hello your OTP is "+str(otp) +"."
    Send_Otp("+918660614659",msg)
    return otp

def apply_otp(text_bytes, otp_bytes):
    return bytes([b ^ o for b, o in zip(text_bytes, otp_bytes)])

def encrypt_with_otp(plaintext):
    triple_des_key = generate_triple_des_key()
    encrypted_text = encrypt_triple_des(triple_des_key, plaintext)

    otp = generate_otp(len(encrypted_text))

    encrypted_bytes = encrypted_text.encode()
    otp_encrypted = apply_otp(encrypted_bytes, otp)

    return base64.b64encode(otp_encrypted).decode(), base64.b64encode(otp).decode(), base64.b64encode(triple_des_key).decode()

def encrypt_message(plaintext):
    encrypted_text, otp, des_key = encrypt_with_otp(plaintext)
    print("\nEncrypted Text:", encrypted_text)
    print("OTP (to send to Computer 2):", otp)
    print("Triple DES Key (to be shared in advance or securely):", des_key)
    return encrypted_text, otp, des_key

plaintext = "Hello, hi"
print("Original Text (Computer 1):", plaintext)

encrypted_text, otp, des_key = encrypt_message(plaintext)

#3DES CODE ENDS