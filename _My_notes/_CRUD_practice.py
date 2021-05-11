print("------create------")
std_name = "venkatesh"
pasd_out = 2017
is_reg = True
brch = "eee"

print("-------retrival--------")
print("Std_name", std_name)
print("pasd_out", pasd_out)
print("Reg or distance", is_reg)
print("branch", brch)

print("---------update-------")
std_name = "raju"
brch = "cse"
print("Std_name", std_name)
print("Pasd_out", pasd_out)
print("Reg or distance", is_reg)
print("Branch", brch)

print("--------delete---------")
print(std_name, pasd_out, is_reg, brch)
del std_name
print(pasd_out, is_reg, brch)
del pasd_out
print(is_reg, brch)
del is_reg
print(brch)
del brch