from vmdwritefunctions import*
from fbxshapefunctions import*
import argparse

# Setup argument parser
parser = argparse.ArgumentParser()
parser.add_argument("fbxfilepath", help="Path to the fbx")
parser.add_argument("meshname", help="name of mesh contains shape animation")
args = parser.parse_args()

# Configure sdk manager
lSdkManager = FbxManager.Create()
ios = FbxIOSettings.Create(lSdkManager, "IOSRoot") # IOSROOT
lSdkManager.SetIOSettings(ios)

# Create an importer
lImporter = FbxImporter.Create(lSdkManager, "")
if lImporter.Initialize(args.fbxfilepath, -1, lSdkManager.GetIOSettings()):
    print("The scene imported successfully.")
    print("~ wait until output finishes ~")
else:
    print("Failed to import the scene:")
    print(lImporter.GetStatus().GetErrorString())

# Import file contents to the scene container
lScene = FbxScene.Create(lSdkManager, "New Scene")
lImporter.Import(lScene)

# Get Animation Components
lAnimStack = lScene.GetCurrentAnimationStack()
lAnimLayer = lAnimStack.GetMember(0)

# Get All mesh in the Scene
targetmesh = None
for i in range(lScene.GetRootNode().GetChildCount()):
    child = lScene.GetRootNode().GetChild(i)
    if child.GetName() == args.meshname:
        targetmesh = child.GetNodeAttribute()

# Write to VMD file
with open("converted.vmd", "wb") as result:
    # Header
    header = VMD_HEADER("Vocaloid Motion Data 0002", "Some model")
    writeheader(result, header)
    
    # Motion Data Count
    motioncount = VMD_MOTION_COUNT(0)
    writemotioncount(result, motioncount)
     
    # Skin
    if not HasBlendShape(targetmesh)[0]:
        writeskincount(result, VMD_SKIN_COUNT(0))
    else:
        blendshapeindex = HasBlendShape(targetmesh)[1]
        shapelist = list()
        shapecurves = list()
        animationcount = 0
        for i in range(targetmesh.GetShapeCount()):
            curve = targetmesh.GetShapeChannel(blendshapeindex, i, lAnimLayer)
            if curve:
                animationcount += curve.KeyGetCount()
                shapecurves.append(curve)
                shapelist.append(targetmesh.GetShape(blendshapeindex, i, 0))

        # Skin Data Count
        writemotioncount(result, VMD_MOTION_COUNT(animationcount))

        # SKin Data
        for i in range(len(shapecurves)):
            curve = shapecurves[i]
            if curve:
                KeyIndex = 0
                for j in range(curve.KeyGetCount()):
                    shape = shapelist[i].GetName()
                    frame = curve.KeyGetTime(j).GetFrameCount()
                    value = curve.KeyGetValue(j)
                    writeskin(
                        result,
                        VMD_SKIN(shape, frame, value/100.0)
                    )
        '''
        sorted_data = sorted(data, key=lambda x: x[1])
        for item in sorted_data:
            writeskin(
                result,
                VMD_SKIN(item[0], item[1], item[2])
            )
        '''
    
    # Camera Data Count
    cameracount = VMD_CAMERA_COUNT(0)
    writecameracount(result, cameracount)

    # Light Data Count
    lightcount = VMD_LIGHT_COUNT(0)
    writelightcount(result, lightcount)

    # Self Shadow Data Count
    selfshadowcount = VMD_SELF_SHADOW_COUNT(0)
    writeselfshadowcount(result, selfshadowcount)


print("The vmd file was written successfully.")

# Cleanup
lImporter.Destroy()
lSdkManager.Destroy()