################################################################################
# UNIVERSIDADE FEDERAL DE CATALÃO (UFCAT)
# WANDERLEI MALAQUIAS PEREIRA JUNIOR,                  ENG. CIVIL / PROF (UFCAT)
# JOÃO V. COELHO ESTRELA,                                     ENG. MINAS (UFCAT)
# MATHEUS TOLEDO,												    COMP. (UNIP)
################################################################################

################################################################################
# DESCRIÇÃO ALGORITMO:
# BIBLIO. DE FUNÇÕES GRÁFICAS DA PLATAFORMA "META OPTIMIZATION TOOLBOX" DESENVOL-
# VIDA PELO GRUPO DE PESQUISAS E ESTUDOS EM ENGENHARIA.
################################################################################

################################################################################
# BIBLIOTECAS NATIVAS PYTHON
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

################################################################################
# BIBLIOTECAS DESENVOLVEDORES GPEE

# CONVERTE A ENTRADA DE SI (SISTEMA INTERNACIONAL) PARA POLEGADAS    
def CONVERT_SI_TO_INCHES(WIDTH, HEIGHT):
    """ 
    This function convert figure size meters to inches
    
    Input:
    WIDTH: Figure width in SI units, (float)
    HEIGHT: Figure height in SI units, (float)
    
    Output:
    WIDTH: Figure width in INCHES units, (float)
    HEIGHT: Figure height in INCHES units, (float)
    """
    WIDTH = WIDTH / 0.0254
    HEIGHT = HEIGHT / 0.0254
    return WIDTH, HEIGHT

# SALVA A FIGURA NA PASTA OU CAMINHO DESEJADO
def SAVE_GRAPHIC(NAME, EXT, DPI):
    """ 
    This function save graphics on a specific path
    extensions options

    - 'svg'
    - 'png'
    - 'eps'
    - 'pdf'

    Input: 
    NAME: Path + name figure (string)
    EXT: File extension (string)
    DPI: The resolution in dots per inch (integer)
    """
    plt.savefig(NAME + '.' + EXT, dpi = DPI, bbox_inches='tight', transparent=True)

