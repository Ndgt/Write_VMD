from fbx import*

def HasBlendShape(mesh: FbxMesh) -> tuple:
    result = False
    index = -1
    count = mesh.GetDeformerCount()
    if count > 0:
        for i in range(count):
            if type(mesh.GetDeformer(i)) == FbxBlendShape:
                result = True
                index = i
                break
    return (result, index)

def GetBlendShape(mesh: FbxMesh) -> FbxBlendShape:
    for i in mesh.GetDeformerCount():
        deformer = mesh.GetDeformer(i)
        if type(deformer) == FbxBlendShape:
            return deformer

def GetDeformersName(mesh: FbxMesh) -> dict:
    deformers = dict([["blendshape", ""], ["skin", ""]])
    for i in range(mesh.GetDeformerCount()):
        deformer = mesh.GetDeformer(i)
        if type(deformer) == FbxBlendShape:
            deformers["blendshape"] = deformer.GetName()
        elif type(deformer) == FbxSkin:
            deformers["skin"] = deformer.GetName()
    return deformers

def GetShapekeys(mesh: FbxMesh) -> list:
    shapelist = list()
    if HasBlendShape(mesh)[0]:
        shapecount = mesh.GetShapeCount()
        blendshapeindex = HasBlendShape(mesh)[1]
        for i in range(shapecount):
            shapelist.append(mesh.GetShape(blendshapeindex, i, 0))
    return shapelist