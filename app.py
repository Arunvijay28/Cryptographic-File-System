# app.py
from flask import Flask, render_template, request, send_file
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

current_directory = os.getcwd()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload_encrypt', methods=['POST'])
def upload_encrypt():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    encrypted_data = cipher_suite.encrypt(file.read())

    encrypted_filename = os.path.join(current_directory, 'encrypted_file.txt')
    with open(encrypted_filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    return "File uploaded and encrypted successfully"
@app.route('/upload_decrypt', methods=['POST'])
def upload_decrypt():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    decrypted_data = cipher_suite.decrypt(file.read())
    decrypted_filename = os.path.join(current_directory, 'decrypted_file.txt')
    with open(decrypted_filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    return "File uploaded and decrypted successfully"
@app.route('/download_encrypted')
def download_encrypted():
    return send_file('encrypted_file.txt', as_attachment=True)
@app.route('/download_decrypted')
def download_decrypted():
    return send_file('decrypted_file.txt', as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)
