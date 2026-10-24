#اولین پروژه :
#برنامه ای که نام و سن وشغل و شهر رو بگیره و داخل یک دیکشنری بریزه
#مستقیم بیرون کلاس
def identity():
    name=input("name:")
    age=int(input("age:"))
    job=input("job:")
    city=input("city:")
    Info={
        "name": name ,
        "age": age ,
        "job": job ,
        "city": city
    }
    if age <18:
        print("not Eligible")
    else:
        print("eligible")
    return Info
result=identity()
print(result)
#درون کلاس
class Information:
    def __init__(self):
        self.name=input("name:")
        self.age=int(input("age:"))
        self.job=input("job:")
        self.city=input("city:")
        if self.age <18:
            print("not eligible")
        else:
            print("eligible")
identity=Information()
print(identity.__dict__)
