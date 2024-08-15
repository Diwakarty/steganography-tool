# Steganography Tool

## What Is Steganography?

Steganography is the practice of concealing information within other non-secret text or data. Unlike encryption, which makes the content unreadable to unauthorized users, steganography hides the very existence of the information. The hidden message is embedded within a carrier file, such as an image, audio, or video file, in a way that is not apparent to casual observers.

In essence, steganography ensures that the message remains hidden in plain sight, making it a powerful technique for secure communication and data protection.

## Objective
Create a steganography tool that allows users to hide text within images and later retrieve the hidden text. The tool supports image formats like `.webp`, `.png`, `.jpeg`, `.jpg`, `.bmp`, `.tiff`, and `.gif`.


## Skills Learned
- **Steganography**: Understanding the technique of hiding information within images.
- **Python Programming**: Writing Python scripts for image manipulation.
- **Image Processing**: Using the Pillow library to handle image formats and data.
- **Git & GitHub**: Managing code versions and sharing the project.

## Tools Used
- **Python 3.x**: Programming language used for development.
- **Pillow Library**: Python library for image processing.
- **Visual Studio Code**: Code editor for writing and debugging.
- **Git**: Version control tool.
- **GitHub**: Platform to host and share the project.

## How It Works

1. **Encoding Text**:
   - The tool converts the input text into binary format.
   - It then embeds this binary data into the Least Significant Bits (LSBs) of the image's red color component.
   - The embedding process modifies the LSB of each pixel to encode the binary text while keeping changes minimal to avoid noticeable distortion.
   - A delimiter (`1111111111111110`) is added at the end of the text to mark its conclusion.

2. **Decoding Text**:
   - The tool reads the LSBs of the image's red color component to extract the binary data.
   - It reconstructs the binary text from these bits and converts it back to readable text.
   - The extraction process stops when it encounters the delimiter, indicating the end of the hidden message.

This method ensures that the text is hidden within the image with minimal impact on visual quality.


## Steps

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Diwakarty/steganography-tool.git
```

### 2. Navigate to the Project Directory

Change into the project directory:

```bash
cd steganography-tool
```

### 3. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment to manage dependencies:

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
```

### 4. Install Dependencies

Install the required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Run the Tool

You can now run the tool by executing the Python script:

```bash
python stegano.py
```

