from flask import Flask,request,render_template,redirect


app=Flask(__name__)

@app.route('/send',methods=['GET','POST'])
def send():
	if request.method=='POST':
		return "POST / SIMPLEBASE TEST SERVER V-0.1.0 \nForm Data Received:\n%s"%str(
			request.form)
	else:
		return "POST / SIMPLEBASE TEST SERVER V-0.1.0 \nForm Data Received:\n%s"%str(
			request.args.to_dict())


if __name__ == '__main__':
	app.run(host='0.0.0.0',port='8080',debug=True)
