import sys
import scipy #Location: C:\Users\ronal\AppData\Local\Programs\Python\Python313\python.exe
sys.path.append(r"C:\Users\ronal\Gotham_Web\SIMULATIONS\simulations")
sys.path.append(r"C:\Users\ronal\Gotham_Web\SIMULATIONS\Example_Data")
import treebricks as tb


gal_file = r"C:\Users\ronal\Gotham_Web\SIMULATIONS\Example_Data\sample_smoothed_cube.fr"
myGals = tb.GalaxyCatalog(gal_file)