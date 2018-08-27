# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# This addon is made for windows!


bl_info = {
    'name' : 'Batch Render',
    'author' : 'Hans Willem Gijzel',
    'version' : (1, 0),
    'blender' : (2, 79),
    'location' : 'View 3D > Tools > Batch Render',
    'description' : 'Batch render blend files.',
    'warning' : '',
    'wiki_url' : '',
    'category' : 'Render'
    }


#imports
import bpy
import os
from shutil import copyfile


#path to folder
batch_file = 'P:/_blender_batch_render/batch_render.bat'


#the main functions called by the operators
def main_add_to_queue(a = None):
    print('adding to queue...')
    f = open(batch_file, 'a')
    if a == None:
        render_string = '"' + bpy.app.binary_path + '" -b "' + str(bpy.data.filepath) + '" -x 1 -a' + '\n'
    else:
        render_string = '"' + bpy.app.binary_path + '" -b "' + a + '" -x 1 -a' + '\n'
    f.write(render_string)
    f.close()

    removeDuplicates()


def main_add_layers_to_queue():
    print('saving render layers as files...')
    fn = os.path.basename(bpy.data.filepath) #blendfile
    fn_ne = os.path.splitext(fn)[0] #blendfile without extension
    dr = os.path.dirname(bpy.data.filepath) #path
    outp = bpy.context.scene.render.filepath 
    #itterate through layers
    for i in bpy.context.scene.render.layers:
        for j in bpy.context.scene.render.layers:
            j.use = False;
        i.use = True
        nf = fn_ne  + '_' + i.name + '.blend' #new filename
        nf_p = os.path.join(dr, nf) #new filename  including path
        bpy.context.scene.render.filepath = outp + '[' + i.name + ']_'
        bpy.ops.wm.save_as_mainfile(filepath = nf_p, copy = True) #save a copy of the blendfile

        main_add_to_queue(nf_p)


def main_clear_queue():
    print('clearing the queue...')
    createBatchFile()


def main_open_folder():
    print('opening folder...')
    os.startfile(os.path.dirname(batch_file))


#helper functions
def getQueueLength():
    count = 0;
    f = open(batch_file, 'r')
    for i in f:
        count += 1
    f.close()
    return count


def removeDuplicates():
    f = open(batch_file, 'r')
    l = set([i for i in f])
    f.close()
    f = open(batch_file, 'w')
    for i in l:
        f.write(i)
    f.close()


def createBatchFile():
    f = open(batch_file, 'w')
    f.close()


#panel class
class MyPanel_batch_render(bpy.types.Panel):

    #panel attributes
    """Batch Render Panel Class"""
    bl_label = 'Batch Render'
    bl_idname = 'tools_my_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Batch Render'

    #draw loop
    def draw(self, context):
        layout = self.layout
        if not os.path.isfile(batch_file):
            createBatchFile()
        layout.label('In Queue: ' + str(getQueueLength()))
        col = layout.column(align = True)
        col.operator('script.operator_add_to_queue', text='Add Current File To Queue')
        col.operator('script.operator_add_layers_to_queue', text = 'Add Layers To Queue')
        col.operator('script.operator_clear_queue', text='Clear Queue')
        col.operator('script.operator_open_folder', text='Open Folder')


#operator class
class MyOperator_add_to_queue(bpy.types.Operator):

    #operator attributes
    """Add Current Blend File To The Queue"""
    bl_label = 'Add To Queue'
    bl_idname = 'script.operator_add_to_queue'
    bl_options = {'REGISTER', 'UNDO'}

    #poll - if the .blend file is not saved, the layers cannot be added to the queue
    @classmethod
    def poll(cls, context):
        return bpy.data.is_saved

    #execute
    def execute(self, context):
        main_add_to_queue()

        return {'FINISHED'}


class MyOperator_add_layers_to_queue(bpy.types.Operator):

    #operator attributes
    """Add Current Blend File To The Queue"""
    bl_label = 'Add To Queue'
    bl_idname = 'script.operator_add_layers_to_queue'
    bl_options = {'REGISTER', 'UNDO'}

    #poll - if the .blend file is not saved, it cannot be added to the queue
    @classmethod
    def poll(cls, context):
        return bpy.data.is_saved

    #execute
    def execute(self, context):
        main_add_layers_to_queue()

        return {'FINISHED'}


class MyOperator_clear_queue(bpy.types.Operator):

    #operator attributes
    """Clear The Queue"""
    bl_label = 'Clear The Queue'
    bl_idname = 'script.operator_clear_queue'
    bl_options = {'REGISTER', 'UNDO'}

    #execute
    def execute(self, context):
        main_clear_queue()

        return {'FINISHED'}


class MyOperator_open_folder(bpy.types.Operator):

    #operator attributes
    """Open the folder with the batch file"""
    bl_label = 'Open Folder'
    bl_idname = 'script.operator_open_folder'
    bl_options = {'REGISTER', 'UNDO'}

    #execute
    def execute(self, context):
        main_open_folder()

        return {'FINISHED'}


#registration
def register():
    bpy.utils.register_class(MyPanel_batch_render)
    bpy.utils.register_class(MyOperator_add_to_queue)
    bpy.utils.register_class(MyOperator_add_layers_to_queue)
    bpy.utils.register_class(MyOperator_open_folder)
    bpy.utils.register_class(MyOperator_clear_queue)


def unregister():
    bpy.utils.unregister_class(MyPanel_batch_render)
    bpy.utils.unregister_class(MyOperator_add_to_queue)
    bpy.utils.unregister_class(MyOperator_add_layers_to_queue)
    bpy.utils.unregister_class(MyOperator_open_folder)
    bpy.utils.unregister_class(MyOperator_clear_queue)


#enable to test the addon by running this script
if __name__ == '__main__':
    register()
