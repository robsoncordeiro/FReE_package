import random
import math

# A dict with the std for each feature of a given dataset (Change it for your dataset)
dict_feature = {
0:0.5653777011086821,
1:1.0088265271412988,
2:1.006346329628135,
3:0.6000184917287497,
4:1.0063262097577417,
5:0.47497474748208457,
6:1.009302998729834,
7:1.005901133509622,
8:1.0278075745389876,
9:0.4999938629754578,
10:1.0093305135554005,
11:1.0061544361071129,
12:1.0493980467427613,
13:0.4876623479668582,
14:1.0087467550832716,
15:1.0063049907729718,
16:1.1936755758259998,
17:0.5057776865399287,
18:1.0076942716151907,
19:1.0063656333478728,
20:1.4002093860905722,
21:0.6746353681519813,
22:0.3808074123595258,
23:0.16457625130316283,
24:0.39744531681187606,
25:0.525406272889298,
26:0.36525562144604234,
27:0.3133377909489078
}

# Setting the noise configuration
noise_d = {
    0.2: 1000000.0,
    1.0: 200000.0,
    2.0: 100000.0,
    5.0: 40000.0,
    7.0: 29000.0,
    10.0: 20000.0
}

# Start the factor value with a valid noise configuration
factor = noise_d[0.2]

t = 1

# Generate an expression to be used for create redundant attributes
def get_expr(t=None, noise=0, qt_att=1, corr_att=1):
    feature = random.randint(0, 27)
    constant = random.randint(1, 200)

    if t=='mix':
        #list_corr = ['linear', 'e2', 'e3', 'e10', 'e100', 'log', 'sin', 'exp']
        list_corr = ['linear', 'e2', 'e3', 'e10']
        t = list_corr[random.randint(1, len(list_corr)) - 1]


    if t == 'linear':  # linear
        expr = ('({%d}*(({rand{%d}}/{%d})+[%d]))' % (
        constant, random.randint(1, (int(dict_feature[feature] * 100000))) / 100.0, noise*corr_att, feature))
    elif t == 'e2':  # e2
        expr = ('({%d}*((({rand{%d}}/{%d})+[%d])^{2}))' % (
        constant, random.randint(1, (int(dict_feature[feature] * 100000))) / 100.0, noise*corr_att, feature))
    elif t == 'e3':  # e3
        expr = ('({%d}*((({rand{%d}}/{%d})+[%d])^{3}))' % (
        constant, random.randint(1, (int(dict_feature[feature] * 100000))) / 100.0, noise*corr_att, feature))
    elif t == 'e10':  # e10
        expr = ('({%d}*((({rand{%d}}/{%d})+[%d])^{10}))' % (
        constant, random.randint(1, (int(dict_feature[feature] * 100000))) / 100.0, noise*corr_att, feature))
    elif t == 'e100':  # e100
        expr = ('({%d}*((({rand{%d}}/{%d})+[%d])^{100}))' % (
        constant, random.randint(1, (int(dict_feature[feature] * 100000))) / 100.0, noise*corr_att, feature))
    elif t == 'log':  # log
        expr = ('({%d}*l((({rand{%d}}/{%d})+[%d])+{10000}))' % (
        constant, random.randint(1, (int(dict_feature[feature] * 100000))) / 100.0, noise*corr_att, feature))
    elif t == 'sin':  # sin
        expr = ('({%d}*s((({rand{%d}}/{%d})+[%d])))' % (
        constant, random.randint(1, (int(dict_feature[feature] * 100000))) / 100.0, noise*corr_att, feature))
    else:
        expr = ('({%d}^(({rand{%d}}/{%d})+[%d]))' % (
        constant, random.randint(1, (int(dict_feature[feature] * 100000))) / 100.0, noise*corr_att, feature))

    return expr


def generateDataExpressions(corr_att, qt_att, t_exp, noise, output):
    with open(output, 'w') as f:
        for i in range(qt_att):
            exp = '"'

            for j in range(corr_att):
                exp = exp + get_expr(t_exp, noise_d[noise], qt_att, corr_att)
                if j < corr_att - 1:
                    exp = exp + '+'

            if i < qt_att - 1:
                exp = exp + '",\n'
            else:
                exp = exp + '"\n'
            f.write(exp)


list_corr = ['linear', 'e2', 'e3', 'e10', 'e100', 'log', 'sin', 'exp', 'mix']
list_corr = ['mix']
list_noise = [0.2, 1.0, 2.0, 5.0, 7.0, 10.0]
#list_noise = [10.0]
#list_corr_att = [2, 4, 8, 12, 20, 28]

list_qt_attr = [1, 5, 10, 20, 50, 100]
#list_corr_att = [2, 4, 8, 12]
list_corr_att = [1, 1, 1, 1, 1, 1]

#qt_of_attributes = 5
for qt_of_attributes in list_qt_attr:
	for corr in list_corr:
	    for ind in range(len(list_corr_att)):
	    #for corr_att in list_corr_att:
	        #for noise in list_noise:
	        print(list_corr[random.randint(1, len(list_corr))-1])
	        generateDataExpressions(list_corr_att[ind], qt_of_attributes, corr, list_noise[ind], ('HIGGS_%s_approx_%d_p%d_%d.txt' % (corr, qt_of_attributes, list_corr_att[ind], list_noise[ind]*10)))
