#coding:utf-8
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s: %s' %(self.name,self.score))

    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
print( 'Bart grade is %s' % bart.get_grade())
print( 'Lisa grade is %s' % lisa.get_grade())


class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(animal):
            animal.run()
            animal.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog=Dog()
dog.run()

cat=Cat()
cat.run()

print('run twice')
Animal.run_twice(Animal())
Animal.run_twice(Dog())
Animal.run_twice(Cat())

try:
    print('try...')
    r=10/0
    print('result:',r)
    print('lala 你会执行吗')
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r=10/int('2')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')