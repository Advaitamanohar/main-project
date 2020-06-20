import flask
import werkzeug
import dehaze
import cv2


app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def h():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    dehaze.ma()  
    
    return flask.send_file('androidFlask_out_t00.55_w0.95.jpg',mimetype="image/*jpg") 
       
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    
