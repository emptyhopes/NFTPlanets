import bpy
import random

# Rotation

PLANET_ROTATION_X = random.uniform(0.000000, 6.283185)
PLANET_ROTATION_Y = random.uniform(0.000000, 6.283185)
PLANET_ROTATION_Z = random.uniform(0.000000, 6.283185)

CLOUD_ROTATION_X = random.uniform(0.000000, 6.283185)
CLOUD_ROTATION_Y = random.uniform(0.000000, 6.283185)
CLOUD_ROTATION_Z = random.uniform(0.000000, 6.283185)

LIGHT_ROTATION_X = random.uniform(0.200000, 0.600000)
LIGHT_ROTATION_Y = random.uniform(1.500000, 1.800000)
LIGHT_ROTATION_Z = random.uniform(0.000000, 0.100000)

# Materials planet

# Dirty random position
MAPPING_000_X = random.uniform(1, 10000)
MAPPING_000_Y = random.uniform(1, 10000)
MAPPING_000_Z = random.uniform(1, 10000)

# Desert random position
MAPPING_001_X = random.uniform(1, 10000)
MAPPING_001_Y = random.uniform(1, 10000)
MAPPING_001_Z = random.uniform(1, 10000)

# Oceans random position
MAPPING_002_X = random.uniform(1, 10000)
MAPPING_002_Y = random.uniform(1, 10000)
MAPPING_002_Z = random.uniform(1, 10000)

# Grass and dirty

NOISETEXTURE_000_SCALE = random.uniform(2.5, 10)

COLORRAMP_000_POSITION_0_R = 0.000
COLORRAMP_000_POSITION_0_G = random.uniform(0.005, 0.030)
COLORRAMP_000_POSITION_0_B = 0.000

COLORRAMP_000_POSITION_1_R = random.uniform(0.000, 0.020)
COLORRAMP_000_POSITION_1_G = 0.020
COLORRAMP_000_POSITION_1_B = 0.000

COLORRAMP_000_POSITION_2_R = 0.070
COLORRAMP_000_POSITION_2_G = random.uniform(0.030, 0.060)
COLORRAMP_000_POSITION_2_B = 0.020

COLORRAMP_000_POSITION_3_R = random.uniform(0.150, 0.300)
COLORRAMP_000_POSITION_3_G = 0.140
COLORRAMP_000_POSITION_3_B = 0.070

COLORRAMP_001_POSITION_0_R = random.uniform(0.150, 0.300)
COLORRAMP_001_POSITION_0_G = 0.200
COLORRAMP_001_POSITION_0_B = 0.050

COLORRAMP_001_POSITION_1_R = random.uniform(0.150, 0.500)
COLORRAMP_001_POSITION_1_G = 0.250
COLORRAMP_001_POSITION_1_B = 0.120

# Desert

NOISETEXTURE_002_SCALE = random.uniform(2.5, 10)

COLORRAMP_002_POSITION_0_R = 1
COLORRAMP_002_POSITION_0_G = random.uniform(0.700, 1.000)
COLORRAMP_002_POSITION_0_B = 0.300

COLORRAMP_002_POSITION_1_R = random.uniform(0.500, 0.700)
COLORRAMP_002_POSITION_1_G = 0.300
COLORRAMP_002_POSITION_1_B = 0.100

NOISETEXTURE_003_SCALE = random.uniform(2.5, 10)

# Reliefs

NOISETEXTURE_005_SCALE = random.uniform(1, 2.5)

# Oceans

COLORRAMP_005_POSITION_0_R = 0.000
COLORRAMP_005_POSITION_0_G = 0.000
COLORRAMP_005_POSITION_0_B = 1.000

COLORRAMP_005_POSITION_1_R = 0.000
COLORRAMP_005_POSITION_1_G = random.uniform(0.000, 0.020)
COLORRAMP_005_POSITION_1_B = 1.000

COLORRAMP_005_POSITION_2_R = 0.000
COLORRAMP_005_POSITION_2_G = 0.050
COLORRAMP_005_POSITION_2_B = 1.000

COLORRAMP_005_POSITION_3_R = 0.080
COLORRAMP_005_POSITION_3_G = random.uniform(0.200, 0.300)
COLORRAMP_005_POSITION_3_B = 1.000

