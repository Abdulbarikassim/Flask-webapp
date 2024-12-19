from app import app, db
from flask import request , jsonify
from models import Friends


# get all friends. 

@app.route("/api/friends", methods=["GET"])
def get_friends():
    friends = Friends.query.all()
    results = [friend.to_json() for friend in friends]
    return jsonify(results)

# create a friend. 

@app.route("/api/friends", methods=["POST"])
def create_friend():

    try: 
        data = request.json

        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")

        if gender == "male" : 
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female": 
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name} "
        else : 
            img_url = None

        new_friend = Friends(name=name, role=role, description=description, gender=gender, img_url=img_url)

        db.session.add(new_friend)

        db.session.commit()

        return jsonify(new_friend.to_json()), 201
    
    except Exception as e: 
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

    