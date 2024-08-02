'''
Title: Mean Median and Mode Finder
Author: HDz(https://github.com/hdz-088/)
Date of Creation: 17th April, 2024
Last Update: 20th April, 2024
'''

# ==== Insertion Functions

def insertingFI():
    """
    Function to Input Frequency(Fi)
    """
    fi_str = input("Enter Fi separated by comma: ")
    fi = fi_str.split(',')
    fi = [float(x) for x in fi]
    print("Fi:", fi)
    return fi

def insertingXI():
    """
    Function to Input Xi
    """
    xi_str = input("Enter Xi separated by comma: ")
    xi = xi_str.split(',')
    xi = [float(x) for x in xi]
    print("Xi:", xi)
    return xi

def insertingClassS():
    """
    Function to Input Class Lower Limit
    """
    classS_str = input("Enter Class Starting Points separated by comma: ")
    classS = classS_str.split(',')
    classS = [float(x) for x in classS]
    print("ClassS:", classS)
    return classS

def insertingclassE():
    """
    Function to Input Class Upper Limit
    """
    classE_str = input("Enter Class Ending Points separated by comma: ")
    classE = classE_str.split(',')
    classE = [float(x) for x in classE]
    print("classE:", classE)
    return classE

def findingXI(classE, classS):
    """
    Function to Find Xi From Upper and Lower Limits [(U-L)/2]
    """
    xi = []
    n = 0
    while n < len(classS):
        xi.append((classE[n]+classS[n])/2)
        n = n+1
    return xi

def insertingH():
    """
    Function to Input Class Size (h)
    """
    h = float(input("Enter h(Class Size): "))
    return h

def findingH(classE, classS):
    """
    Function to Find Class Size (h) From Upper and Lower limits
    """
    h = classE[0]-classS[0]
    return h

def maxFrequency(fi):
    """
    Function to Find Max Frequency for Mode
    """
    maxFreq = 0
    limit = 0
    term = 0
    while limit < len(fi):
        if maxFreq < fi[limit]:
            maxFreq = fi[limit]
        limit = limit + 1
    return maxFreq

def cfTerm(fi):
    n = 0
    maxFreq = 0
    term = 0
    while n < len(fi):
        if maxFreq < fi[n]:
            maxFreq = fi[n]
            term = n
        n = n + 1
    return term

def findingCF(fi):
    """
    Function to Find Cumulative Frequency(CF) For Mode
    """
    term = cfTerm(fi)
    cfreq = 0
    n = 0
    while n < term:
        cfreq = cfreq + fi[n]
        n = n+1
    return cfreq
    
def findingL(fi, classS):
    """
    Function to Find Model Class Lower Limit For Mode
    """
    term = cfTerm(fi)
    l = classS[term]
    return l

# ==== Calculation Functions

def woFrequency(xi):
    """
    Function to Find Mean For Data Without Frequency 
    x̄ = ΣXi/n ; n = number of data
    """
    n = 0
    sum_xi = sum(xi)
    print("---------------")
    print(f"|\tXi\t|")
    print("---------------")
    while n < len(xi):
        print(f"|\t{xi[n]}\t|")
        n = n+1
    print("----------------")
    print(f"|\t{sum_xi}\t|")
    print("----------------")
    n=len(xi)
    mean = (sum_xi)/n
    print(f"Simple Mean x̄ = {mean}")
    return mean

def wFreq(xi, fi):
    """
    Function to Find Mean For Data With Frequency 
    x̄ = ΣFiXi/n ; n = sum of frequency
    """
    n = 0
    sum_fixi = 0
    sum_fi = sum(fi)
    print("-------------------------------------------------")
    print(f"|\tXi\t|\tFi\t|\tFiXi\t|")
    print("-------------------------------------------------")
    while n < len(xi):
        fixi = xi[n]*fi[n]
        print(f"|\t{xi[n]}\t|\t{fi[n]}\t|\t{fixi}\t|")
        sum_fixi = sum_fixi + fixi
        n = n+1
    print("-------------------------------------------------")
    print(f"|\t--\t|\t{sum_fi}\t|\t{sum_fixi}\t|")
    print("-------------------------------------------------")
    mean = sum_fixi/sum_fi
    print(f"\n Mean = {mean}\n")
    return mean

