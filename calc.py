class Calculater:

    def add(self,x,y):
        return x + y
    
    def sub(self,x,y):
        return x - y
    
    def multiple(self,x,y):
        return  x* y
    
    def divide(self,x,y):
        if y != 0:
            return x / y
        else:
            print("cannot divided by zero")

Calculater = Calculater()    

result = Calculater.add(3,7)
print("3+7=",result)

result = Calculater.sub(6,9)
print("6-9=",result)

result = Calculater.multiple(6,7)
print("6*7=",result)

result = Calculater.divide(62,0)
print("3/0=",result)


    
