# Blender Batch Render

### install instructions

Blender should be installed (blender.org) to the **default** location (C:\Program Files\Blender Foundation\Blender\blender.exe).
Python should be installed and added to the PATH. Atom should be installed (atom.io)

Download all files from this repository and copy them to a network folder. Look for the following line in the file *addon_batch_render_windows.py* so that it points to the right network folder.
```python
batch_file = 'P:/_blender_batch_render/batch_render.bat'
```
