import comtypes.client
acad = comtypes.client.GetActiveObject("AutoCAD.Application")
print(acad)

