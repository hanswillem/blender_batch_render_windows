# Blender Batch Render

### Install instructions

Blender should be installed (blender.org) in the **default** location (C:\Program Files\Blender Foundation\Blender\blender.exe).
Python 3 should be installed and added to the Windows PATH, and finally Atom should be installed (atom.io).

Download all files from this repository and copy them to a network folder, eg *P:/_blender_batch_render*. Look for the following line in the file *addon_batch_render_windows.py* and edit it so that it points to that network folder.
```python
batch_file = 'P:/_blender_batch_render/batch_render.bat'
```

Start Blender and install *addon_batch_render_windows.py* as a Blender Add-on. After the Add-on is enabled a new tab called *Batch Render* should show up in the Tools region (toggled on and off with the shortcut 't'). 



### Use the Add-on

The Add-on is pretty straightforward. You can add a loaded .blend file to the queue, clear the queue, open the queue in Atom and open the folder where the *.bat* and *.py* files are stored. If you double click on *batch_render.bat* Blender starts rendering all the files in the queue (in the background, i.e. the Blender UI is not opened).  
 

### Use zombie mode

In the Add-on click on *Open Folder*
