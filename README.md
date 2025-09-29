# Bulk Certificate Generator

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A configurable Python script to generate personalized certificates in bulk from a CSV data file. This tool allows users to define text positions, fonts, and colors in a simple configuration file, making it adaptable to any certificate template.



## ✨ Features

-   **Bulk Generation:** Create hundreds of personalized certificates from a single command.
-   **Fully Configurable:** No code changes needed. All settings are controlled via a `config.json` file.
-   **Customizable Elements:** Define any number of text blocks with unique fonts, sizes, colors, and positions.
-   **CSV Data Source:** Easily manage recipient data in a simple `.csv` file.
-   **PDF Output:** Generates high-quality, individual PDF files for each recipient.

---

## 📂 Project Structure

The project is organized into a clean and understandable folder structure.

```
certificate-generator/
│
├── .gitignore
├── config.json         # Main configuration file
├── README.md           # This file
├── requirements.txt    # Project dependencies
│
├── input/              # Folder for all user-provided files
│   ├── certificate_template.png
│   ├── member_data.csv
│   └── fonts/
│       └── YourFont.ttf
│
├── output/             # Folder where generated certificates are saved
│
├── src/                # Source code
│   └── generate.py
│
└── venv/               # Python virtual environment (ignored by Git)
```

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   Python 3.9 or higher
-   Git

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/certificate-generator.git](https://github.com/your-username/certificate-generator.git)
    cd certificate-generator
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```sh
    pip install -r requirements.txt
    ```

---

## ⚙️ How to Use

1.  **Prepare Your Input Files:**
    -   Place your blank certificate template (as a `.png` or `.jpg`) inside the `input/` folder.
    -   Create your `member_data.csv` file in the `input/` folder. Make sure its column headers match the `column_name` fields you'll define in the config.
    -   Place your chosen font files (`.ttf` or `.otf`) inside the `input/fonts/` folder.

2.  **Configure the Script:**
    -   Open `config.json` and edit the settings. Point the file paths to your input files and adjust the text `elements` to match your certificate layout. See the configuration guide below for details.

3.  **Run the Generator:**
    -   Execute the script from the root directory of the project.
    -   ```sh
      python src/generate.py
      ```

Your completed certificates will appear one by one in the `output/` folder.

---

## 🔧 Configuration Guide (`config.json`)

This file is the control panel for the script. Here's what each setting does:

-   `"template_path"`: Path to your certificate image template.
-   `"data_path"`: Path to your CSV file with recipient data.
-   `"font_path"`: Default font to use if an element doesn't specify its own.
-   `"output_folder"`: Folder where the generated certificates will be saved.
-   `"text_color"`: Default text color.
-   `"elements"`: A list of text blocks to draw on the certificate. Each block has the following properties:
    -   `"column_name"`: The exact header of the column from your CSV file to get the text from.
    -   `"position"`: An `[X, Y]` coordinate for placing the text. `[0, 0]` is the top-left corner.
    -   `"font_size"`: The size of the text in points.
    -   `"align"`: Text alignment. Can be `"left"`, `"center"`, or `"right"`.
    -   `"text_color"` (optional): A specific color for this text block (e.g., `"white"`, `"#D4AF37"`).
    -   `"font_path"` (optional): A specific font file for this text block.
    -   `"prefix"` (optional): Text to add before the data from the CSV (e.g., `"Credential ID: "`).

---

