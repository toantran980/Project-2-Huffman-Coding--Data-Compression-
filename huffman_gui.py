import tkinter as tk
from tkinter import filedialog
import huffman_algorithm as algo
from file_processor import File
from pathlib import Path
from datetime import datetime
#####################Functions##########################################################################################################################

def create_output_directory(directory_name):

    output_directory_name = directory_name

    results_directory = Path(output_directory_name)
    results_directory.mkdir(parents=True, exist_ok=True)  # Create folder if it doesn't exist

    return results_directory

def get_bytesizes(uncompressed_file_path, compressed_file_path):
    file_obj = File()

    size_tuple = file_obj.compare_files_size(uncompressed_file_path,compressed_file_path)
    return  size_tuple

#Takes the byte sizes of the file before and after compression, 
#Error Checking: Checks to make sure the sizes are not the same and checks to see if the compressed size is larger than the uncompressed size
#If compressed size is less than compressed size the ratio will be calculated and return, if not the program will return -42
def calculate_ratio(uncompressed_size,compressed_size):

    if(uncompressed_size == compressed_size):
        print("Error: uncompressed_size and compressed size are the same size")
        return -42
    elif(compressed_size > uncompressed_size):
        print("Error: compressed_size bytecounte larger than uncompressed_size bytecount")
        return -42
    elif(compressed_size < uncompressed_size):
        print(f"Uncompressed Size: {uncompressed_size}")
        print(f"Compressed Size: {compressed_size}")

        ratio = round((compressed_size/uncompressed_size),3)

    return ratio

def read_uncomp_file():
    file_string =  "None"

    #Use file_processor to read from uncompressed file and return a string to user for uncompressed output field

    return file_string

#decompress = 0
#compress = 1
def file_select(compress_or_decompress, output_field, bytesize_label_obj = None):
    file_obj = File()
#    current_filepath = filedialog.askopenfilename(title="Select file",filetypes=[("Text Files", "*.txt")])
#
#    if current_filepath:
#        print(f"User selected file: {current_filepath}")


    #compress_or_decompress == 0, if so it will decompress the file selected by user
    #also updates the output field for the huffman codes
    if(compress_or_decompress == 0):
        
        current_filepath = filedialog.askopenfilename(title="Select file",filetypes=[("Text Files", "*.bin")])
        if current_filepath:
            print(f"User selected file: {current_filepath}")

#        text_in_file = File.read_file(current_filepath)
#        encoded_text, huffman_codes = algo.huffman_encode(text_in_file)
        encoded_text, huffman_codes = encode_and_grab_info(current_filepath)

        #deleting what is currently in output field and then inserting the huffman codes
        output_field.delete("1.0", tk.END)
        output_field.insert(tk.END, encoded_text)


        return encoded_text

    #compress_or_decompress == 1, if so it will compress the file selected by user
    #also updates the output field for the decoded huffman encoded file
    elif(compress_or_decompress == 1):
        
        current_filepath = filedialog.askopenfilename(title="Select file",filetypes=[("Text Files", "*.txt")])
        current_time = -1
        if current_filepath:
            print(f"User selected file: {current_filepath}")
            #Grabs current time now because we want to append this data to the filenames of the encoded text and the huffman codes
            #This is done so both of the files can be associated when the encoded text's .bin file is selected
            #Minor parsing will have to be done but it will be simple, single seperator '_' so you can just split with that as an arg to find the packed data
            current_time = datetime.now()
            current_time_string = str(current_time.month) + "_" + str(current_time.day) + "_" + str(current_time.hour) + "_" + str(current_time.minute) + "." + str(current_time.second) 


        bytesize_string = f"Original Size: 0 Bytes | Compressed Size: 0 Bytes | Ratio: 0.0%"
        encoded_text, huffman_codes = encode_and_grab_info(current_filepath)
        
        #deleting what is currently in output field and then inserting the huffman codes
        output_field.delete("1.0", tk.END)
        output_field.insert(tk.END, huffman_codes)

        #writing encoded data to .bin file
        output_filepath = get_output_file_path(_result_directory_path, "encoded", current_time_string, ".bin")
        #file_obj.write_file(output_filepath,encoded_text)
        #vvvmake it so its writing a binary filev= vvv
        #write_txt_file(output_filepath,encoded_text)
        file_obj.compressed_file(output_filepath, encoded_text)
        #file_obj.write_file(output_filepath, encoded_text)

        #writing huffman codes to a txt file
        huffman_codes_output_filepath = get_output_file_path(_huffman_codes_directory_path, "h_codes", current_time_string, ".txt")

        huffman_codes_string = '\n'.join(f'{key}: {value}' for key, value in huffman_codes.items())
        print(f"Huffman Code Strings: {huffman_codes_string}")

        write_txt_file(huffman_codes_output_filepath,huffman_codes_string)

        size_tuple = get_bytesizes(current_filepath,output_filepath)
        ratio = calculate_ratio(size_tuple[0],size_tuple[1])
        bytesize_label_obj.config(text=f"Original Size: {size_tuple[0]} Bytes | Compressed Size: {size_tuple[1]} Bytes | Ratio: {ratio}%")

        return output_filepath
    
    else:
        print("file_select call misused, please enter argument either 0 for compress 1 for decompress")

    return current_file_compressed_filepath


