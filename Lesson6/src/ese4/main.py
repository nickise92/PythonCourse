# Exercise 4
def load_experiment(file_name):
    datas = []
    with open(file_name, 'r') as f:
        for line in f:
            datas.append(line.split(','))
    datas.pop(0)

    measure = []
    power = []
    gain = []
    for d in datas:
        measure.append(int(d[0]))
        power.append(float(d[1]))
        gain.append(float(d[2]))

    return measure, power, gain
            

def mean(l):
    sum = 0
    for v in l:
        sum += v

    return sum / len(l)

def median(l):
    n = len(l)
    s = sorted(l)
    if n % 2 == 0:
        # if data set is even
        return (s[(n//2)-1] + s[n//2]) / 2
    else:
        # if data set is odd
        return (l[len(l)//2])

# MAIN:
m, p, g = load_experiment('experiment_data.csv')
testList = [1, 2, 3, 4, 5, 6, 8, 9]

m_mean = mean(m)
p_mean = mean(p)
g_mean = mean(g)

print(f'The mean of the measure is: {m_mean}, the mean of the power is: {p_mean} and the mean of the gain is: {g_mean}.')

m_median = median(m)
p_median = median(p)
g_median = median(g)

print(f'The median of the measure is: {m_median}, the median of the power is: {p_median} and the median of the gain is: {g_median}.')
print('#' * 60)
power_dict= dict()
gain_dict = dict()

for i in range(len(m)):
    if m[i] in power_dict:
        power_dict.setdefault(m[i], power_dict.get(m[i]).append(p[i]))
    else:
        power_dict.setdefault(m[i], [p[i]])
        
    if m[i] in gain_dict:
        gain_dict.setdefault(m[i], gain_dict.get(m[i]).append(g[i]))
    else:
        gain_dict.setdefault(m[i], [g[i]])
        
for k in power_dict.keys():
    avg = mean(power_dict.get(k))
    print(f'For measure {k} the average power is: {avg}')

print('#' * 60)
for k in gain_dict.keys():
    avg = mean(gain_dict.get(k))
    print(f'For measure {k} the average gain is: {avg}')


