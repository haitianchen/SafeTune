import sys
import matplotlib.pyplot as plt

y_variable = 'tps'


def parse_file(file):
    f = open(file)
    lines = f.readlines()
    resL = []
    for line in lines:
        tmp = line.split('|')
        for t in tmp:
            if y_variable in t and not('env initialized' in t ) and not('LHS' in t ) and not('GP-BOTORCH' in t) and not('Var' in t):
           #     print('t = ',t)
                res = float(t.split('_')[1])

                if y_variable == 'lat':
                    res = -res
              #  print(res)
                resL.append(res)

    return resL

def plot_res(file):
    resL = parse_file(file)
    plt.figure()
    plt.scatter(resL)
    plt.xlabel('Iteration')
    plt.ylabel(y_variable)
    plt.savefig("{}.png".format(file.split('.')[0]))
   # plt.show()
    plt.close()
def plot_resLine(file):
    resL = parse_file(file)
    plt.figure()
    x =[i for i  in range(0,len(resL)) ]
    plt.plot(x,resL)
    plt.xlabel('Iteration')
    plt.ylabel(y_variable)
    plt.savefig("{}.png".format(file.split('.')[0]))
    plt.close()
def analyze_res(file):
    resL = parse_file(file)
    best_res = -1e9
    res_record = []
    for i in range(len(resL)):
        if resL[i] > best_res:
            best_res = resL[i]
        if i == 50:
            print ("Best Result in  50 interations {}".format(best_res, file))
            res_record.append(best_res)
        if i == 100:
            print ("Best Result in 100 interations: {}".format(best_res))
            res_record.append(best_res)
        if i == 150:
            print ("Best Result in 150 interations: {}".format(best_res))
            res_record.append(best_res)

    print ("Best Result in over 200 interations: {}".format(best_res))
    res_record.append(best_res)
    f = open("./tem_results.txt", 'w')
    f.write("{}|{}\n".format(file,res_record))
    f.close()

if __name__ == '__main__':
    result_file = sys.argv[1]
    y_variable = sys.argv[2]
    analyze_res(result_file)
    plot_resLine(result_file)
  #  plot_res(result_file)
