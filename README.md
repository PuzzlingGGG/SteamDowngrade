# Steam Game Downgrader

Steam Game Downgrader is a GUI tool that assists users in reverting Steam games to previous versions. By leveraging the Steam API, it facilitates the identification and installation of specific game versions through an intuitive interface.

## Features

- Fetch game information through Steam API
- Dynamically retrieve and display game logo and title
- Assist in identifying the required Depot and Manifest IDs
- Automatic steamcmd installation if not present
- Game version downgrade using steamcmd

## Prerequisites

- Python 3.x
- [steamcmd](https://developer.valvesoftware.com/wiki/SteamCMD)
- Internet connection for API communication and game downloading

## Dependencies

The script relies on the following Python packages:
- `tkinter` for the GUI
- `requests` for handling HTTP requests
- `PIL` (Python Imaging Library) for image processing
- `io` for in-memory bytes streams
- `zipfile` and `os` for file and OS operations
- `subprocess` for running shell commands
- `webbrowser` for opening web pages

You can install the necessary Python packages with pip:

```
pip install Pillow requests
```

## Usage

1. Clone the repository or download the script.
2. Run `main.py` to start the application:
    ```
    python main.py
    ```
3. Input the Steam App ID of the game you want to downgrade.
4. Follow the on-screen instructions: confirm the game title, visit the SteamDB page for depot information, and input the Depot and Manifest IDs when prompted.
5. If steamcmd is not installed, the script will fetch and set it up automatically.
6. The script will then use steamcmd to download the specified game version.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/PuzzlingGGG/SteamDowngrade/issues) if you want to contribute.

## License

Distributed under the MIT License.
