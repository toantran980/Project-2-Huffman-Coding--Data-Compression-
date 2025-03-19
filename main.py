from huffman_algorithm import*
from file_processor import*

# Main function to demonstrate encoding and decoding
def main():
    file = File()
    text = file.read_file("input.txt")# Read the input file

    # Build Huffman Tree and binary translation
    encoded_text, huffman_codes = huffman_encode(text)
    print("\nHuffman Codes:")
    for char, code in huffman_codes.items():
        print(f"'{char}': {code}")
    print("\nEncoded Text: ", encoded_text)

    # Compress the encoded text and save to a file
    encoded_text = file.compressed_file("compressed.bin", encoded_text)
    
    # Decoded the text
    decoded_text = huffman_decode(encoded_text, huffman_codes)
    print("\nDecoded Text: ", decoded_text)

    # Compare the sizes of the original and compressed files
    file.compare_files_size("input.txt", "compressed.bin")


if __name__ == "__main__":
    main()
