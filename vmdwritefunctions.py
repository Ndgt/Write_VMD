# VMD formats
from vmd import (VMD_HEADER, VMD_MOTION_COUNT, VMD_MOTION, VMD_SKIN_COUNT, VMD_SKIN,
                 VMD_CAMERA_COUNT, VMD_CAMERA, VMD_LIGHT_COUNT, VMD_LIGHT,
                 VMD_SELF_SHADOW, VMD_SELF_SHADOW_COUNT)

from io import BufferedWriter
from struct import pack

# write functions
def writeheader(file: BufferedWriter, vmd_header: VMD_HEADER) -> None:
    file.write(pack("30s", vmd_header.VmdHeader.encode("shift-jis")))
    file.write(pack("20s", vmd_header.VmdModelName.encode("shift-jis")))

def writemotioncount(file: BufferedWriter, vmd_motion_count: VMD_MOTION_COUNT) -> None:
    count = vmd_motion_count.Count
    if 0 <= count <= 999999:
        file.write(pack("I", count))

def writemotion(file: BufferedWriter, vmd_motion: VMD_MOTION) -> None:
    encoded_BoneName = vmd_motion.BoneName.encode("shift-jis")
    file.write(pack("15s", encoded_BoneName))
    file.write(pack("I", vmd_motion.FrameNo))
    file.write(pack("3f", *vmd_motion.Location))
    file.write(pack("4f", *vmd_motion.Rotation))
    file.write(pack("64B", *vmd_motion.Interpolation))

def writeskincount(file: BufferedWriter, vmd_skin_count: VMD_SKIN_COUNT) -> None:
    count = vmd_skin_count.Count
    if 0 <= count <= 999999:
        file.write(pack("I", count))

def writeskin(file: BufferedWriter , vmd_skin: VMD_SKIN) -> None:
    if 0 <= vmd_skin.FrameNo <= 999999:
        encoded_string = vmd_skin.SkinName.encode("shift-jis")
        file.write(pack("15s", encoded_string))
        file.write(pack("I", vmd_skin.FrameNo))
        file.write(pack("f", vmd_skin.Weight))

def writecameracount(file: BufferedWriter, vmd_camera_count: VMD_CAMERA_COUNT) -> None:
    count = vmd_camera_count.Count
    if 0 <= count <= 999999:
        file.write(pack("I", count))

def writecamera(file: BufferedWriter, vmd_camera: VMD_CAMERA) -> None:
    file.write(pack("I", vmd_camera.FrameNo))
    file.write(pack("f", vmd_camera.Length))
    file.write(pack("3f", *vmd_camera.Location))
    file.write(pack("3f", *vmd_camera.Rotation))
    file.write(pack("24B", *vmd_camera.Interpolation))
    file.write(pack("I", vmd_camera.ViewingAngle))
    file.write(pack("B", vmd_camera.Perspective))

def writelightcount(file: BufferedWriter, vmd_light_count: VMD_LIGHT_COUNT) -> None:
    count = vmd_light_count.Count
    if 0 <= count <= 999999:
        file.write(pack("I", count))

def writelight(file: BufferedWriter, vmd_light: VMD_LIGHT) -> None:
    file.write(pack("I", vmd_light.FrameNo))
    file.write(pack("3f", *vmd_light.RGB))
    file.write(pack("3f", *vmd_light.Location))

def writeselfshadowcount(file: BufferedWriter, vmd_self_shadow_count: VMD_SELF_SHADOW_COUNT) -> None:
    count = vmd_self_shadow_count.Count
    if 0 <= count <= 999999:
        file.write(pack("I", count))

def writeselfshadow(file: BufferedWriter, vmd_self_shadow: VMD_SELF_SHADOW) -> None:
    file.write(pack("I", vmd_self_shadow.FrameNo))
    file.write(pack("B", vmd_self_shadow.Mode))
    file.write(pack("f", vmd_self_shadow.Distance))