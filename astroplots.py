import matplotlib.pyplot as plt

class Astroplots():
    def __init__(self):
        self.orig_params = plt.rcParams.copy()
        
    def default_all(self):
        for i in plt.rcParams.keys():
            plt.rcParams[i] = self.orig_params[i]
   
    def squarefig(self,fold_on='x'):
        sizes = plt.rcParams['figure.figsize']
        if fold_on == 'x':
            plt.rcParams['figure.figsize'] = [sizes[0],sizes[0]]
        elif fold_on == 'y':
            plt.rcParams['figure.figsize'] = [sizes[1],sizes[1]]
        
    def bigger_onplot_text(self,scale):
        plt.rcParams['figure.fontsize']*=scale
        
    def scale_text(self,scale='bigger',fig_adj=False):
        if isinstance(scale,str):
            if scale=='bigger':
                scale = 1.25
            elif scale=='smaller':
                scale = 0.8
            elif scale=='default':
                plt.rcParams[i] = self.origrcParams[i]
            elif isinstance(scale,float):
                scale = scale
            elif isinstance(scale,int):
                scale=scale
            else:
                raise ValueError('input not recognized, please use scale = str(bigger), str(smaller) or a scaling value, float or int')
        
        size_params = plt.rcParams.find_all(pattern='font.size')
        size_params.update(plt.rcParams.find_all(pattern='labelsize'))
    
        fig_sizes = plt.rcParams['figure.figsize']
        
        if fig_adj:
            plt.rcParams['figure.figsize'] = [fig_sizes[0]*scale,fig_sizes[1]*scale]
        
        for i in size_params:
            plt.rcParams[i]*=scale
                
                
                
                