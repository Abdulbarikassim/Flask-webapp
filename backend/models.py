from app import db

class Friends(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    img_url = db.Column(db.String(200), nullable=True)  

    def __init__(self, name, role, description, gender, img_url):
        self.name = name
        self.role = role
        self.description = description
        self.gender = gender
        self.img_url = img_url

    def to_json(self): 
        return {
            "name": self.name, 
            "role": self.role, 
            "description": self.description, 
            "gender": self.gender, 
            "imgUrl": self.img_url  
        }