COLORRAMP_005_POSITION_4_R = 0.070
COLORRAMP_005_POSITION_4_G = random.uniform(0.300, 0.500)
COLORRAMP_005_POSITION_4_B = 0.500

COLORRAMP_005_POSITION_5_R = 0.040
COLORRAMP_005_POSITION_5_G = random.uniform(0.100, 0.200)
COLORRAMP_005_POSITION_5_B = 0.400

class Clear:

    def __main__():
        Clear.Clear()

    def Clear():
        for collection in bpy.data.collections:

            for object in collection.objects:
                bpy.data.objects.remove(object, do_unlink=True)
                
            bpy.data.collections.remove(collection)

        for object in bpy.data.objects:
            bpy.data.objects.remove(object, do_unlink=True)

class Settings:

    def __main__():
        Settings.Settings()

    def Settings():
        for area in bpy.context.screen.areas:
            if area.type == "VIEW_3D":
                for space in area.spaces:
                    space.shading.type = "RENDERED"
                    

class Planet:

    PlanetPositionX = 0
    PlanetPositionY = 0
    PlanetPositionZ = 0

    PlanetRotationX = PLANET_ROTATION_X
    PlanetRotationY = PLANET_ROTATION_Y
    PlanetRotationZ = PLANET_ROTATION_Z
    
    PlanetScaleX = 1
    PlanetScaleY = 1
    PlanetScaleZ = 1

    def __main__():
        Planet.Create()
        Planet.Settings()
        Planet.Materials()
    
    def Create():
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=8, 
            radius =  1, 
            enter_editmode=False, 
            align="WORLD", 
            location=(Planet.PlanetPositionX, Planet.PlanetPositionY, Planet.PlanetPositionZ), 
            rotation=(Planet.PlanetRotationX, Planet.PlanetRotationY, Planet.PlanetRotationZ), 
            scale=(Planet.PlanetScaleX, Planet.PlanetScaleY, Planet.PlanetScaleZ)
        )

    def Settings():
        object = bpy.data.objects["Icosphere"]
        object.name = "Planet"

    def Materials(): 
        Materials.Earth()
    

