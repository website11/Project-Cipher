
class BaconianCipher:
    def __init__(self, encrypted_message=""):
        self.encrypted_message = encrypted_message
        self.current_message = encrypted_message[:]

    def create_empty_message(self):
        empty_message = ""
        for char in self.encrypted_message:
            if char.isalpha():
                empty_message += "_"
            else:
                empty_message += char
        return empty_message


    def baconian_mapper(self, text):
        decoded_text = ""
        baconian_dict = {
            'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
            'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
            'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
            'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
            'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
            'Z': 'BBAAB'
        }
        for letter in text:
            decoded_text += baconian_dict[letter.upper()] + " "
        print(decoded_text)
        return decoded_text




    def baconian_solver(self):
        baconian_view = self.create_empty_message()[:]
        message = ""
        crib = "No Crib Set"
        crib_decode = "No Crib Set"
        while True:
            print("Crib:" ,crib)
            print("Decoded Crib:" ,crib_decode)
            print("")
            print("Encrypted View:")
            print(self.encrypted_message)
            print("--------------------------")
            print(baconian_view)
            print("--------------------------")
            print("Decrypted View:")
            print(message)

            print("1. Replace a Letter (ex. C->A)       2. Crib Menu")
            print("3. Reset Board                       4. Back")

            choice = input("Select an Option (ex. 1):\n")

            if choice == "2":
                print("1. Add a Crib                        2. Place Crib")
                print("3. Back")

                choice = input("Select an Option (ex. 1):\n")
                if choice == "1":
                    crib = input("Enter a crib name: ")
                    if crib.isalpha():
                        crib = crib.upper()
                        crib_decode = self.baconian_mapper(crib)
                    else:
                        crib = ""
                        crib_decode = ""
                        print("Invalid Crib")

