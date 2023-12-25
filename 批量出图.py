# coding:utf-8
import arcpy
mxd=arcpy.mapping.MapDocument(r"C:\Users\Administrator.DESKTOP-DLO6OMT\Desktop\1128.mxd")
for pageNum in range(1,mxd.dataDrivenPages.pageCount+1):
    mxd.dataDrivenPages.currentPageID=pageNum
    mapName=mxd.dataDrivenPages.pageRow.getValue(mxd.dataDrivenPages.pageNameField.name)
    print mapName
    arcpy.mapping.ExportToJPEG(mxd,r"C:\Users\Administrator.DESKTOP-DLO6OMT\Desktop\1129奉贤\出图2\\"+mapName+".jpg",resolution=300)
    print'ok'
