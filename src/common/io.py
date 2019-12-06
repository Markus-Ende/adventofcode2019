def read(file_path):
    input_file = open(file_path, 'r')
    input_raw = input_file.read()
    input_file.close()
    return input_raw