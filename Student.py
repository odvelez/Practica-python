from Person import Person
class Student(Person):
    def __init__(self, name, age, grade, score):
        super().__init__(name, age)
        self.grade = grade
        self.score = score

    def avg_score(self, score1, score2, score3):
        try:
            total = float(score1) + float(score2) + float(score3)
            print(total/0)
            return total
        except ZeroDivisionError: 
            print ("Cannot divide by 0")
        except ValueError:
            print("Could you verify the inputs")
        
    def __str__(self):
        return (f"Student Grade: {self.grade}, Score: {self.score}")