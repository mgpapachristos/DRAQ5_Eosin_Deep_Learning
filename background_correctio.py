from ij import IJ

lst = open("C:/Users/c23115040/OneDrive - Cardiff University/Desktop/TMA Data/list.txt", "r")
lst = lst.read()
lst = lst.split("\n")
list2 = []
for i in range(len(lst)):
    if lst[i][12:15] == '0.6':
        list2.append(lst[i])
lst = list2  

for i in range(len(lst)):
  strng = "C:/Users/c23115040/OneDrive - Cardiff University/Desktop/TMA Data/" + lst[i] + ".czi"
  IJ.run("Bio-Formats Importer", "open=["+ strng +"] + autoscale color_mode=Default rois_import=[ROI manager] split_channels view=[Standard ImageJ] stack_order=Default")
  imp = IJ.selectWindow(strng +" - C=0")
  IJ.run("Subtract Background...", "rolling=50 sliding")
  #IJ.run("Subtract Background...", "rolling=50")
  IJ.saveAs(imp, "Tiff", strng[:len(strng)-4] + "_DRAQ5.tiff")
  imp = IJ.selectWindow(strng +" - C=1")
  IJ.run("Subtract Background...", "rolling=50 sliding")
  #IJ.run("Subtract Background...", "rolling=50")
  IJ.saveAs(imp, "Tiff", strng[:len(strng)-4] + "_Eosin.tiff")

  