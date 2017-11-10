# Blender Batch Render

### install instructions

Blender should be installed (blender.org) to the **default** location (C:\Program Files\Blender Foundation\Blender\blender.exe).
Python 3 should be installed and added to the Windows PATH, and finally Atom should be installed (atom.io)

Download all files from this repository and copy them to a network folder, eg *P:/_blender_batch_render*. Look for the following line in the file *addon_batch_render_windows.py* and edit it so that it points to that network folder.
```python
batch_file = 'P:/_blender_batch_render/batch_render.bat'
```

Start Blender and install *addon_batch_render_windows.py* as a BLender addon (go to *User Preferences > Add-ons > install Add-on from file*)
