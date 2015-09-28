try:
    import arcpy
    arcpyFound = True
except ImportError, e:
    arcpyFound = False