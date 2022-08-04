#!/home/user/Sublime/calculator/venv/bin/python3
from kivy.app import App
from kivy.lang import Builder

from fractions import Fraction

class MyApp(App):

    def build(self):

        self.signs = ["+", "-", ":", "*"]

        return Builder.load_file("interface.kv")

    def change_sign(self, instance):
        
        length = len(self.signs)
        sign_now = self.signs.index(instance.text)

        if sign_now == length - 1:
            sign_now = 0
        else:
            sign_now += 1

        instance.text = self.signs[sign_now]

    def solve(self, instance):

        ids = instance.parent.parent.parent.ids

        # Перший дріб
        fraction11 = ids["fraction11"]
        fraction12 = ids["fraction12"]
        fraction13 = ids["fraction13"]

        # Другий дріб
        fraction21 = ids["fraction21"]
        fraction22 = ids["fraction22"]
        fraction23 = ids["fraction23"]

        # Третій дріб
        fraction31 = ids["fraction31"]
        fraction32 = ids["fraction32"]
        fraction33 = ids["fraction33"]

        # Перевірка дробів на правильність

        if not fraction11.text.isdigit():
            fraction11.text = "0"
        if not fraction12.text.isdigit():
            fraction12.text = "1"
        if (not fraction13.text.isdigit()) or fraction13.text == "0":
            fraction13.text = "1"

        if not fraction21.text.isdigit():
            fraction21.text = "0"
        if not fraction22.text.isdigit():
            fraction22.text = "1"
        if (not fraction23.text.isdigit()) or fraction23.text == "0":
            fraction23.text = "1"

        # Перетворення тексту

        fraction11 = int(fraction11.text)
        fraction12 = int(fraction12.text)
        fraction13 = int(fraction13.text)
     
        fraction21 = int(fraction21.text)
        fraction22 = int(fraction22.text)
        fraction23 = int(fraction23.text)   

        # Основні дроби
        fraction1 = Fraction(fraction11 * fraction13 + fraction12, fraction13)
        fraction2 = Fraction(fraction21 * fraction23 + fraction22, fraction23)

        # Дізнаємось знак
        sign = ids['sign'].text

        # Визначаємо результат
        if sign == "+": result = fraction1 + fraction2
        elif sign == "-": result = fraction1 - fraction2
        elif sign == "*": result = fraction1 * fraction2
        elif sign == ":": result = fraction1 / fraction2

        minus = str(result).startswith("-")

        # Чисельник 
        numerator = result.numerator
        
        # Знаменник
        denominator = result.denominator

        integer = numerator//denominator

        if minus: integer = -integer

        numerator %= denominator

        if numerator == 0: 

            numerator = ""
            denominator = ""
        if integer == 0: integer = ""

        fraction31.text = str(integer)
        fraction32.text = str(numerator)
        fraction33.text = str(denominator)

if __name__ == "__main__":
    MyApp().run()
      