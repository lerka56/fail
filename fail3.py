def read_files(file_names):
    files_data = []
    
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.readlines()
            line_count = len(content)
            files_data.append((file_name, line_count, content))
    
    return files_data

def sort_files_by_line_count(files_data):
    return sorted(files_data, key=lambda x: x[1])

def write_combined_file(sorted_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for file_name, line_count, content in sorted_files:
            file.write(f"{file_name}\n{line_count}\n")
            file.writelines(content)
            file.write("\n") 

def main():
    file_names = ['1.txt', '2.txt', '3.txt']  
    output_file = 'combined_output.txt' 

    files_data = read_files(file_names)
    
    sorted_files = sort_files_by_line_count(files_data)
    
    write_combined_file(sorted_files, output_file)

if __name__ == "__main__":
    main()