# Importing the necessary libraries
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask , request, render_template
import os
import numpy as np


# flask application name
app = Flask(__name__)
# Loading the model
model = load_model("ship_classification.h5")

# rendering the html template
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/predict',methods = ['GET','POST'])
def upload():a
    if request.method == 'POST':
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname("__file__")
        print("current path", basepath)
        filepath = os.path.join(basepath,'uploads',f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)
        
        img = image.load_img(filepath,target_size = (64,64))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis =0)

        preds = model.predict_classes(x)
            
        print("prediction",preds)
            
        index = ['aircraft carriers','bulkers ship','cruise ships','drilling rigs','fire-fighting vessels','fishing vessels','inland dry cargo vessels','motor yachts','submarines']
        
        text = "the ship name is : " + str(index[preds[0]])
        
    return text
if __name__ == '__main__':
    app.run(debug = False, threaded = False)