def assumed_mean(xi,fi):
    """
    Function to Find Mean By Assumed Mean Method 
    x̄ = A + (ΣFiDi/n) ; n = sum of frequency, A = assumed point
    """
    a = xi[round(len(xi)/2)]
    sum_fidi = 0
    sum_fi = sum(fi)
    n = 0   
    print("-----------------------------------------------------------------")
    print(f"|\tXi\t|\tFi\t|\tDi=Xi-A\t|\tFiDi\t|")
    print("-----------------------------------------------------------------")
    while n < len(xi):
        di = xi[n]-a
        fidi = fi[n] * di
        print(f"|\t{xi[n]}\t|\t{fi[n]}\t|\t{di}\t|\t{fidi}\t|")
        sum_fidi = sum_fidi + fidi
        n = n+1
    print("-----------------------------------------------------------------")
    print(f"|\t--\t|\t{sum_fi}\t|\t--\t|\t{sum_fidi}\t|")
    print("-----------------------------------------------------------------")
    print(f"\nHere we will take A = {a}\n")
    mean = a+(sum_fidi/sum_fi)
    print(f"x̄ = {mean}\n")
    return mean

def step_deviation(xi, fi, h):
    """
    Function to Find Mean By Step Deviation Method 
    x̄ = A + h(ΣFiUi/n) ; n = sum of frequency, A = assumed point, h = size of class
    """
    a = xi[round(len(xi)/2)]
    sum_fiui = 0
    sum_fi = sum(fi)
    n = 0   
    print("-----------------------------------------------------------------")
    print(f"|\tXi\t|\tFi\t|\tUi=Di/h\t|\tFiUi\t|")
    print("-----------------------------------------------------------------")
    while n < len(xi):
        ui = (xi[n]-a)/h
        fiui = fi[n] * ui
        print(f"|\t{xi[n]}\t|\t{fi[n]}\t|\t{ui}\t|\t{fiui}\t|")
        sum_fiui = sum_fiui + fiui
        n = n+1
    print("-----------------------------------------------------------------")
    print(f"|\t--\t|\t{sum_fi}\t|\t--\t|\t{sum_fiui}\t|")
    print("-----------------------------------------------------------------")
    print(f"\nHere we will take A = {a}\n")
    mean = (a+(h*(sum_fiui / sum_fi)))
    print(f"x̄ = {mean}\n")
    return mean
    
def woFreqHM(xi):
    """
    Function to Find Harmonic Mean For Data Without Frequency 
    x̄ = (n / Σ(1/Xi))
    """
    n = 0
    sum_denominator = 0
    print("-----------------------------------------")
    print("|\tXi\t|\t1/Xi\t|")
    while n < len(xi):
        print("-----------------------------------------")
        denominator = 1 / xi[n]
        sum_denominator = sum_denominator + denominator
        print(f"|\t{xi[n]}\t|\t{denominator}\t|")
        n = n+1
    print("-----------------------------------------")
    print(f"|\t---\t|\t{sum_denominator}\t|")
    print("-----------------------------------------")
    mean = len(xi)/sum_denominator
    print(f"\nHarmonic Mean = {mean}")
    return mean

def wFreqHM(xi,fi):
    """
    Function to Find Harmonic Mean For Data With Frequency 
    x̄ = (ΣFi/Σ(Fi/Xi))
    """
    n = 0
    sum_denominator = 0
    sum_fi = sum(fi)
    print("-----------------------------------------")
    print("|\tXi\t|\tFi\t|\tFi/Xi\t|")
    while n < len(xi):
        print("-----------------------------------------")
        denominator = fi[n] / xi[n]
        sum_denominator = sum_denominator + denominator
        print(f"|\t{xi[n]}\t|\t{fi[n]}\t|\t{denominator}\t|")
        n = n+1
    print("-----------------------------------------")
    print(f"|\t---\t|\t{sum_fi}\t|\t{sum_denominator}\t|")
    print("-----------------------------------------")
    mean = sum_fi/sum_denominator
    print(f"\nHarmonic Mean = {mean}\n")
    return mean
    
