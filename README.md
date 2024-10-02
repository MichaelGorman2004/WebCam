# Webcam Display App

This is a Python application that displays your webcam feed in a resizable and movable window on your screen. It's designed to be flexible and stay on top of other windows.

## Features

- Real-time webcam display
- Always-on-top window
- Draggable window position
- Resizable window
- Simple interface with a quit button

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system
- pip (Python package installer)

## Installation

1. Clone this repository or download the `webcam.py` file.

2. Install the required dependencies using pip:

   ```
   pip install opencv-python pillow
   ```

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing `webcam.py`.

3. Run the script using Python:

   ```
   python3 webcam.py
   ```

4. A window will appear on your screen, showing your webcam feed.

5. To move the window, click and drag anywhere on the webcam feed.

6. To resize the window, click and drag the resize grip in the bottom-right corner.

7. To close the app, click the "Quit" button in the window.

## Customization

- To change the initial window position and size, modify the `geometry` parameter in the `__init__` method of the `WebcamApp` class.
- To adjust the update frequency of the webcam feed, change the `delay` value in the `WebcamApp` class.

## Troubleshooting

- If you see a black screen instead of your webcam feed, make sure your webcam is not being used by another application.
- If the window position is not correct for your screen, adjust the initial `geometry` parameter to fit your screen resolution.

## Contributing

Contributions to this project are welcome. Feel free to fork the repository and submit pull requests.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
