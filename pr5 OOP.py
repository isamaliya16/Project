
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        cls = "Human"
        return "{}(name={}, age={})".format(cls, self.name, self.age)

class Worker(Human):
    def __init__(self, name, age, code="", pay=0.0):
        super().__init__(name, age)
        self.__badge = str(code)
        self.__package = float(pay)

    # encapsulation
    def code(self): return self.__badge
    def code_set(self, new_code): self.__badge = str(new_code)
    def pay(self): return self.__package
    def pay_set(self, value):
        value = float(value)
        if value < 0: print("Invalid pay")
        else: self.__package = value

    # 'overloading' via alternative constructors
    @classmethod
    def from_core(cls, name, age, code):
        return cls(name, age, code, 0.0)
    @classmethod
    def hydrate(cls, d):
        return cls(d.get("name",""), d.get("age",0), d.get("employee_id",""), d.get("salary",0))

    def __str__(self):
        return "Worker(name={}, age={}, code={}, pay=${})".format(self.name, self.age, self.__badge, self.__package)
    # comparison operators -> pay based
    def __eq__(self, other): return isinstance(other, Worker) and self.pay() == other.pay()
    def __lt__(self, other): return isinstance(other, Worker) and self.pay() < other.pay()
    def __gt__(self, other): return isinstance(other, Worker) and self.pay() > other.pay()

    def showup(self): print(self)

class TeamLead(Worker):
    def __init__(self, name, age, code, pay, dept):
        super().__init__(name, age, code, pay)
        self.dept = dept
    def showup(self):
        print(super().__str__() + " | team: " + str(self.dept))

class SoftwareMaker(Worker):
    def __init__(self, name, age, code, pay, lang):
        super().__init__(name, age, code, pay)
        self.lang = lang
    def showup(self):
        print(super().__str__() + " | code lang: " + str(self.lang))

print("check:", issubclass(TeamLead, Worker), issubclass(SoftwareMaker, Worker))

people_bin = []
staff_map = {}

def banner():
    print("\n--- Role Manager ---")
    print("1) New Human")
    print("2) New Worker")
    print("3) New TeamLead")
    print("4) New SoftwareMaker")
    print("5) Show")
    print("6) Compare Pay")
    print("7) Exit")

while True:
    banner()
    pick = input("Choose: ").strip()
    if pick == "1":
        nm = input("Name: "); ag = int(input("Age: "))
        people_bin.append(Human(nm, ag))
        print("saved")
    elif pick == "2":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("ID Code: "); py = float(input("Package: "))
        e = Worker(nm, ag, cd, py); staff_map[e.code()] = e; print("ok")
    elif pick == "3":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("ID Code: "); py = float(input("Package: ")); dp = input("Team: ")
        m = TeamLead(nm, ag, cd, py, dp); staff_map[m.code()] = m; print("ok")
    elif pick == "4":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("ID Code: "); py = float(input("Package: ")); lg = input("Code Lang: ")
        d = SoftwareMaker(nm, ag, cd, py, lg); staff_map[d.code()] = d; print("ok")
    elif pick == "5":
        print("a) Humans  b) Worker by id  c) all Worker")
        sub = input("-> ").strip().lower()
        if sub == "a":
            if not people_bin: print("none")
            for i, p in enumerate(people_bin, 1): print(i, p)
        elif sub == "b":
            key = input("id: "); obj = staff_map.get(key)
            if obj: obj.showup()
            else: print("not found")
        else:
            if not staff_map: print("empty")
            for v in staff_map.values(): v.showup()
    elif pick == "6":
        a = input("id1: "); b = input("id2: ")
        x = staff_map.get(a); y = staff_map.get(b)
        if not x or not y: print("missing")
        else:
            if x == y: print("same pay")
            elif x > y: print(a, "earns more than", b)
            else: print(a, "earns less than", b)
    elif pick == "7":
        print("bye"); break
    else:
        print("wrong")
