
# MP4 to MP3 Converter

This Python script is a multi-threaded tool to rename MP4 files to MP3 files. It uses the `os` and `threading` modules to perform this task efficiently.

## Usage

Before running the script, ensure that you have Python installed on your system. You'll also need to install the `moviepy` library if you haven't already. You can install it using pip:

```shell
pip install moviepy
```

Once you have the dependencies installed, follow these steps:

1. Clone this repository or download the script to your local machine.
2. Navigate to the directory containing your MP4 files that you want to rename.
3. Open a terminal or command prompt in that directory.
4. Run the script using the following command:

```shell
python mp4_to_mp3.py
```

The script will rename all MP4 files in the current directory to have the ".mp3" extension.

## Configuration

You can adjust the number of threads used for the renaming process by modifying the `num_threads` variable in the script. A higher number of threads can speed up the process, but be cautious not to use too many threads, as it may lead to excessive CPU usage.

## Error Handling

The script includes error handling to capture and report any errors that occur during the renaming process. If a file cannot be renamed for any reason, the script will print an error message indicating which file encountered the error and the specific error message.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Underemployed/mp4_to_mp3_script/blob/main/LICENSE) file for details.

## Contributing

Contributions to this project are welcome. Please open an issue or create a pull request with your suggestions or improvements.

