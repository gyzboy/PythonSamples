class Person(object):
    #默认构造方法
    def __init__(self,first='guo',last='yizhe',age=20):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):#返回的是print打印的结果
        "This is the string that is printed"
        return "A {} age person".format(self.age)

    def __repr__(self):#返回的是不使用print的结果
        "This string recretes the object"
        return "{}(age='{}')".format(self.__class__.__name__,self.age)

    def full_name(self):
        return "name = " + self.first + self.last + ", age = " + str(self.age)

    #本来可以通过修改self.age的值来修改read_only返回,加上property注解后,read_only只读不可修改
    # @property
    def read_only(self):
        return self.age


class Son(Person):
    def full_name(self):
        super(Son,self).full_name()
    def son_name(self):
        return "son name"
    def __str__(self):
        return "son name is son"

person = Person("guo","yizhe",25)
print(person)

#等效于person = Person()
new_person = Person.__new__(Person)
Person.__init__(new_person)
pperson = new_person
print(pperson)

person.age = 50
print(person.read_only())


# print(person.full_name())
son = Son()
print(son)
print(son.son_name())
print(son.full_name())