class Materials:

    def Earth():

        # Base material
        Material = bpy.data.materials.new(name = "Earth")

        # Settings base material
        Material.use_nodes = True

        # Nodes
        Nodes = Material.node_tree.nodes

        # Links
        Links = Material.node_tree.links

        # Principled
        PrincipledBSDF000 = Nodes.get("Principled BSDF")

        PrincipledBSDF000.location[0] = 0
        PrincipledBSDF000.location[1] = 0

        PrincipledBSDF000.inputs[9].default_value = 0.7

        # Material output
        MaterialOutput = Nodes.get("Material Output")

        MaterialOutput.location[0] = 1000
        MaterialOutput.location[1] = 0

        # Land

        # Grass and dirty

        # Grass and dirty color

        TextureCoordinate000 = Nodes.new(type = "ShaderNodeTexCoord")

        TextureCoordinate000.location[0] = -2000
        TextureCoordinate000.location[1] = 1500

        Mapping000 = Nodes.new(type = "ShaderNodeMapping")

        Mapping000.location[0] = -1750
        Mapping000.location[1] = 1500

        Mapping000.inputs[1].default_value[0] = MAPPING_000_X
        Mapping000.inputs[1].default_value[1] = MAPPING_000_Y
        Mapping000.inputs[1].default_value[2] = MAPPING_000_Z

        NoiseTexture000 = Nodes.new(type = "ShaderNodeTexNoise")

        NoiseTexture000.location[0] = -1500
        NoiseTexture000.location[1] = 1500

        NoiseTexture000.inputs[2].default_value = NOISETEXTURE_000_SCALE
        NoiseTexture000.inputs[3].default_value = 20
        NoiseTexture000.inputs[4].default_value = 0.700
        NoiseTexture000.inputs[5].default_value = 0.000

        ColorRamp000 = Nodes.new(type = "ShaderNodeValToRGB")

        ColorRamp000.location[0] = -1250
        ColorRamp000.location[1] = 1500

        ColorRamp000.color_ramp.elements[0].position = (0.400)
        ColorRamp000.color_ramp.elements[0].color = (COLORRAMP_000_POSITION_0_R, COLORRAMP_000_POSITION_0_G, COLORRAMP_000_POSITION_0_B, 1)

        ColorRamp000.color_ramp.elements.new(0.450)
        ColorRamp000.color_ramp.elements[1].color = (COLORRAMP_000_POSITION_1_R, COLORRAMP_000_POSITION_1_G, COLORRAMP_000_POSITION_1_B, 1)

        ColorRamp000.color_ramp.elements.new(0.550)
        ColorRamp000.color_ramp.elements[2].color = (COLORRAMP_000_POSITION_2_R, COLORRAMP_000_POSITION_2_G, COLORRAMP_000_POSITION_2_B, 1)

        ColorRamp000.color_ramp.elements[3].position = (0.600)
        ColorRamp000.color_ramp.elements[3].color = (COLORRAMP_000_POSITION_3_R, COLORRAMP_000_POSITION_3_G, COLORRAMP_000_POSITION_3_B, 1)

        # Grass and dirty detalization

        # Grass and dirty detalization color

        TextureCoordinate001 = Nodes.new(type = "ShaderNodeTexCoord")

        TextureCoordinate001.location[0] = -2000
        TextureCoordinate001.location[1] = 1000

        NoiseTexture001 = Nodes.new(type = "ShaderNodeTexNoise")

        NoiseTexture001.location[0] = -1750
        NoiseTexture001.location[1] = 1000

        NoiseTexture001.inputs[2].default_value = 5
        NoiseTexture001.inputs[3].default_value = 20
        NoiseTexture001.inputs[4].default_value = 0.700
        NoiseTexture001.inputs[5].default_value = 0.000

        VoronoiTexture000 = Nodes.new(type = "ShaderNodeTexVoronoi")

        VoronoiTexture000.location[0] = -1500
        VoronoiTexture000.location[1] = 1000

        VoronoiTexture000.feature = "DISTANCE_TO_EDGE"

        VoronoiTexture000.inputs[2].default_value = 50

        ColorRamp001 = Nodes.new(type = "ShaderNodeValToRGB")

        ColorRamp001.location[0] = -1250
        ColorRamp001.location[1] = 1000

        ColorRamp001.color_ramp.elements[0].color = (COLORRAMP_001_POSITION_0_R, COLORRAMP_001_POSITION_0_G, COLORRAMP_001_POSITION_0_B, 1)

        ColorRamp001.color_ramp.elements[1].position = (0.300)
        ColorRamp001.color_ramp.elements[1].color = (COLORRAMP_001_POSITION_1_R, COLORRAMP_001_POSITION_1_G, COLORRAMP_001_POSITION_1_B, 1)

        # Mix color grass, dirty and detalization

        MixRGB000 = Nodes.new(type = "ShaderNodeMixRGB")
        
        MixRGB000.location[0] = -750
        MixRGB000.location[1] = 0

        MixRGB000.inputs[0].default_value = 0.700

        # Desert

        # Desert color

        TextureCoordinate002 = Nodes.new(type = "ShaderNodeTexCoord")

        TextureCoordinate002.location[0] = -2000
        TextureCoordinate002.location[1] = -500

        NoiseTexture002 = Nodes.new(type = "ShaderNodeTexNoise")

        NoiseTexture002.location[0] = -1500
        NoiseTexture002.location[1] = -500

        NoiseTexture002.inputs[2].default_value = NOISETEXTURE_002_SCALE
        NoiseTexture002.inputs[3].default_value = 20
        NoiseTexture002.inputs[4].default_value = 0.700
        NoiseTexture002.inputs[5].default_value = 0.000

        ColorRamp002 = Nodes.new(type = "ShaderNodeValToRGB")

        ColorRamp002.location[0] = -1250
        ColorRamp002.location[1] = -500

        ColorRamp002.color_ramp.elements[0].position = (0.400)
        ColorRamp002.color_ramp.elements[0].color = (COLORRAMP_002_POSITION_0_R, COLORRAMP_002_POSITION_0_G, COLORRAMP_002_POSITION_0_B, 1)

        ColorRamp002.color_ramp.elements[1].position = (0.600)
        ColorRamp002.color_ramp.elements[1].color = (COLORRAMP_002_POSITION_1_R, COLORRAMP_002_POSITION_1_G, COLORRAMP_002_POSITION_1_B, 1)

        # Desert rarity

        TextureCoordinate003 = Nodes.new(type = "ShaderNodeTexCoord")

        TextureCoordinate003.location[0] = -2000
        TextureCoordinate003.location[1] = -1000

        Mapping001 = Nodes.new(type = "ShaderNodeMapping")

        Mapping001.location[0] = -1750
        Mapping001.location[1] = -1000

        Mapping001.inputs[1].default_value[0] = MAPPING_001_X
        Mapping001.inputs[1].default_value[1] = MAPPING_001_Y
        Mapping001.inputs[1].default_value[2] = MAPPING_001_Z

        NoiseTexture003 = Nodes.new(type = "ShaderNodeTexNoise")

        NoiseTexture003.location[0] = -1500
        NoiseTexture003.location[1] = -1000

        NoiseTexture003.inputs[2].default_value = NOISETEXTURE_003_SCALE
        NoiseTexture003.inputs[3].default_value = 20
        NoiseTexture003.inputs[4].default_value = 0.700
        NoiseTexture003.inputs[5].default_value = 0.000

        ColorRamp003 = Nodes.new(type = "ShaderNodeValToRGB")

        ColorRamp003.location[0] = -1250
        ColorRamp003.location[1] = -1000

        ColorRamp003.color_ramp.elements[0].position = (0.500)
        ColorRamp003.color_ramp.elements[0].color = (0.000, 0.000, 0.000, 1)

        ColorRamp003.color_ramp.elements[1].position = (1.000)
        ColorRamp003.color_ramp.elements[1].color = (1.000, 1.000, 1.000, 1)

        # Mix color grass, dirty, grass and dirty detalization, desert color and desert rarity

        MixRGB001 = Nodes.new(type = "ShaderNodeMixRGB")
        
        MixRGB001.location[0] = -500
        MixRGB001.location[1] = 0

        MixRGB001.blend_type = "ADD"

        # Land bumps

        TextureCoordinate004 = Nodes.new(type = "ShaderNodeTexCoord")

        TextureCoordinate004.location[0] = -2000
        TextureCoordinate004.location[1] = -1500

        NoiseTexture004 = Nodes.new(type = "ShaderNodeTexNoise")

        NoiseTexture004.location[0] = -1500
        NoiseTexture004.location[1] = -1500

        NoiseTexture004.inputs[2].default_value = 50
        NoiseTexture004.inputs[3].default_value = 20
        NoiseTexture004.inputs[4].default_value = 0.700
        NoiseTexture004.inputs[5].default_value = 0.000

        Bump000 = Nodes.new(type = "ShaderNodeBump")

        Bump000.location[0] = -1250
        Bump000.location[1] = -1500

        Bump000.inputs[0].default_value = 0.1

        # Coasts

        TextureCoordinate005 = Nodes.new(type = "ShaderNodeTexCoord")

        TextureCoordinate005.location[0] = -2000
        TextureCoordinate005.location[1] = -2000

        Mapping002 = Nodes.new(type = "ShaderNodeMapping")

        Mapping002.location[0] = -1750
        Mapping002.location[1] = -2000

        Mapping002.inputs[1].default_value[0] = MAPPING_002_X
        Mapping002.inputs[1].default_value[1] = MAPPING_002_Y
        Mapping002.inputs[1].default_value[2] = MAPPING_002_Z

        NoiseTexture005 = Nodes.new(type = "ShaderNodeTexNoise")

        NoiseTexture005.location[0] = -1500
        NoiseTexture005.location[1] = -2000

        NoiseTexture005.inputs[2].default_value = NOISETEXTURE_005_SCALE
        NoiseTexture005.inputs[3].default_value = 20
        NoiseTexture005.inputs[4].default_value = 0.700
        NoiseTexture005.inputs[5].default_value = 0.000

        ColorRamp004 = Nodes.new(type = "ShaderNodeValToRGB")

        ColorRamp004.location[0] = -1250
        ColorRamp004.location[1] = -2000

        ColorRamp004.color_ramp.elements[0].position = (0.490)
        ColorRamp004.color_ramp.elements[1].position = (0.510)

        Bump001 = Nodes.new(type = "ShaderNodeBump")

        Bump001.location[0] = -750
        Bump001.location[1] = -2000

        Bump001.inputs[0].default_value = 0.4

        # Oceans

        ColorRamp005 = Nodes.new(type = "ShaderNodeValToRGB")

        ColorRamp005.location[0] = -1250
        ColorRamp005.location[1] = -2500

        ColorRamp005.color_ramp.elements[0].position = (0.400)
        ColorRamp005.color_ramp.elements[0].color = (COLORRAMP_005_POSITION_0_R, COLORRAMP_005_POSITION_0_G, COLORRAMP_005_POSITION_0_B, 1)

        ColorRamp005.color_ramp.elements[1].position = (0.450)
        ColorRamp005.color_ramp.elements[1].color = (COLORRAMP_005_POSITION_1_R, COLORRAMP_005_POSITION_1_G, COLORRAMP_005_POSITION_1_B, 1)

        ColorRamp005.color_ramp.elements.new(0.490)
        ColorRamp005.color_ramp.elements[2].color = (COLORRAMP_005_POSITION_2_R, COLORRAMP_005_POSITION_2_G, COLORRAMP_005_POSITION_2_B, 1)

        ColorRamp005.color_ramp.elements.new(0.510)
        ColorRamp005.color_ramp.elements[3].color = (COLORRAMP_005_POSITION_3_R, COLORRAMP_005_POSITION_3_G, COLORRAMP_005_POSITION_3_B, 1)

        ColorRamp005.color_ramp.elements.new(0.550)
        ColorRamp005.color_ramp.elements[4].color = (COLORRAMP_005_POSITION_4_R, COLORRAMP_005_POSITION_4_G, COLORRAMP_005_POSITION_4_B, 1)

        ColorRamp005.color_ramp.elements.new(0.600)
        ColorRamp005.color_ramp.elements[5].color = (COLORRAMP_005_POSITION_5_R, COLORRAMP_005_POSITION_5_G, COLORRAMP_005_POSITION_5_B, 1)


        TextureCoordinate006 = Nodes.new(type = "ShaderNodeTexCoord")

        TextureCoordinate006.location[0] = -2000
        TextureCoordinate006.location[1] = -2750

        NoiseTexture006 = Nodes.new(type = "ShaderNodeTexNoise")

        NoiseTexture006.location[0] = -1500
        NoiseTexture006.location[1] = -2750

        NoiseTexture006.inputs[2].default_value = 70
        NoiseTexture006.inputs[3].default_value = 20
        NoiseTexture006.inputs[4].default_value = 0.700
        NoiseTexture006.inputs[5].default_value = 0.000

        Bump002 = Nodes.new(type = "ShaderNodeBump")

        Bump002.location[0] = -1250
        Bump002.location[1] = -2750

        Bump002.inputs[0].default_value = 0.025

        PrincipledBSDF001 = Nodes.new(type = "ShaderNodeBsdfPrincipled")

        PrincipledBSDF001.location[0] = -500
        PrincipledBSDF001.location[1] = -2500

        # Mix land and oceans

        MixShader000 = Nodes.new(type = "ShaderNodeMixShader")

        MixShader000.location[0] = 500
        MixShader000.location[1] = 0

        # Links materials

        # Grass and dirty
        Links.new(TextureCoordinate000.outputs[3], Mapping000.inputs[0])
        Links.new(Mapping000.outputs[0], NoiseTexture000.inputs[0])
        Links.new(NoiseTexture000.outputs[0], ColorRamp000.inputs[0])

        # Grass and dirty detalization
        Links.new(TextureCoordinate001.outputs[3], NoiseTexture001.inputs[0])
        Links.new(NoiseTexture001.outputs[1], VoronoiTexture000.inputs[0])
        Links.new(VoronoiTexture000.outputs[0], ColorRamp001.inputs[0])

        # Mix color grass, dirty and detalization
        Links.new(ColorRamp000.outputs[0], MixRGB000.inputs[2])
        Links.new(ColorRamp001.outputs[0], MixRGB000.inputs[1])

        # Desert

        # Desert color
        Links.new(TextureCoordinate002.outputs[3], NoiseTexture002.inputs[0])
        Links.new(NoiseTexture002.outputs[0], ColorRamp002.inputs[0])
        # Desert rarity
        Links.new(TextureCoordinate003.outputs[3], Mapping001.inputs[0])
        Links.new(Mapping001.outputs[0], NoiseTexture003.inputs[0])
        Links.new(NoiseTexture003.outputs[0], ColorRamp003.inputs[0])

        # Mix color grass, dirty and detalization
        Links.new(ColorRamp003.outputs[0], MixRGB001.inputs[0])
        Links.new(MixRGB000.outputs[0], MixRGB001.inputs[1])
        Links.new(ColorRamp002.outputs[0], MixRGB001.inputs[2])

        # Land bumps
        Links.new(TextureCoordinate004.outputs[3], NoiseTexture004.inputs[0])
        Links.new(NoiseTexture004.outputs[0], Bump000.inputs[2])

        # Coasts
        Links.new(TextureCoordinate005.outputs[3], Mapping002.inputs[0])
        Links.new(Mapping002.outputs[0], NoiseTexture005.inputs[0])
        Links.new(NoiseTexture005.outputs[0], ColorRamp004.inputs[0])
        Links.new(ColorRamp004.outputs[0], Bump001.inputs[2])

        # Oceans
        Links.new(NoiseTexture005.outputs[0], ColorRamp005.inputs[0])
        Links.new(TextureCoordinate006.outputs[3], NoiseTexture006.inputs[0])
        Links.new(NoiseTexture006.outputs[0], Bump002.inputs[2])

        # Bumps

        # Source bumps
        Links.new(Bump000.outputs[0], Bump001.inputs[3])
        # Coasts bumps
        Links.new(Bump001.outputs[0], PrincipledBSDF000.inputs[22])
        # Oceans bumps
        Links.new(Bump002.outputs[0], PrincipledBSDF001.inputs[22])

        # Output

        # Oceans
        Links.new(ColorRamp005.outputs[0], PrincipledBSDF001.inputs[0])
        # Lands
        Links.new(MixRGB001.outputs[0], PrincipledBSDF000.inputs[0])
        # Mix land and oceans
        Links.new(ColorRamp004.outputs[0], MixShader000.inputs[0])
        Links.new(PrincipledBSDF001.outputs[0], MixShader000.inputs[1])
        Links.new(PrincipledBSDF000.outputs[0], MixShader000.inputs[2])
        # Finaly output
        Links.new(MixShader000.outputs[0], MaterialOutput.inputs[0])

        # Add materials
        bpy.context.active_object.data.materials.append(Material)

