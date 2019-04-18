
# 1000 gram meat
#
# NitroSalt: 10
# Salt: 15
# ActivateCultures: 0.5
# Sugar: 5
# 2 days each 500 gramm




def nitro_salt(m):
    # 1000 : 10 = m :
    try:
        m = int(m)
    except:
        m = 0
    return int(10 * m / 1000)





def salt(m):
    # 1000 : 15 = m
    return 15 * m / 1000

def cultures(m):
    return 0.5 * m / 1000

def sugar(m):
    return 5 * m / 1000

def days(m):
    return 4 * m / 1000


print(cultures(500))
print(salt(1000))
