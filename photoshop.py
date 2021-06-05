import os
from PIL import Image, ImageFilter
from flask import *
from werkzeug.utils import secure_filename

uploadFolder = 'photoshop-webapp/uploads/'
app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('home.html')

@app.route('/upload', methods = ['POST', 'GET'])
def upload_img():
	if request.method == 'POST':
		uploaded_img = request.files['user_img']
		action = request.form.get('effect')
		print(action)
		uploaded_img.save('newimage.jpg')
		img = Image.open('newimage.jpg')
		if action == 'gray':
			result = img.convert('L')
		elif action == 'blur':
			result = img.filter(ImageFilter.BLUR)
		elif action == 'smooth':
			result = img.filter(ImageFilter.SMOOTH)
		elif action == 'sharpen':
			result = img.filter(ImageFilter.SHARPEN)
		result.save('ready/result.png')
		return render_template('download.html')
	else:
		return 'NO POST'


@app.route("/download", methods = ['GET'])
def download():
	file_path = './ready/result.png'
	if request.method=='GET':
		return send_file(file_path, as_attachment=True)

 



if __name__ == '__main__':
	app.run()
	app.Debug=True

