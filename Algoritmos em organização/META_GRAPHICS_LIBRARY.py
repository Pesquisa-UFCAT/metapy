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
	# CONVERT UNITS OF SIZE FIGURE
	W, H = CONVERT_SI_TO_INCHES(W, H)
	# PLOT
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

# PLOTAGEM 1: GRÁFICO DUPLO FO + APTIDÃO
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
	# CONVERT UNITS OF SIZE FIGURE
	W, H = CONVERT_SI_TO_INCHES(W, H)
	# PLOT
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