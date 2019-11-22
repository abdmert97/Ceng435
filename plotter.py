from scipy.stats import sem, t
from scipy import mean
import matplotlib.pyplot as plt
import numpy as np
def getConfidenceIntervalAndPlotGraph():
    confidence = 0.95
    f20= open("20ms.txt","r+")
    f40= open("40ms.txt","r+")
    f50= open("50ms.txt","r+")
    
    data20 = []
    lines20 = f20.readlines()
    for line in lines20:
         data20.append(float(line.split('\n')[0]))
    f20.close()

    data40 = []
    lines40 = f40.readlines()
    for line in lines40:
         data40.append(float(line.split('\n')[0]))
    f40.close()
    data50 = []
    lines50 = f50.readlines()
    for line in lines50:
         data50.append(float(line.split('\n')[0]))
    f50.close()


   
    n20 = len(data20)
    m20 = mean(data20)
    std_err20 = sem(data20)
    confidenceInterval20 = std_err20 * t.ppf((1 + confidence) / 2, n20 - 1)

    n40 = len(data40)
    m40 = mean(data40)
    std_err40 = sem(data40)
    confidenceInterval40 = std_err40 * t.ppf((1 + confidence) / 2, n40 - 1)  

    n50 = len(data50)
    m50 = mean(data50)
    std_err50 = sem(data50)
    confidenceInterval50 = std_err50 * t.ppf((1 + confidence) / 2, n50 - 1)  
  
    plotGraph([20,40,50],[m20,m40,m50],[confidenceInterval20,confidenceInterval40,confidenceInterval50])
   

def plotGraph(listX,listY,error):
    avg = 0
    for e in error:
        avg+= e
    avg = avg/3
    print(error[0])
    print(error[1])
    print(error[2])
    plt.errorbar(listX,listY, yerr=error, fmt='.k')
    plt.xlabel('network emulation delay(ms)')
    plt.ylabel('end-to-end delay(ms)')
    plt.show()
