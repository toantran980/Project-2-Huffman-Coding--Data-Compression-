import tkinter as tk

#####################Functions##########################################################################################################################
def get_bytesizes(uncompressed_file, compressed_file):
    
    bytesize = -1

    return  bytesize

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

        ratio = compressed_size/uncompressed_size

    return ratio

def read_uncomp_file():
    file_string =  "None"

    #Use file_processor to read from uncompressed file and return a string to user for uncompressed output field

    return file_string


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


#####################Execution##########################################################################################################################
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
textfile_button = tk.Button(frame, text="Select Text File", command=root.destroy)
textfile_button.grid(row=2, column=0)

#File Size Comparison Label
bytesize_label = tk.Label(frame, text="Huffman Compression Tool", font=("Arial", 24))
bytesize_label.grid(row=3, column=0)

#Huffman Encoding output from selected file
comp_file_text = tk.Text(frame, wrap="word", height=10, width=100)

comp_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=comp_file_text.yview)
comp_scrollbar.grid(row=4, column=1, sticky="ns")  # Attach scrollbar next to the Text widget
comp_scrollbar.place(in_=comp_file_text, relx=1.0, rely=0, relheight=1.0, anchor="ne")

comp_file_text.config(yscrollcommand=comp_scrollbar.set)
comp_file_text.grid(row=4, column=0)
comp_file_text.insert(tk.END, long_text)



#Decompress huffman encoded file
decompress_button = tk.Button(frame, text="Decompress File", command=root.destroy)
decompress_button.grid(row=5, column=0)

#Decompressed output label
label = tk.Label(frame, text="Decompressed File:", font=("Arial", 24))
label.grid(row=6, column=0)

#Decompressed Ouput field
#uncomp_file_text = tk.Text(frame, wrap="word",height=10, width=50)
#uncomp_file_text.grid(row=7, column=0)
#uncomp_file_text.insert(tk.END, long_text)

uncomp_file_text = tk.Text(frame, wrap="word", height=10, width=100)

uncomp_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=uncomp_file_text.yview)
uncomp_scrollbar.grid(row=7, column=1, sticky="ns")  # Attach scrollbar next to the Text widget
uncomp_scrollbar.place(in_=uncomp_file_text, relx=1.0, rely=0, relheight=1.0, anchor="ne")

uncomp_file_text.config(yscrollcommand=uncomp_scrollbar.set)
uncomp_file_text.grid(row=7, column=0)
uncomp_file_text.insert(tk.END, long_text)

#Exit button
""" exit_button = tk.Button(frame, text="Exit", command=root.destroy)
exit_button.grid(row=10, column=0) """

root.mainloop()