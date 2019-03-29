import matplotlib.pyplot as plt

class astroplots:
    def __init__(self):
        self.origrcParams = plt.rcParams.copy()
    
    def scale_text(self,scale='bigger'):
        size_params = plt.rcParams.find_all(pattern='labelsize')
        size_params.update(plt.rcParams.find_all(pattern='font.size'))

        for i in size_params:
            if isinstance(plt.rcParams[i],float):
                if scale=='bigger':
                    plt.rcParams[i] *= 1.25
                elif scale=='smaller':
                    plt.rcParams[i] *= 0.80
                elif scale=='default':
                    plt.rcParams[i] = self.origrcParams[i]
                elif isinstance(scale,(float,int)):
                    plt.rcParams[i] *= scale
                else:
                    raise ValueError("not recognized")
