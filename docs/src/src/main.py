class CloudDataEncryption:

    def encrypt_data(self, data):
        print(f"Encrypting: {data}")

    def decrypt_data(self, data):
        print(f"Decrypting: {data}")


def main():
    security = CloudDataEncryption()

    security.encrypt_data("User Confidential Data")
    security.decrypt_data("Encrypted Data")


if __name__ == "__main__":
    main()
