# input_registration.py

def main():
    # Meminta pengguna untuk memasukkan email
    email = input("Silakan masukkan email Anda: ")
    
    # Meminta pengguna untuk memasukkan password
    password = input("Silakan masukkan password Anda: ")
    
    # Meminta pengguna untuk memasukkan kode undangan
    invitation_code = input("Silakan masukkan kode undangan Anda: ")
    
    # Mengembalikan data yang dimasukkan
    return email, password, invitation_code

if __name__ == "__main__":
    email, password, invitation_code = main()
    print("\nInformasi yang Anda masukkan:")
    print(f"Email: {email}")
    print(f"Password: {password}")  # Hati-hati dengan mencetak password di aplikasi nyata
    print(f"Kode Undangan: {invitation_code}")
