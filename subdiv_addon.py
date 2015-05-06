bl_info = { 
    "name": "Subdiv Panel",
    "category": "3D View"
}

import bpy

def subdiv_select():
    for o in bpy.context.selected_objects:
        if (o.type == 'MESH' and 'SUBSURF' not in (mod.type for mod in o.modifiers)):
            bpy.context.scene.objects.active = o
            bpy.ops.object.modifier_add(type='SUBSURF')
            bpy.context.object.modifiers["Subsurf"].levels = 2


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
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

 # заготовка под интовое поле для устоновки уровня сабдивайда 
    # def initSceneProperties(scn):
    #     bpy.types.Scene.MyInt = bpy.props.IntProperty(
    #         name = "Integer", 
    #         description = "Enter an integer")
    #     scn['MyInt'] = 2
    #     return

    # initSceneProperties(bpy.context.scene)
 
    def draw(self, context):
        lt = self.layout
        scn = context.scene
        lt.prop(scn, 'MyInt', icon='BLENDER', toggle=True)
        lt.operator('object.subdiv_operator')
        lt.operator('object.unsubdiv_operator')






def register():
    bpy.utils.register_class(SelectSubdive)
    bpy.utils.register_class(SelectUnsubdive)
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.register_class(SelectSubdive)
    bpy.utils.register_class(SelectUnsubdive)
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()
