class person:
    def __init__(self, name):
        self.__name = name

    def run(self, area):
        print("{}在{}跑步".format(self.__name, area))
class Cat:
    def laugh(self):
        print("猫在笑")