class Light:

    LightPositionX = 10
    LightPositionY = 5
    LightPositionZ = 5

    LightRotationX = LIGHT_ROTATION_X
    LightRotationY = LIGHT_ROTATION_Y
    LightRotationZ = LIGHT_ROTATION_Z
    
    LightScaleX = 1
    LightScaleY = 1
    LightScaleZ = 1

    def __main__():
        Light.Create()
        Light.Settings()
        
    def Create():
        bpy.ops.object.light_add(
            type="SUN", 
            align="WORLD", 
            location=(Light.LightPositionX, Light.LightPositionY, Light.LightPositionZ), 
            rotation=(Light.LightRotationX, Light.LightRotationY, Light.LightRotationZ), 
            scale=(Light.LightScaleX, Light.LightScaleY, Light.LightScaleZ)
        )
    
    def Settings():
        bpy.context.object.data.energy = 5

class Camera:

    CameraPositionX = 0
    CameraPositionY = -5
    CameraPositionZ = 0

    CameraRotationX = 1.5708
    CameraRotationY = 0
    CameraRotationZ = 0
    
    CameraScaleX = 1
    CameraScaleY = 1
    CameraScaleZ = 1

    def __init__():
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1920

    def __main__():
        Camera.Create()
        
    def Create():
        bpy.ops.object.camera_add(
            enter_editmode=False, 
            align="VIEW", 
            location=(Camera.CameraPositionX, Camera.CameraPositionY, Camera.CameraPositionZ), 
            rotation=(Camera.CameraRotationX, Camera.CameraRotationY, Camera.CameraRotationZ), 
            scale=(Camera.CameraScaleX, Camera.CameraScaleY, Camera.CameraScaleZ)
        )

Clear.__main__()
Settings.__main__()

Camera.__init__()
Camera.__main__()

Light.__main__()

Planet.__main__()
