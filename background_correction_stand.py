from ij import IJ

lst = open("C:/Users/c23115040/OneDrive - Cardiff University/Desktop/MGP/D&E WCB CORE/list.txt", "r")
lst = lst.read()
lst = lst.split("\n")

lst2 = open("C:/Users/c23115040/OneDrive - Cardiff University/Desktop/MGP/D&E WCB CORE/list2.txt", "r")
lst2 = lst2.read()
lst2 = lst2.split("\n")

for i in range(9, 10):
  for p in range(len(lst2)):
  	if ((i > 7) & ((p == 1) | (p == 2))):
  	  continue 
  	strng = "C:/Users/c23115040/OneDrive - Cardiff University/Desktop/MGP/D&E WCB CORE/" + lst[i] + "/" + lst2[p] + ".czi"
  	IJ.run("Bio-Formats Importer", "open=["+ strng +"] + autoscale color_mode=Default rois_import=[ROI manager] split_channels view=[Standard ImageJ] stack_order=Default")
  	imp = IJ.selectWindow(strng +" - C=0")
  	if p == 0:
  	  IJ.run("Subtract Background...", "rolling=50 sliding stack")    
  	else:
  	  IJ.run("Subtract Background...", "rolling=50 sliding")
  	IJ.saveAs(imp, "Tiff", strng[:len(strng)-4] + "_Eosin.tiff")
  	imp = IJ.getImage()
  	imp.close()
  	imp = IJ.selectWindow(strng +" - C=1")
  	if p == 0:
  	  IJ.run("Subtract Background...", "rolling=50 sliding stack")
  	else:
  	  IJ.run("Subtract Background...", "rolling=50 sliding")
  	IJ.saveAs(imp, "Tiff", strng[:len(strng)-4] + "_DRAQ5.tiff")
  	imp = IJ.getImage()
  	imp.close()

    
 
 
 