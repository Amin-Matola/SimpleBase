from flask import Flask,request,render_template,redirect


app=Flask(__name__)

@app.route('/send',methods=['GET','POST'])
def send():
	if request.method=='POST':
		return "POST / AMIN TEST SERVER V-0.1.0 \nForm Data Received:\n%s"%str(
			request.form['Subject'])
	else:
		return "POST / AMIN TEST SERVER V-0.1.0 \nForm Data Received:\n%s"%str(
			request.args.get('Subject','Not available'))


if __name__ == '__main__':
	app.run(host='0.0.0.0',port='8080',debug=True)
