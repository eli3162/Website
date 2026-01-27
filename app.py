from flask import *
from subprocess import *
from werkzeug.utils import secure_filename
import os
import json
import subprocess
from pathlib import Path
import requests

def download_file(url, local_filename):

    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()

            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk: 
                        f.write(chunk)
        print(f"Successfully downloaded '{local_filename}'")
    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")

app = Flask(__name__)

@app.route('/hey/you/should/come/download/all/my/photogrammetry/files/')
def im_coming_to_get_all_the_photogrammetry_files():
	for i in range(1, 11):
		url = f'http://192.168.0.110:5000/images/captured_img{i}.jpg'
		local_filename = f'img{i}.jpg'
		download_file(url, local_filename)
	return 'I came and got your photogrammeyry files :]'

@app.route('/.well-known/acme-challenge/<challenge_key>')
def acme_challenge(challenge_key):
	return challenge_key

@app.route('/artifacts/view/<filename>')
def view(filename):
	return f'''
		<!DOCTYPE html>
		<html lang="en">
		<html>
			<body>
				<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/4.0.0/model-viewer.min.js"></script>
				<model-viewer src="/artifacts/data/{filename}" alt="A 3D model" auto-rotate camera-controls ar ar-modes="webxr scene-viewer quick-look" style="width: 100%; height: 100vh;">
			</body>
		</html>
	'''


@app.route('/artifacts/data/<filename>')
def glb_fetch(filename):
	directory = os.path.join('fll', 'artifacts')
	return send_from_directory(directory, filename, as_attachment=False)

@app.route('/artifacts/metadata/<filename>')
def metadata_fetch(filename):
	if request.method == 'GET' or request.method == 'OPTIONS':
		root = os.path.dirname(__file__)
		directory = os.path.join(root, 'fll', 'artifacts')
		filepath = os.path.join(directory, filename)
		with open(filepath, "r", encoding="utf-8", newline='\n') as f:
			text = f.read()
		return text

@app.route('/assets/<filename>')
def asset_file(filename):
	directory = 'assets'
	return send_from_directory(directory, filename, as_attachment=False)

@app.route('/fll/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return 'No file selected'
            
            file = request.files['file']
            if file.filename == '':
                return 'No file selected'
            
            if file:
                upload_dir = os.path.join(os.path.dirname(__file__), 'fll', 'artifacts')
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)

                filename = secure_filename(file.filename)
                file_path = os.path.join(upload_dir, filename)

                file.save(file_path)

                return f'File {filename} uploaded successfully!'
        
        except Exception as e:
            return f'An error occurred: {e}'
    
    return render_template('upload.html')


@app.route('/code/upload', methods=['GET', 'POST'])
def uploadblock():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return 'No file selected'
            
            file = request.files['file']
            if file.filename == '':
                return 'No file selected'
            
            if file:
                upload_dir = os.path.join(os.path.dirname(__file__), 'code', 'block')
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)

                filename = secure_filename(file.filename)
                file_path = os.path.join(upload_dir, filename)

                file.save(file_path)

                return f'File {filename} uploaded successfully!'
        
        except Exception as e:
            return f'An error occurred: {e}'
    
    return render_template('block.html')

@app.route('/fll/uploads/metadata', methods=['GET', 'POST'])
def handle_json_metadata():
	metadata = request.get_json()
	return

@app.route('/download/assets/<filename>')
def download_assets(filename):
	directory = 'assets'
	return send_from_directory(directory, filename, as_attachment=True)

@app.route('/download/uploads/<filename>')
def download_uploads(filename):
	directory = 'uploads'
	return send_from_directory(directory, filename, as_attachment=True)

@app.route('/assets/uploads/<filename>')
def assets_uploads(filename):
	directory = 'uploads'
	return send_from_directory(directory, filename, as_attachment=False)

@app.route('/music/<filename>')
def music(filename):
	directory = 'music'
	return send_from_directory(directory, filename, as_attachment=False)
    
@app.route('/download/music/<filename>')
def download_music(filename):
	directory = 'music'
	return send_from_directory(directory, filename, as_attachment=True)
    
@app.route('/<file>')
def index(file):
	if file not in ['favicon.ico', 'fll.html']:
		try:
			root = os.path.dirname(__file__)
			file_path = os.path.join(root, file)
			with open(file_path, 'r', encoding='utf-8') as file:
				return file.read()
		except Exception as e:
			print(f"Error: {e}")
			return send_from_directory('', file, as_attachment=False)
	else:
		if file == 'fll.html':
			root = os.path.dirname(__file__)
			file_path = os.path.join(root, 'fll', 'index.html')
			with open(file_path, 'r', encoding='utf-8') as file:
				return file.read()
		else:
			return send_from_directory('', file, as_attachment=False)

@app.route('/')
def home():
	root = os.path.dirname(__file__)
	file_path = os.path.join(root, 'index.html')
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

	
@app.route('/files')
def files():
	root = os.path.dirname(__file__)
	file_path = os.path.join(root, 'files.txt')
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

@app.route('/fll')
def fll():
	root = os.path.join(os.path.dirname(__file__), 'fll')
	file_path = os.path.join(root, 'index.html')
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

@app.route('/fll/<filename>')
def fetch_fll(filename):
	root = os.path.join(os.path.dirname(__file__), 'fll')
	file_path = os.path.join(root, filename)
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()




if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)