# Code Line Counter

A simple Python-based tool to count lines of code in selected files using a graphical user interface (GUI). The application allows you to count:

- Total lines (including code, comments, and empty lines)
- Total lines of code and comments (excluding empty lines)
- Total lines of code (excluding comments and empty lines)

### Features
- **Browse Files**: Select multiple files to analyze.
- **Line Counting Options**: Choose between counting total lines, code and comment lines, or just code lines.
- **Results Display**: View results in a pop-up message box showing the total line counts for the selected criteria.

### Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)
  
### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tanzimenvst/code_line_count.git
   ```

2. **Ensure Python is installed**: This tool requires Python 3.x. If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).

   > **Note**: Tkinter should already be included with Python by default. If not, refer to the [Tkinter installation guide](https://tkdocs.com/tutorial/install.html).

### Usage

1. **Run the Python script:**

   - **Directly from Python:**

     Navigate to the project folder:
     
     ```bash
     cd code_line_count
     ```
   
     Run the script from the command line:

     ```bash
     python line_count.py
     ```

   - **Using the batch file (`line_count.bat`):**

     Double-click `line_count.bat` to open the GUI. This script runs the `line_count.py` Python script (Give permission if needed).

2. **Select Files**: After launching the tool, click "Browse" to select the files you want to analyze.

3. **Select Counting Options**: Choose one or more of the line count options:
   - Total lines (including code, comments, and empty lines)
   - Total lines of code and comments (excluding empty lines)
   - Total lines of code (excluding comments and empty lines)

4. **View Results**: Click "Calculate Lines" to get the results in a pop-up message box.

### Demo

![Line Calculator Demo](Demo.gif)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Author
Developed by **Tanzim**. Feel free to connect!
