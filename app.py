"""Flask app for Cupcakes""" 
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake         # for example below

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']='abc123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/cupcakes')
def list_cupcakes():

    #should turn into [{{'':''},{'':''},{'':''}...}, {{'':''},{'':''},{'':''}...}... ]
    serialized = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    #turns it into {cupcakes:{'':'','':''}}
    return jsonify(cupcakes = serialized)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """return json about a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods = ['POST'])
def create_cupcake():
    """Add a cupcake according to the JSON data in the body of the POST request
    want the data to come in in this JSON form
    (without the outside braces and cupcake: ):
    {
                    "flavor": "TestFlavor2",
                    "size": "TestSize2",
                    "rating": 10,

                    "image": "http://test.com/cupcake2.jpg"
                }
            """
    #I had to add and remove and play with that extra ["cupcake"] - I ended up adding it on 
    #client side and then removing it here on server side.  JSONstringify never worked for me
    # and there is NO teacher version for this!  That REALLY would have been helpful since I had to do this
    # on a weekend where the TA's are not available.  Grrrrrrrr...
    # What I learned: TEST WITH INSOMNIA AND LOOK CLOSELY AT WHAT THE BACK-END IS GETTING TO MAKE SURE IT
    # MATCHES!!!!
    
    data = request.json["cupcake"]
    print(f"RECIEVED DATA: {data}")

    new_cupcake = Cupcake(
        flavor=data["flavor"],
        rating=data["rating"],
        size=data["size"],
        image=data["image"] or None)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = new_cupcake.serialize()

    return (jsonify(cupcake=serialized_cupcake), 201)


@app.route('/api/cupcakes/<int:cc_id>', methods=['PATCH'])
def update_cupcake(cc_id):
    """update cupcake
    For it to work have to FEED IT DATA LIKE THIS:
    {
                    "flavor": "TestFlavor2",
                    "size": "TestSize2",
                    "rating": 10,
                    "image": "http://test.com/cupcake2.jpg"
                }
    DO NOT USE {cupcake:{}}!!!

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}"""
    #update cupcake from json data
    data = request.json

    #get existingcupcake from database
    cupcake = Cupcake.query.get_or_404(cc_id)
    
    cupcake.flavor= data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cc_id>', methods=['DELETE'])
def delete_cupcake(cc_id):
    """ delete cupcake and return confirmation """
    cupcake = Cupcake.query.get_or_404(cc_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")

