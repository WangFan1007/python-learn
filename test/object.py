
class Persion():
    def __init__(self,name,age):
        name = name
        age = age

    def __call__(self, *args, **kwargs):
        print('called')



perter = Persion(name='peter',age=30)

perter()