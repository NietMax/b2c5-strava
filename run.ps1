# Create a virtual environment
python -m venv env

# Activate the virtual environment
.\env\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install the required modules
pip install -r requirements.txt.

# Feedback on the installed modules
echo "Installed modules all packages"

# Run your script
python main.py

# Feedback on completion
echo "Process completed successfully."

# Stop powershell script
exit
