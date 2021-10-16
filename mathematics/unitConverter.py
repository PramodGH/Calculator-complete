def power_raise(value):
    scientific_notation = "{:.2e}".format(value)
    print(scientific_notation,"-----scn noti----")
    # print(type(scientific_notation),"-----type---")
    # [print(x, end=",") for x in scientific_notation]
    output = ""
    power = ''
    output += scientific_notation[:4] + " x 10 "
    if scientific_notation[5:6] == "+":
        power = scientific_notation[6:]
        if power[0]=='0':
            power = power[1:]
    else:
        power_digit = scientific_notation[6:]
        power = power + '-'

        if power_digit[0]=='0':
            power += power_digit[1:]
        else:
            power +=power_digit
        # power = scientific_notation[5:]
    # print(output,"----------",power)
    return output, power

# ohm converter
    def ohm_converter(value, op):
        if op == 'moh':
            return value * 0.0001
        elif op == 'koh':
            return value * 1000
        elif op == 'megaoh':
            return value * 1000000
        else:
            return value

# length - meter convertor
    def meterconverter(lenn, lentype):
        if lentype == 'km/s':
            m = lenn * 1000
        elif lentype == 'mi/s':
            m = lenn * 1609.34
        elif lentype == 'c':
            m = lenn * 299792458
        else:
            m = lenn
        return m


 # to check for float values in input
    def check_decimal(value):
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

#farad convertor
    def faradconverter(t, l):
        if t == "nf":
            l = l / 1000000000
        elif t == "uf":
            l = l / 1000000
        elif t == "pf":
            l = l / 1000000000000
        elif t == "mf":
            l = l / 1000
        else:
            l = l

# convertor
    def meterconverter(lentype, lenn):
        if lentype == 'km':
            m = lenn * 1000
        elif lentype == 'mm':
            m = lenn / 1000
        elif lentype == 'cm':
            m = lenn / 100.0
        elif lentype == 'in':
            m = lenn / 39.37
        elif lentype == 'ft':
            m = lenn / 3.28084
        elif lentype == 'yd':
            m = lenn / 1.094
        elif lentype == 'mi':
            m = lenn * 1609
        else:
            m = lenn
        return m

# weight converter
def wtconverter_to_pounds(val, op):
    if op == 'kg':
        value = val * 2.20462
    elif op == 'US tons':
        value = val * 2000
    elif op == 't':
        value = val * 2204.6226218
    elif op == 'Long tons':
        value = val * 2240
    elif op == 'lb':
        value = val
    return value

#power to metric horsepower
def powerConverter(val, op):
    if op == 'w':
        value = val*0.00135962
    elif op == 'kw':
        value = val*1.35962
    elif op == 'mw':
        value = val*1359.62
    elif op == 'hpl':
        value = val*1.01
    elif op == 'hpm':
        value = val*1.01
    return value



