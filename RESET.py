bl_info = {
    "name": "Reset Buttons",
    "author": "Demon",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "View3D ",
    "description": "A button that will allow you to copy location a reset to your choosing",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy
from bpy.types import(
        Panel,
        Operator,
        PropertyGroup,
)
from bpy.props import(
        StringProperty,
        PointerProperty,
        FloatProperty
)
class MyProperties(bpy.types.PropertyGroup): #The Propery group that display the x,y,z numbers
    
    my_string : bpy.props.StringProperty(name= "Enter Text")
    
    my_float : bpy.props.FloatVectorProperty(name= "Scale(x,y,z)", soft_min= 0, soft_max= 1000, default= (1,1,1))
    
    my_Loc : bpy.props.FloatVectorProperty(name= "Location(x,y,z)", soft_min= 0, soft_max= 1000, default= (0,0,0))
    
    my_Rot : bpy.props.FloatVectorProperty(name= "Rotation(x,y,z)", soft_min= 0, soft_max= 1000, default= (0,0,0))

class ADDONNAME_PT_main_panel(bpy.types.Panel):
    bl_label = "Reset 1.0"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
                                                 #This will tell the location panel.
        layout.prop(mytool, "my_Loc")
        layout.operator("object.1", icon="HOME",)
        layout.operator("object.4", icon="HOME")
                                                #This will display the rotation panel
        layout.prop(mytool, "my_Rot")
        layout.operator("object.2", icon="FORCE_VORTEX")
        layout.operator("object.5", icon="FORCE_VORTEX")
                                                #This will display the scale.
        layout.prop(mytool, "my_float")
        layout.operator("object.3", icon="MESH_ICOSPHERE")
        layout.operator("object.6", icon="MESH_ICOSPHERE")

class ButtonOperator1(bpy.types.Operator): #The Location Reset
    bl_idname = "object.1"
    bl_label = "Location "
    bl_options ={"REGISTER","UNDO"} 
    bl_description="This will reset the loction of the select object."
  

    def execute(self, context):
       scene = context.scene
       mytool = scene.my_tool
       
        
       bpy.context.object.location[0] = mytool.my_Loc[0]
       bpy.context.object.location[1] = mytool.my_Loc[1]
       bpy.context.object.location[2] = mytool.my_Loc[2]

       return {'FINISHED'}
   
   
    
class ButtonOperator2(bpy.types.Operator): #Rotation Reset
    bl_idname = "object.2"
    bl_label = "Rotation"
    bl_options ={"REGISTER","UNDO"} 
    bl_description="This will reset the rotation of the select object"

    def execute(self, context):
       scene = context.scene
       mytool = scene.my_tool
       
       bpy.context.object.rotation_euler[0] = mytool.my_Rot[0]
       bpy.context.object.rotation_euler[1] = mytool.my_Rot[1]
       bpy.context.object.rotation_euler[2] = mytool.my_Rot[2]

       return {'FINISHED'}

class ButtonOperator3(bpy.types.Operator):  #Scale reset
    bl_idname = "object.3"
    bl_label = "Scale"
    bl_options ={"REGISTER","UNDO"} 
    bl_description="This will reset the scale to whatever number is placed."
    
    def execute(self, context):
       scene = context.scene
       mytool = scene.my_tool
       
       #bpy.ops.transform.resize(value=(mytool.my_float[0],mytool.my_float[1], mytool.my_float[2]), orient_type='GLOBAL')
       bpy.context.object.scale[0] = mytool.my_float[0]
       bpy.context.object.scale[1] = mytool.my_float[1]
       bpy.context.object.scale[2] = mytool.my_float[2]

       return {'FINISHED'}
   
class ButtonOperator11(bpy.types.Operator): #The Location Reset
    bl_idname = "object.4"
    bl_label = "Copy Location "
    bl_options ={"REGISTER","UNDO"} 
    bl_description="This will copy the location of the selected object."
  

    def execute(self, context):
       scene = context.scene
       mytool = scene.my_tool
       
        
       mytool.my_Loc[0] =  bpy.context.object.location[0]
       mytool.my_Loc[1] =  bpy.context.object.location[1]
       mytool.my_Loc[2] =  bpy.context.object.location[2]
       

       return {'FINISHED'}

class ButtonOperator21(bpy.types.Operator): #Rotation copy
    bl_idname = "object.5"
    bl_label = "Copy Rotation"
    bl_options ={"REGISTER","UNDO"} 
    bl_description="This will copy the rotation of the selected object."

    def execute(self, context):
       scene = context.scene
       mytool = scene.my_tool
       
       mytool.my_Rot[0]=bpy.context.object.rotation_euler[0]
       mytool.my_Rot[1]=bpy.context.object.rotation_euler[1]
       mytool.my_Rot[2]=bpy.context.object.rotation_euler[2]

      
       return {'FINISHED'}

class ButtonOperator31(bpy.types.Operator): #Scale Copy
    bl_idname = "object.6"
    bl_label = "Copy Scale"
    bl_options ={"REGISTER","UNDO"} 
    bl_description="This will copy the scale of the selected object."
    
    def execute(self, context):
       scene = context.scene
       mytool = scene.my_tool
       
       #bpy.ops.transform.resize(value=(mytool.my_float[0],mytool.my_float[1], mytool.my_float[2]), orient_type='GLOBAL')
       mytool.my_float[0] = bpy.context.object.scale[0]
       mytool.my_float[1] = bpy.context.object.scale[1]
       mytool.my_float[2] = bpy.context.object.scale[2]
       

       return {'FINISHED'}

class ADDONNAME_OT_my_op(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operator"
    
    
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        
        return {'FINISHED'}
 
classes = [MyProperties, ADDONNAME_PT_main_panel, ADDONNAME_OT_my_op, ButtonOperator1, ButtonOperator2,
            ButtonOperator3, ButtonOperator11,ButtonOperator21,ButtonOperator31]
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= MyProperties)
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.my_tool
 
 
 
if __name__ == "__main__":
    register()
  

