class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.score = float(score)
        self.tracks = tracks
    def change_name(self, name):
         self.name = name
         return name
    
    def change_age(self, age):
         self.age = int(age)
         return age
    def add_track(self, tracks):
         self.tracks.append(tracks)
         return tracks
         
    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

