# import pint
# u=pint.UnitRegistry()
# Q=u.Quantity


class Unit:

    def conversion(self, unit, num, u):
        if unit=='m':
            if u=='cm':
                num=float(num/100)
            elif u=='mm':
                num=float(num/1000)
            elif u=='in':
                num=float(num/39.37)
            elif u=='ft':
                num=float(num/3.281)
            elif u=='yd':
                num=float(num/1.094)
            return num


        elif unit=='joules':
            if u=='kJ':
                num=float(num/1000)
            elif u=='MJ':
                num=float(num/1000)
            elif u=='Wh':
                num=float(num/1000)
            elif u=='kWh':
                num=float(num/1000)
            elif u=='ft-lb':
                num=float(num/1000)
            elif u=='kcal':
                num=float(num/1000)
            elif u=='eV':
                num=float(num/1000)

            return num



    def check(self, conv_unit, value, unit, name):
        if unit != conv_unit:
            changed_value = self.conversion(conv_unit, value, unit)
            text =f"{value} in {conv_unit} is {changed_value} {conv_unit}"

            return changed_value, text

        else:
            return value, ''


class Type:
    def type_conversion(self, num):
        if num.isdigit():
            Number = int(num)

        else:
            Number = float(num)

        return Number

# z=Unit()
# print(z.check('m',5,'yd','my_unit'))