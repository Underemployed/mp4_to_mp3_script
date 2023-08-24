import os
import threading

# Function to rename MP4 files to MP3
def rename_mp4_to_mp3(input_folder, filename):
    input_path = os.path.join(input_folder, filename)
    new_filename = f"{os.path.splitext(filename)[0]}.mp3"
    new_path = os.path.join(input_folder, new_filename)
    
    try:
        os.rename(input_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Error renaming {filename}: {str(e)}")

def process_mp4_files(input_folder, files):
    for filename in files:
        if filename.endswith(".mp4"):
            rename_mp4_to_mp3(input_folder, filename)

if __name__ == "__main__":
    current_directory = os.getcwd()  # current directory
    input_folder = current_directory  
    
    # List of files
    files = os.listdir(input_folder)
    
    # Create threads
    num_threads = 4  # You can adjust this to control the number of threads
    threads = []
    
    # Divide the files
    chunk_size = len(files) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(files)
        thread = threading.Thread(target=process_mp4_files, args=(input_folder, files[start:end]))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All MP4 files processed.")
