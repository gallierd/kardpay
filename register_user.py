# register_user.py

import requests
import json
from input_registration import main  # Mengimpor fungsi dari file input_registration.py

def register_user(email, password, invitation_code):
    # Ganti dengan URL pendaftaran yang sesuai
    url = "https://example.com/api/register"  
    
    # Membuat data pendaftaran
    registration_data = {
        "email": email,
        "password": password,
        "invitation_code": invitation_code
    }

    # Mengirim permintaan POST dengan data JSON
    response = requests.post(url, json=registration_data)

    # Memeriksa status kode respons
    if response.status_code == 201:  # 201 Created
        print("Pendaftaran berhasil!")
        print("Respons:", response.json())  # Mencetak respons dari server
    else:
        print("Pendaftaran gagal!")
        print("Status Kode:", response.status_code)
        print("Respons:", response.text)  # Mencetak pesan kesalahan

if __name__ == "__main__":
    email, password, invitation_code = main()  # Memanggil fungsi dari file input_registration.py
    register_user(email, password, invitation_code)  # Mendaftarkan pengguna
