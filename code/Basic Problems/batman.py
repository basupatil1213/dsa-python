def nanana_batman(x):
    return "batman!" if x <= 0 else "na"*x + " batman!"






def call_methods():
    print(nanana_batman(0))  # "batman!"
    print(nanana_batman(10))  # "na batman!"
    print(nanana_batman(-1))  # "batman!"