# PLOTAGEM 1: GRÁFICO DUPLO FO + APTIDÃO
def META_PLOT_001(DATASET, PLOT_SETUP):
	"""
    OF + FIT chart - Line chart

    Input:  
    DATASET: META Optimization toolbox results (Python dictionary)
    PLOT_SETUP: Chart setup
    
    Output:
    The image is saved in the current directory 
	"""
	NAME = PLOT_SETUP['NAME']
	W = PLOT_SETUP['WIDTH']
	H = PLOT_SETUP['HEIGHT']
	EXT = PLOT_SETUP['EXTENSION']
	DPI = PLOT_SETUP['DPI']
	COLOR_OF = PLOT_SETUP['COLOR OF']
	MARKER_OF = PLOT_SETUP['MARKER OF']
	COLOR_FIT = PLOT_SETUP['COLOR FIT']
	MARKER_FIT = PLOT_SETUP['MARKER FIT']
	MARKER_SIZE = PLOT_SETUP['MARKER SIZE']
	LINE_WIDTH = PLOT_SETUP['LINE WIDTH']
	LINE_STYLE = PLOT_SETUP['LINE STYLE']
	Y_OF_AXIS_LABEL = PLOT_SETUP['OF AXIS LABEL']
	X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
	LABELS_SIZE = PLOT_SETUP['LABELS SIZE']     
	LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
	X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
	Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
	AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
	GRID = PLOT_SETUP['ON GRID?']
	X = DATASET['X']
	Y_0 = DATASET['OF']
	Y_1 = DATASET['FIT']
	# Convert units of size figure
	W, H = CONVERT_SI_TO_INCHES(W, H)
	# Plot
	FIG, AX= plt.subplots(2, 1, figsize = (W, H), sharex = True)
	AX[0].plot(X, Y_0, marker = MARKER_OF, color = COLOR_OF, linestyle = LINE_STYLE, linewidth = LINE_WIDTH, markersize = MARKER_SIZE)
	AX[1].plot(X, Y_1, marker = MARKER_FIT, color = COLOR_FIT, linestyle = LINE_STYLE, linewidth = LINE_WIDTH, markersize = MARKER_SIZE)
	font = {'fontname': 'Arial',
			'color':  LABELS_COLOR,
			'weight': 'normal',
			'size': LABELS_SIZE}
	AX[0].set_ylabel(Y_OF_AXIS_LABEL, fontdict = font)
	AX[1].set_xlabel(X_AXIS_LABEL, fontdict = font)
	AX[1].set_ylabel('Fitness', fontdict = font)          
	AX[0].tick_params(axis= 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
	AX[0].tick_params(axis= 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
	AX[1].tick_params(axis= 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
	AX[1].tick_params(axis= 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
	if GRID == True:
		AX[0].grid(color = 'grey', linestyle = '-.', linewidth = 1, alpha = 0.20)
		AX[1].grid(color = 'grey', linestyle = '-.', linewidth = 1, alpha = 0.20)
	SAVE_GRAPHIC(NAME, EXT, DPI)

# PLOTAGEM 2: GRÁFICO ÚNICO FO OU APTIDÃO OU PIOR OU MÉDIA
def META_PLOT_002(DATASET, PLOT_SETUP):
	"""
    OF or FIT chart - Line chart

    Input:  
    DATASET: META Optimization toolbox results (Python dictionary)
    PLOT_SETUP: Chart setup
    
    Output:
    The image is saved in the current directory 
	"""
	NAME = PLOT_SETUP['NAME']
	W = PLOT_SETUP['WIDTH']
	H = PLOT_SETUP['HEIGHT']
	EXT = PLOT_SETUP['EXTENSION']
	DPI = PLOT_SETUP['DPI']
	COLOR = PLOT_SETUP['COLOR']
	MARKER = PLOT_SETUP['MARKER']
	MARKER_SIZE = PLOT_SETUP['MARKER SIZE']
	LINE_WIDTH = PLOT_SETUP['LINE WIDTH']
	LINE_STYLE = PLOT_SETUP['LINE STYLE']
	Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
	X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
	LABELS_SIZE = PLOT_SETUP['LABELS SIZE']     
	LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
	X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
	Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
	AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
	GRID = PLOT_SETUP['ON GRID?']
	X = DATASET['X']
	Y = DATASET['Y']
	# Convert units of size figure
	W, H = CONVERT_SI_TO_INCHES(W, H)
	# Plot
	FIG, AX= plt.subplots(1, 1, figsize = (W, H), sharex = True)
	AX.plot(X, Y, marker = MARKER, color = COLOR, linestyle = LINE_STYLE, linewidth = LINE_WIDTH, markersize = MARKER_SIZE)
	font = {'fontname': 'Arial',
			'color':  LABELS_COLOR,
			'weight': 'normal',
			'size': LABELS_SIZE}
	AX.set_ylabel(Y_AXIS_LABEL, fontdict = font)
	AX.set_xlabel(X_AXIS_LABEL, fontdict = font)   
	AX.tick_params(axis= 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
	AX.tick_params(axis= 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
	if GRID == True:
		AX.grid(color = 'grey', linestyle = '-.', linewidth = 1, alpha = 0.20)
	SAVE_GRAPHIC(NAME, EXT, DPI)

# PLOTAGEM 3: GRÁFICO ÚNICO FO + PIOR + MÉDIA
def META_PLOT_003(DATASET, PLOT_SETUP):
	"""
    OF - Line chart

    Input:  
    DATASET: META Optimization toolbox results (Python dictionary)
    PLOT_SETUP: Chart setup
    
    Output:
    The image is saved in the current directory 
	"""
	NAME = PLOT_SETUP['NAME']
	W = PLOT_SETUP['WIDTH']
	H = PLOT_SETUP['HEIGHT']
	EXT = PLOT_SETUP['EXTENSION']
	DPI = PLOT_SETUP['DPI']
	COLOR_1 = PLOT_SETUP['COLOR OF BEST']
	COLOR_2 = PLOT_SETUP['COLOR OF WORST']
	COLOR_3 = PLOT_SETUP['COLOR OF AVERAGE']
	MARKER_1 = PLOT_SETUP['MARKER OF BEST']
	MARKER_2 = PLOT_SETUP['MARKER OF WORST']
	MARKER_3 = PLOT_SETUP['MARKER OF AVERAGE']
	MARKER_SIZE = PLOT_SETUP['MARKER SIZE']
	LINE_WIDTH = PLOT_SETUP['LINE WIDTH']
	LINE_STYLE = PLOT_SETUP['LINE STYLE']
	Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
	X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
	LABELS_SIZE = PLOT_SETUP['LABELS SIZE']     
	LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
	X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
	Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
	AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
	GRID = PLOT_SETUP['ON GRID?']
	LOC = PLOT_SETUP['LOC LEGEND']
	SIZE_LEGEND = PLOT_SETUP['SIZE LEGEND']
	X = DATASET['X']
	Y_1 = DATASET['OF BEST']
	Y_2 = DATASET['OF WORST']
	Y_3 = DATASET['OF AVERAGE']
	# Convert units of size figure
	W, H = CONVERT_SI_TO_INCHES(W, H)
	# Plot
	FIG, AX= plt.subplots(1, 1, figsize = (W, H), sharex = True)
	AX.plot(X, Y_1, marker = MARKER_1, color = COLOR_1, linestyle = LINE_STYLE, linewidth = LINE_WIDTH, markersize = MARKER_SIZE, label='Best')
	AX.plot(X, Y_2, marker = MARKER_2, color = COLOR_2, linestyle = LINE_STYLE, linewidth = LINE_WIDTH, markersize = MARKER_SIZE, label='Worst')
	AX.plot(X, Y_3, marker = MARKER_3, color = COLOR_3, linestyle = LINE_STYLE, linewidth = LINE_WIDTH, markersize = MARKER_SIZE, label='Average')
	font = {'fontname': 'Arial',
			'color':  LABELS_COLOR,
			'weight': 'normal',
			'size': LABELS_SIZE}
	AX.set_ylabel(Y_AXIS_LABEL, fontdict = font)
	AX.set_xlabel(X_AXIS_LABEL, fontdict = font)   
	AX.tick_params(axis= 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
	AX.tick_params(axis= 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
	if GRID == True:
		AX.grid(color = 'grey', linestyle = '-.', linewidth = 1, alpha = 0.20)
	plt.legend(loc = LOC, prop = {'size': SIZE_LEGEND})
	SAVE_GRAPHIC(NAME, EXT, DPI)

# PLOTAGEM 4: BOXPLOT + HISTOGRAMA
def META_PLOT_004(DATASET, PLOT_SETUP):
    """
    OF or Fitness - Boxplot + histogram 

    Input:  
    DATASET: META Optimization toolbox results (Python dictionary)
    PLOT_SETUP: Chart setup
    
    Output:
    The image is saved in the current directory 
    """
    # Start reserved space for repetitions
    MINVALUES = []
    # Checking which is the best process 
    N_REP = DATASET['NUMBER OF REPETITIONS']
    TYPE = DATASET['DATA TYPE']
    BEST_REP = DATASET['DATASET']
    N_ITER = np.shape(BEST_REP[0]['OF'])
    LAST = N_ITER[0] - 1
    for I_COUNT in range(N_REP):
        ID = I_COUNT
        if TYPE == 'OF':
            X = BEST_REP[ID]['OF'][LAST]
        else:
            X = BEST_REP[ID]['FIT'][LAST]
        MINVALUES.append(X)
    NAME = PLOT_SETUP['NAME']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']     
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    CHART_COLOR = PLOT_SETUP['CHART COLOR']
    BINS = PLOT_SETUP['BINS']
    KDE = PLOT_SETUP['KDE']
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    sns.set(style = 'ticks')
    # Convert units of size figure
    [W, H] = CONVERT_SI_TO_INCHES(W, H)
    # Plot
    FIG, (AX_BOX, AX_HIST) = plt.subplots(2, figsize = (W, H), sharex = True, gridspec_kw = {'height_ratios': (.15, .85)})
    sns.boxplot(MINVALUES, ax = AX_BOX, color = CHART_COLOR)
    sns.histplot(MINVALUES, ax = AX_HIST, kde = KDE, color = CHART_COLOR, bins = BINS)
    AX_BOX.set(yticks = [])
    AX_BOX.set(xlabel='')
    font = {'fontname': 'Arial',
            'color':  LABELS_COLOR,
            'weight': 'normal',
            'size': LABELS_SIZE}
    AX_HIST.set_xlabel(X_AXIS_LABEL, fontdict = font)
    AX_HIST.set_ylabel('$COUNT$', fontdict = font)
    AX_HIST.tick_params(axis= 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
    AX_HIST.tick_params(axis= 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    sns.despine(ax = AX_HIST)
    sns.despine(ax = AX_BOX, left = True)
    SAVE_GRAPHIC(NAME, EXT, DPI)