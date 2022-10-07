import bpy

bl_info = {
    "name": "SameMaterialSelector",
    "author": "marvo737",
    "version": (1, 0),
    "blender": (3, 2, 0),
    "location": "",
    "description": "hoge",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": ""
}


class SameMaterialSelector(bpy.types.Operator):
    bl_idname = "object.same_material_selector"
    bl_label = "SameMaterialSelector"
    bl_description = "Same Material Selector"
    bl_options = {'REGISTER', 'UNDO'}

    def is_mesh(obj):
        obj_data = obj.data
        return isinstance(obj_data, bpy.types.Mesh)

    def get_materials_from_objects(obj):
        if not SameMaterialSelector.is_mesh(obj):
            return []
        return obj.data.materials

    def select_same_mat_objects():
        sel_objs = bpy.context.selected_objects
        if not sel_objs:
            return
        sel_mats = set()
        for obj in sel_objs:
            mats = SameMaterialSelector.get_materials_from_objects(obj)
            for mat in mats:
                sel_mats.add(mat)

        objs = bpy.data.objects
        for obj in objs:
            mats = SameMaterialSelector.get_materials_from_objects(obj)
            for mat in mats:
                if mat in sel_mats:
                    obj.select_set(True)
                    break

    def execute(self, context):
        SameMaterialSelector.select_same_mat_objects()
        print("Test Completed")
        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(SameMaterialSelector.bl_idname)


classes = [
    SameMaterialSelector,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_select_object.append(menu_fn)


def unregister():
    bpy.types.VIEW3D_MT_select_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
