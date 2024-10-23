#!pip install pycryptodome

from Crypto.Cipher import DES3
import base64

otp = "ZiHXdn3W5jhJ5PcuWrMhQC9oM2g/Gy5j"

rcvdText = "Nk6+LjmSiEAcibBDFOAUB1syXgB3bBNe"
SecretKey = "IMJc8mBsZ12gWoig7bRmUdOksZT+Op7u"



def decrypt_triple_des(key, encrypted_text):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text))
    return decrypted_text.decode().strip()


def apply_otp(text_bytes, otp_bytes):
    return bytes([b ^ o for b, o in zip(text_bytes, otp_bytes)])

# Triple DES with OTP decryption
def decrypt_with_otp(encrypted_otp_text, otp_base64, triple_des_key_base64):
    # Step 1: Decode Base64 inputs
    otp_encrypted = base64.b64decode(encrypted_otp_text)
    otp = base64.b64decode(otp_base64)
    triple_des_key = base64.b64decode(triple_des_key_base64)


    decrypted_bytes = apply_otp(otp_encrypted, otp)
    decrypted_text = decrypted_bytes.decode()


    decrypted_plaintext = decrypt_triple_des(triple_des_key, decrypted_text)

    return decrypted_plaintext


def decrypt_message(encrypted_text, otp, des_key):
    decrypted_text = decrypt_with_otp(encrypted_text, otp, des_key)
    print("\nDecrypted Text (Computer 2):", decrypted_text)

received_encrypted_text = rcvdText  # From Computer 1
received_otp = otp # From Computer 1
received_des_key = SecretKey  # Securely shared

decrypt_message(received_encrypted_text, received_otp, received_des_key)