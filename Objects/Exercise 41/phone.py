class Phone:
    def dial(self):
        return f'You Are Calling {input("Dial phone number: ")}.'


class SmartPhone(Phone):
    def run_app(self):
        return f'{input("What app you want to run: ")} is running.'


class IPhone(SmartPhone):
    def dial(self):
        return super().dial().lower()


p1 = Phone()
s1 = SmartPhone()
i1 = IPhone()

#print(p1.dial())
#print(s1.run_app())
print(i1.dial())

