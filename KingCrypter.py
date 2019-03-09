class Encoder:
    def encode(self, word = ""):
        next_char = 5
        encode_word = ""
        for char in word:
            encode_word +=  chr(ord(char) + next_char)
        return encode_word

class Decoder:
    def decode(self, hash = ""):
        decoding = ""
        previous_char = 5
        for char in hash:
            decoding += chr(ord(char) - previous_char )
        return decoding

