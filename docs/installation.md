# Installation

![TBH.AI Logo]<img width="618" alt="Main" src="https://github.com/user-attachments/assets/6ef7f0f4-3dbd-4250-9cad-9772f3853243" /> <!-- Placeholder - Save logo here -->

This guide explains how to install the `tbh_secure_agents` package.

## Prerequisites

*   **Python:** Ensure you have Python installed (version 3.8 or higher is recommended). You can download it from [python.org](https://www.python.org/).
*   **pip:** The Python package installer (`pip`) is usually included with Python installations. Ensure it's up-to-date:
    ```bash
    python -m pip install --upgrade pip
    ```

## Installation from PyPI (Recommended)

Once the package is published to the Python Package Index (PyPI), you can install it directly using pip:

```bash
pip install tbh_secure_agents
```
*(Note: This command will only work after the package has been successfully published to PyPI.)*

## Installation from Source (for Development)

If you want to install the package directly from the source code (e.g., after cloning the repository for development):

1.  **Clone the Repository (if applicable):**
    ```bash
    git clone https://github.com/saishshinde15/TBH.AI_SecureAgents.git # Updated URL
    cd TBH.AI_SecureAgents # Updated directory name based on repo name
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    # Create environment
    python -m venv venv
    # Activate environment
    # Windows (CMD/PowerShell):
    venv\Scripts\activate
    # Linux/macOS:
    source venv/bin/activate
    ```

3.  **Install in Editable Mode:** This allows you to make changes to the source code and have them reflected immediately without reinstalling.
    ```bash
    pip install -e .
    ```
    This command installs the package along with its core dependencies (like `google-generativeai`).

4.  **Install Development Dependencies (Optional):** If you plan to contribute or run tests, install the development extras:
    ```bash
    pip install -e .[dev]
    ```

## Verifying Installation

After installation, you can verify it by trying to import the package in a Python interpreter:

```python
import tbh_secure_agents
print(tbh_secure_agents.__version__)
```

If this runs without errors and prints the version number, the installation was successful.

## API Key Configuration

`tbh_secure_agents` uses Google Gemini as its default LLM, which requires an API key.

*   **Recommended Method:** Set the `GOOGLE_API_KEY` environment variable before running your application. The library will automatically detect and use it.
    *   **Linux/macOS:** `export GOOGLE_API_KEY='YOUR_API_KEY'`
    *   **Windows CMD:** `set GOOGLE_API_KEY=YOUR_API_KEY`
    *   **Windows PowerShell:** `$env:GOOGLE_API_KEY='YOUR_API_KEY'`
*   **Alternative (Testing Only):** You can pass the key directly via the `api_key` parameter during `Agent` initialization, but **this is insecure and not recommended for production code.**