def encode_and_grab_info(filepath):

    file_obj = File()

    text_in_file = file_obj.read_file(filepath)
    encoded_text, huffman_codes = algo.huffman_encode(text_in_file)
    return encoded_text, huffman_codes

def grab_bin_info(file_path):

    bin_data = read_bin_file(file_path)
    algo.huffman_decode(bin_data)

    return 

def get_output_file_path(directory_path, file_name, creation_time, extension):

    full_file_name = file_name + "_" + creation_time + "_" + extension

    full_output_path = directory_path / full_file_name

    return full_output_path

def write_txt_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)




def read_bin_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()


####Variables
long_text = """
1.This is a multiline string.
2.We can write this in multiple lines too!
3.Hello from AskPython. 
4.This is the  line.
5.This is the fourth line. Although the length of the text is longer than
6.the width, we can use tkinter's scrollbar to solve this problem!
7.This is the  line.
8.This is the fourth line. Although the length of the text is longer than
9.the width, we can use tkinter's scrollbar to solve this problem!
10.the width, we can use tkinter's scrollbar to solve this problem!
"""

global current_file_uncompressed_filepath
current_file_uncompressed_size = ""

global current_file_compressed_filepath
current_file_compressed_size = ""


current_file_uncompressed_size = -1
current_file_compressed_size = -1


#####################Execution##########################################################################################################################
global _result_directory_path 
_result_directory_path = create_output_directory("output")
global _huffman_codes_directory_path
_huffman_codes_directory_path = create_output_directory("huffman_codes")

root = tk.Tk()
root.title("Huffman Compression Tool")
root.geometry("800x800")

# Configure the grid to scale with the window size
root.grid_rowconfigure(0, weight=1)  # Empty space at top
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)  # Empty space at bottom

root.grid_columnconfigure(0, weight=1)  # Empty space on the left
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)  # Empty space on the right

# Create a frame to hold widgets
frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

# Configure the frame to expand with the window
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Program Title Label
label = tk.Label(frame, text="Huffman Compression Tool", font=("Arial", 24))
label.grid(row=1, column=0)

#Select Text File Button
#textfile_button = tk.Button(frame, text="Select Text File", command=lambda: file_select(1))
#textfile_button = tk.Button(frame, text="Select Text File", command=root.destroy)
#textfile_button.grid(row=2, column=0)

#--------------------------------------------------------------------------------------------------------------------------------------
#File Size Comparison Label
bytesize_label = tk.Label(frame, text=f"Original Size: 0 Bytes | Compressed Size: 0 Bytes | Ratio: 0.0%", font=("Arial", 18))
bytesize_label.grid(row=3, column=0)
#--------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------
#Huffman Encoding output from selected file
comp_file_text = tk.Text(frame, wrap="word", height=10, width=100)

comp_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=comp_file_text.yview)
comp_scrollbar.grid(row=4, column=1, sticky="ns")  # Attach scrollbar next to the Text widget
comp_scrollbar.place(in_=comp_file_text, relx=1.0, rely=0, relheight=1.0, anchor="ne")

comp_file_text.config(yscrollcommand=comp_scrollbar.set)
comp_file_text.grid(row=4, column=0)
#--------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------
#Select Text File Button
textfile_button = tk.Button(frame, text="Select Text File", command=lambda: file_select(1,comp_file_text,bytesize_label))
#textfile_button = tk.Button(frame, text="Select Text File", command=root.destroy)
textfile_button.grid(row=2, column=0)
#--------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------
#Decompressed output label
label = tk.Label(frame, text="Decompressed File:", font=("Arial", 24))
label.grid(row=6, column=0)
#--------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------
#Decompressed Huffman Encoding Text
uncomp_file_text = tk.Text(frame, wrap="word", height=10, width=100)

uncomp_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=uncomp_file_text.yview)
uncomp_scrollbar.grid(row=7, column=1, sticky="ns")  # Attach scrollbar next to the Text widget
uncomp_scrollbar.place(in_=uncomp_file_text, relx=1.0, rely=0, relheight=1.0, anchor="ne")

uncomp_file_text.config(yscrollcommand=uncomp_scrollbar.set)
uncomp_file_text.grid(row=7, column=0)
#--------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------
#Decompressed Huffman Encoding Button
decompress_button = tk.Button(frame, text="Decompress File", command=lambda: file_select(0,uncomp_file_text))
decompress_button.grid(row=5, column=0)
#--------------------------------------------------------------------------------------------------------------------------------------



#Exit button
""" exit_button = tk.Button(frame, text="Exit", command=root.destroy)
exit_button.grid(row=10, column=0) """

root.mainloop()