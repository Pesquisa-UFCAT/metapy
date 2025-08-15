def KNAPSACK(X, INSTANCE):
    """
    Input:
    X
    INSTANCE  |  Instance tag      |     | String
    X         |  Design variables  |     | Py List
    
    Output
    G         |  Constraints       |  $  | Float
    OF        |  Profit            |  $  | Float
    """
    
    if INSTANCE == 'F1-LOWKP-10D':
        PROFIT = [55., 10., 47., 5., 4., 50., 8., 61., 85., 87.]
        COST = [95., 4., 60., 32., 23., 72., 80., 62., 65., 46.]
        COST_MAX = 269
        D = 10
    elif INSTANCE == 'F2-LOWKP-20D':
        PROFIT = [44., 46., 90., 72., 91., 40., 75., 35., 8., 54., 78., 40., 77., 15., 61., 17., 75., 29., 75., 63.]
        COST = [92., 4., 43., 83., 84., 68., 92., 82., 6., 44., 32., 18., 56., 83., 25., 96., 70., 48., 14., 58.]
        COST_MAX = 878
        D = 20
    elif INSTANCE == 'F3-LOWKP-4D':
        PROFIT = [9., 11., 13., 15.]
        COST = [6., 5., 9., 7.]
        COST_MAX = 20
        D = 4
    elif INSTANCE == 'F4-LOWKP-4D':
        PROFIT = [6., 10., 12., 13.]
        COST = [2., 4., 6., 7.]
        COST_MAX = 11
        D = 4
    elif INSTANCE == 'F5-LOWKP-15D':
        PROFIT = [0.125126, 19.330424, 58.500931, 35.029145, 82.284005, 17.410810, 71.050142, 30.399487, 9.140294, 14.731285, 98.852504, 11.908322, 0.891140, 53.166295, 60.176397]
        COST = [56.358531, 80.874050, 47.987304, 89.596240, 74.660482, 85.894345, 51.353496, 1.498459, 36.445204, 16.589862, 44.569231, 0.466933, 37.788018, 57.118442, 60.716575]
        COST_MAX = 375
        D = 15
    elif INSTANCE == 'F6-LOWKP-10D':
        PROFIT = [20., 18., 17., 15., 15., 10., 5., 3., 1., 1.]
        COST = [30., 25., 20., 18., 17., 11., 5., 2., 1., 1.]
        COST_MAX = 60
        D = 10
    elif INSTANCE == 'F7-LOWKP-7D':
        PROFIT = [70., 20., 39., 37., 7., 5., 10.]
        COST = [31., 10., 20., 19., 4., 3., 6.]
        COST_MAX = 50
        D = 7
    elif INSTANCE == 'F8-LOWKP-23D':
        PROFIT = [981., 980., 979., 978., 977., 976., 487., 974., 970., 485., 485., 970., 970., 484., 484., 976., 974., 482., 962., 961., 959., 958., 857.]
        COST = [983., 982., 981., 980., 979., 978., 488., 976., 972., 486., 486., 972., 972., 485., 485., 969., 966., 483., 964., 963., 961., 958., 959.]
        COST_MAX = 10000
        D = 23
    elif INSTANCE == 'F9-LOWKP-5D':
        PROFIT = [33., 24., 36., 37., 12.]
        COST = [15., 20., 17., 8., 31.]
        COST_MAX = 80
        D = 5
    elif INSTANCE == 'F10-LOWKP-20D':
        PROFIT = [91., 72., 90., 46., 55., 8., 35., 75., 61., 15., 77., 40., 63., 75., 29., 75., 17., 78., 40., 44.]
        COST = [84., 83., 43., 4., 44., 6., 82., 92., 25., 83., 56., 18., 58., 14., 48., 70., 96., 32., 68., 92.]
        COST_MAX = 879
        D = 20

    OF = 0
    G = 0
    
    for I in range(len(PROFIT)):
        OF += X[I] * PROFIT[I]
        G += X[I] * COST[I]

    OF *= -1
    COST_VALUE = G
    G -= COST_MAX
    
    return COST_VALUE, G, OF

def KNAPSACK_DIMENSION(INSTANCE):
    """
    Input:
    X
    INSTANCE  |  Instance tag      |     | String
    
    Output
    G         |  Instance dimensions  |     | Integer
    """
    
    if INSTANCE == 'F1-LOWKP-10D':
        D = 10
    elif INSTANCE == 'F2-LOWKP-20D':
        D = 20
    elif INSTANCE == 'F3-LOWKP-4D':
        D = 4
    elif INSTANCE == 'F4-LOWKP-4D':
        D = 4
    elif INSTANCE == 'F5-LOWKP-15D':
        D = 15
    elif INSTANCE == 'F6-LOWKP-10D':
        D = 10
    elif INSTANCE == 'F7-LOWKP-7D':
        D = 7
    elif INSTANCE == 'F8-LOWKP-23D':
        D = 23
    elif INSTANCE == 'F9-LOWKP-5D':
        D = 5
    elif INSTANCE == 'F10-LOWKP-20D':
        D = 20
    
    return D