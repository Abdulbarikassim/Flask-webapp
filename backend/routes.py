from app import app , db 
from flask import request, jsonify
from models import Friends


# get all friends. 

@app.route("/api/friends", methods=["GET"])
def get_friends():
    friends = Friends.query.all()
    results = [friend.to_json() for friend in friends] 
    return jsonify(results)

# create a new friend.
@app.route("/api/friends", methods=["POST"])
def create_friends():
    try: 
        data = request.get_json()

        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")

        if not name or not role or not gender:
            return jsonify({"error": "Name, role, and gender are required fields"}), 400

        if gender == "male":   
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female": 
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"  
        else : 
            img_url = None

        new_friend = Friends(name=name, role=role, gender=gender, description=description, img_url=img_url)  

        db.session.add(new_friend)

        db.session.commit()
        return jsonify(new_friend.to_json()), 201  
    except Exception as e: 
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
# delete a friend.
@app.route("/api/friends/<int:id>", methods=["DELETE"])
def delete_friend(id): 
    try: 
        friend = Friends.query.get(id)

        if friend is None: 
            return jsonify({"error": "Friend not found!"}), 404
        
        db.session.delete(friend)
        db.session.commit()

        return jsonify({"msg": "Friend deleted successfully"}), 200
    
    except Exception as e: 
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# delete a friend.
@app.route("/api/friends", methods=["DELETE"])
def delete_all_friends():
    try:
        num_deleted = db.session.query(Friends).delete()
        db.session.commit()
        return jsonify({"msg": f"{num_deleted} friends deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


#Update a friend profile. 

@app.route("/api/friends/<int:id>", methods=["PATCH"])
def update_friend(id): 

    try: 
        friend = Friends.query.get(id)
        if friend is None: 
            return jsonify({"error": "friend not found"}), 404
        
        data =  request.json

        friend.name = data.get("name", friend.name)
        friend.role = data.get("role", friend.role)
        friend.gender = data.get("gender", friend.gender)
        friend.id = data.get("id", friend.id)
        friend.description = data.get("description", friend.description)

        db.session.commit()

        return jsonify({"msg": "update friends profile successfully!"})



    except Exception as e: 
        db.session.rollback()

        return jsonify({"error": str(e)}), 500









