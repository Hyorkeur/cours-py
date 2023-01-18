class Emp:
        def _init_(self, name, age):
                self.name = name   
                self.age = age
        def info(self):
            print("Hello, % s. You are % s old." % (self.name, self.age))
            
Emps = [Emp._init_("John", 43),
        Emp._init_("Hilbert", 16),
        Emp._init_("Alice", 30)]

for emp in Emps:
        emp.info()