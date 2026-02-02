from ij import IJ

lst = open("C:/Users/c23115040/OneDrive - Cardiff University/Desktop/AMW/July 3/list.txt", "r")
lst = lst.read()
lst = lst.split("\n")

for i in range(len(lst)):
  strng = "C:/Users/c23115040/OneDrive - Cardiff University/Desktop/AMW/July 3/" + lst[i] + ".czi"
  IJ.run("Bio-Formats Importer", "open=["+ strng +"] + autoscale color_mode=Default rois_import=[ROI manager] split_channels view=[Standard ImageJ] stack_order=Default")
  imp = IJ.selectWindow(strng +" - C=1")
  IJ.run("Subtract Background...", "rolling=50 sliding")
  IJ.saveAs(imp, "Tiff", strng[:len(strng)-4] + "_DRAQ5.tiff")
  imp = IJ.selectWindow(strng +" - C=0")
  IJ.run("Subtract Background...", "rolling=50 sliding")
  IJ.saveAs(imp, "Tiff", strng[:len(strng)-4] + "_Eosin.tiff")