from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Define the root directory
ROOT_DIRECTORY = '/'
app.config['ROOT_DIRECTORY'] = ROOT_DIRECTORY

@app.route('/')
def index():
    return 'Welcome to your app!'

@app.route('/download/<path:filename>')
def download_file(filename):
    # Ensure the requested file is within the allowed directory
    full_path = os.path.join(app.config['ROOT_DIRECTORY'], filename)
    if os.path.isfile(full_path):
        return send_from_directory(app.config['ROOT_DIRECTORY'], filename, as_attachment=True)
    else:
        return 'File not found', 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
