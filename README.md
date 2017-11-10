# Blender Batch Render

#### Put multiple .blend files in a render queue and render them in one go as a background job. It is also possible to make multiple machines render the same queue together.

### Install instructions for use on a single machine

Blender should be installed (blender.org) in the **default** location (C:\Program Files\Blender Foundation\Blender\blender.exe).
Python 3 should be installed and added to the Windows PATH, and finally Atom should be installed (atom.io).

Download *addon_batch_render_windows.py* and copy it to a folder, eg *P:/_blender_batch_render*. Look for the following line in the file  and edit it so that it points to that folder.
```python
batch_file = 'P:/_blender_batch_render/batch_render.bat'
```

Start Blender and install *add-on_batch_render_windows.py* as a Blender Add-on. A new tab called *Batch Render* should show up in the Tools region (toggled on and off with the shortcut 't'). 


### Install instructions for use on multiple machines on a network

Download *addon_batch_render_windows.py*, *zombie.py* and *start_zombie.bat* and copy them to a network folder, eg *P:/_blender_batch_render*. Look for the following line in *addon_batch_render_windows.py*  and edit it so that it points to that network folder.
```python
batch_file = 'P:/_blender_batch_render/batch_render.bat'
```

On at least one machine start Blender and install *add-on_batch_render_windows.py* as a Blender Add-on. A new tab called *Batch Render* should show up in the Tools region (toggled on and off with the shortcut 't'). 


### Use the Batch Render Add-on

The Add-on is pretty straightforward. You can add a loaded .blend file to the queue, clear the queue, open the queue in Atom and open the folder where the *.bat* and *.py* files are stored. If you double click on *batch_render.bat* Blender starts rendering all the files in the queue (in the background, i.e. the Blender UI is not opened).  
 

### Use zombie mode

When you double click on *start_zombie.py* Blender looks at the queue, i.e. *batch_render.bat* and picks the first file that has not yet been rendered. It then starts rendering that file in the background. When it is done, it picks the next file that has not been rendered. It keeps doing this until there are no more files to render. Zombie mode can be started on as many machines you like. Together they will render all the files in the queue. 


