from contour_image import *
metalp = unpickle_phant('fixed_partial_metal_pontic_egsphant.pickle')
metald = unpickle_dose('fixed_partial_metal_pontic_3ddose.pickle')
rowp = unpickle_phant('row_teeth_egsphant.pickle')
rowd = unpickle_dose('row_teeth_3ddose.pickle')
dentp = unpickle_phant('fixed_partial_denture_egsphant.pickle')
dentd = unpickle_dose('fixed_partial_denture_3ddose.pickle')
metald.make_absolute('6MV',1000)
rowd.make_absolute('6MV',1000)
dentd.make_absolute('6MV',1000)
