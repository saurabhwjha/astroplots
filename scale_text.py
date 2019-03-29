def scale_text(scale='bigger'):
       
    size_params = plt.rcParams.find_all(pattern='labelsize')
    size_params.update(plt.rcParams.find_all(pattern='font.size'))

    for i in size_params:
        if isinstance(plt.rcParams[i],float):
            if scale=='bigger':
                plt.rcParams[i] *= 1.25
            elif scale=='smaller':
                plt.rcParams[i] *= 0.80
            elif scale=='default':
                # reset to defaults
                raise NotImplementedError("Steven will write this")
            elif isinstance(scale,(float,int)):
                plt.rcParams[i] *= scale
            else:
                raise ValueError("not recognized")


