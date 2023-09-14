def write_file(file_name, file_content):
   with open(f"{file_name}.txt"  ,mode="w") as file_open:
            file_open.write(file_content)
        

def append_file(file_name, append_content):
    with open(f"{file_name}.txt",mode="a") as file_append:
            file_append.write(append_content)
 

def read_file(file_name):
      open_file =open(f"{file_name}.txt",mode="r")
      return open_file
      
    # with open(f"{file_name}.txt",mode="r") as open_file:
    #         open_file.read()

  