def geoMean(xi,fi):
    """
    Function To Find Geometric Mean Using Reltion Formula
    GM^2 = Arithmetic Mean * Harmonic Mean
    """
    amean = wFreq(xi,fi)
    hmean = wFreqHM(xi,fi)
    gm = (amean*hmean)
    gm = pow(gm,1/2)
    print(f"Geometric Mean GM = {gm}")
    
# >>> MEDIAN

def woFreqMedian(xi):
    """
    Function To Find Meadin For Data Without Frequency
    """
    xi.sort()
    print(f"Sorted: {xi}")
    n = len(xi)
    median = 0
    if (n%2==0):
        term1 = xi[int(n/2)-1] # Because Index start from 0
        term2 = xi[int(n/2)]
        median = (term1+term2)/2
    elif (n%2!=0):
        term = int(n/2)
        median = xi[term]
    else:
        print("Invalid Input")
    print(f"\nMedian M = {median}\n")
    return median

# def wFreqMedian(fi, classS, classE, h):
#     """
#     Function To Find Median For Data With Frequency
#     """
#     sum_fi = sum(fi)
#     maxFreq = maxFrequency(fi)
#     cf = findingCF(fi)
#     lower = findingL(fi, classS)
#     cumfreq = 0
#     n = 0
#     # Printing Table
#     print("\n-------------------------------------------------")
#     print(f"|\tClass\t|\tFi\t|\tcf\t|")
#     print("-------------------------------------------------")
#     while n < len(fi):
#         cumfreq = cumfreq+fi[n]
#         print(f"|\t{classS[n]}-{classE[n]}\t|\t{fi[n]}\t|\t{cumfreq}\t|")
#         n = n+1
#     print("-------------------------------------------------")
#     print(f"|\t--\t|\tn={sum_fi}\t|\t---\t|")
#     print("-------------------------------------------------\n")
#     print(f"Here, L = {lower}\nn={sum_fi},  n/2 = {sum_fi/2} \nF = {maxFreq}, \nH={h},\nCF = {cf} \n")
#     median = ((sum_fi/2) - cf)/maxFreq
#     median = (median * h)+lower
#     print(f"Median M = {median}")
#     return median

def wFreqMedian(fi, classS, classE, h):
    sum_fi = sum(fi)
    cf = [0] * len(fi)
    cf[0] = fi[0]
    for i in range(1, len(fi)):
        cf[i] = cf[i-1] + fi[i]
    median_cf = sum_fi / 2
    median_class_index = 0
    for i in range(len(cf)):
        if cf[i] >= median_cf:
            median_class_index = i
            break
    lower_limit = classS[median_class_index]
    cumulative_freq_before_median = cf[median_class_index] - fi[median_class_index]
    frequency_of_median_class = fi[median_class_index]
    median = lower_limit + ((median_cf - cumulative_freq_before_median) / frequency_of_median_class) * h
    print(f"Median = {median}")
    return median


# >>> MODE

def mode(fi, xi, classS, classE, h):
    """
    Function To Find Mode Using Relational Method
    """
    sum_fi = sum(fi)
    maxFreq = maxFrequency(fi)
    cf = findingCF(fi)
    lower = findingL(fi, classS)
    cumfreq = 0
    n = 0
    sum_fixi = 0
    # Printing Table
    print("\n-------------------------------------------------------------------------------")
    print(f"|\tClass\t|\tFi\t|\tXi\t|\tFiXi\t|\tcf\t|")
    print("---------------------------------------------------------------------------------")
    while n < len(fi):
        fixi = xi[n]*fi[n]
        cumfreq = cumfreq+fi[n]
        print(f"|\t{classS[n]}-{classE[n]}\t|\t{fi[n]}\t|\t{xi[n]}\t|\t{fixi}\t|\t{cumfreq}\t|")
        sum_fixi = sum_fixi + fixi
        n = n+1
    print("---------------------------------------------------------------------------------")
    print(f"|\t--\t|\tn={sum_fi}\t|\t---\t|Sum Fixi={sum_fixi}|\t---\t|")
    print("---------------------------------------------------------------------------------\n")
    print(f"Here, L = {lower}\nn={sum_fi},  n/2 = {sum_fi/2} \nF = {maxFreq}, \nH={h},\nCF = {cf} \n")
    mean = sum_fixi/sum_fi
    print(f"Mean = {mean}\n")
    median = ((sum_fi/2) - cf)/maxFreq
    median = (median * h)+lower
    print(f"Median = {median}\n")
    mode = (3*(median)) - (2*(mean))
    print(f"Mode = {mode}")
    return mode

