import os # For file operations
from bitarray import bitarray 

class File:
    # Read the content of a file
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            text = ' '.join(line.strip() for line in file) # Read the content of the file line by line
        file.close() # Close the file after reading 
        return text
    
    def compressed_file(self, file_path, encoded_text):
        # Convert the encoded text to a bitarray and save to a file
        bits = bitarray(encoded_text)
        with open(file_path, 'wb') as file:
            bits.tofile(file)
        print(f"\nData written to {file_path}...")

        # Read the binary data from the file and convert back to a binary string
        bits = bitarray()
        with open(file_path, 'rb') as file:
            bits.fromfile(file)
        encoded_text_from_file = bits.to01()

        # Ensure the length of the binary string matches the original length
        encoded_text_from_file = encoded_text_from_file[:len(encoded_text)]

        return encoded_text_from_file

    def compare_files_size(self, original_file_path, compressed_file_path):
        original_size = os.path.getsize(original_file_path) # Get the size of the input file in bytes
        compressed_size = os.path.getsize(compressed_file_path) # Get the size of the compressed file in bytes
        
        #print("\nComparison size of input file and compression file...")
        #print(f"Original file size: {original_size} bytes")
        #print(f"Compressed file size: {compressed_size} bytes\n")
        
        return original_size, compressed_size