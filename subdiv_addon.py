bl_info = { 
    "name": "Subdiv Panel_test",
    "author": "Evgeny Starostin",
    "category": "3D View"
}

import bpy

def subdiv_select():
    num = bpy.context.object.my_global_num

    for o in bpy.context.selected_objects:
        if (o.type == 'MESH' and 'SUBSURF' not in (mod.type for mod in o.modifiers)):
            bpy.context.scene.objects.active = o
            bpy.ops.object.modifier_add(type='SUBSURF')
            bpy.context.object.modifiers["Subsurf"].levels = num

class SelectSubdive(bpy.types.Operator):
        
    bl_idname = "object.subdiv_operator"
    bl_label = "Select Subdive Operator"        

    def execute(self, context):
        subdiv_select()
        return {'FINISHED'}

def unsubdiv_select():
    for o in bpy.context.selected_objects:
        if (o.type == 'MESH' and 'SUBSURF' in (mod.type for mod in o.modifiers)):
            bpy.context.scene.objects.active = o
            bpy.context.object.modifiers["Subsurf"].levels = 0
            bpy.ops.object.modifier_remove(modifier='Subsurf')


class SelectUnsubdive(bpy.types.Operator):
    bl_idname = "object.unsubdiv_operator"
    bl_label = "Select Unsubdive Operator"

    def execute(self, context):
        unsubdiv_select()
        return {'FINISHED'}

class HelloWorldPanel(bpy.types.Panel):
    bl_label = "Subdiv Panel"
    bl_idname = "subdiv_ui"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Tools'

    def draw(self, context):
        lt = self.layout
        scn = context.scene
        obj = context.object
        # lt.prop(scn, 'MyInt', icon='BLENDER', toggle=True)
        lt.prop(obj, "my_global_num")
        lt.operator('object.subdiv_operator')
        lt.operator('object.unsubdiv_operator')

def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(SelectSubdive)
    bpy.utils.register_class(SelectUnsubdive)
    bpy.types.Object.my_global_num = bpy.props.IntProperty(
        name="Subdivision",
        description="Integer Value",
        default=1,
    )


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    # bpy.utils.register_class(SelectSubdive)
    # bpy.utils.register_class(SelectUnsubdive)

if __name__ == "__main__":
    register()