# ==== INTRO

def intro():
    print("\n>>> Mean")
    print("Enter 01. For Simple Mean (Without Frequency)")
    print("Enter 02. For Simple Mean (With Frequency)")
    print("Enter 03. For Assumed Mean (Without Xi)")
    print("Enter 04. For Assumed Mean (With Xi)")
    print("Enter 05. For Step Deviation Method Mean (Without Xi)")
    print("Enter 06. For Step Deviation Method Mean (With Xi)")
    print("Enter 07. For Harmonic Mean (Without Frequency)")
    print("Enter 08. For Harmonic Mean (With Frequency)")
    print("Enter 09. For Geometric Mean(using Relation Formula)")
    print("\n>>> Median")
    print("Enter 10. For Median(Without Frequency)")
    print("Enter 11. For Median(With Frequency)")
    print("\n>>> Mode")
    print("Enter 12. For Mode")

    option = int(input())
    return option

def deciding(option):
    
    if (option == 1):
        print("Simple Mean (Without Frequency)")
        xi = insertingXI()
        woFrequency(xi)
        
    elif (option == 2):
        print("Simple Mean (With Frequency)")
        xi = insertingXI()
        fi = insertingFI()
        wFreq(xi,fi)
        
    elif (option == 3):
        print("Assumed Mean (Without Xi)")
        classS = insertingClassS()
        classE = insertingclassE()
        xi = findingXI(classE, classS)
        fi = insertingFI()
        assumed_mean(xi,fi)
        
    elif (option == 4):
        print("Assumed Mean (With Xi)")
        xi = insertingXI()
        fi = insertingFI()
        assumed_mean(xi,fi)
        
    elif (option == 5):
        print("Step Deviation Method Mean (Without Xi)")
        classS = insertingClassS()
        classE = insertingclassE()
        xi = findingXI(classE, classS)
        fi = insertingFI()
        h = insertingH()
        step_deviation(xi, fi, h)
        
    elif (option == 6):
        print("Step Deviation Method Mean (With Xi)")
        xi = insertingXI
        fi = insertingFI()
        h = insertingH()
        step_deviation(xi, fi, h)
        
    elif (option == 7):
        print("Harmonic Mean (Without Frequency)")
        xi = insertingXI()
        woFreqHM(xi)
        
    elif (option == 8):
        print("Harmonic Mean (With Frequency)")
        xi = insertingXI()
        fi = insertingFI()
        wFreqHM(xi,fi)
        
    elif (option == 9):
        print("Geometric Mean(using Relation Formula)")
        xi = insertingXI()
        fi = insertingFI()
        geoMean(xi,fi)
        
    elif (option == 10):
        print("Median Without Frequency")
        xi = insertingXI()
        woFreqMedian(xi)
        
    elif (option == 11):
        print("Median With Frequency")
        fi = insertingFI()
        classS = insertingClassS()
        classE = insertingclassE()
        h = findingH(classE, classS)
        wFreqMedian(fi, classS, classE, h)
        
    elif (option == 12):
        print("Mode")
        fi = insertingFI()
        classS = insertingClassS()
        classE = insertingclassE()
        h = findingH(classE, classS)
        xi = findingXI(classE, classS)
        mode(fi, xi, classS, classE, h)
        
    else: 
        print("Invalid Input. Try Again!")
        deciding(intro())
        

deciding(intro())