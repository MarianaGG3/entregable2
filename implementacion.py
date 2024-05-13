import cv2
import pydicom
import matplotlib.pyplot as plt
import os
from pydicom.data import get_testdata_file
from pydicom import dcmread
archivo = 'archivosDCM'
arch_dicom=[]
print(os.listdir(archivo))
for n in os.listdir(archivo):
    if n.endswith('.dcm'):  
       lectura = os.path.join(archivo, n)
       dcm = pydicom.dcmread(lectura)
       arch_dicom.append(dcm)
       im = dcm.pixel_array
       plt.imshow(im)
       plt.show()