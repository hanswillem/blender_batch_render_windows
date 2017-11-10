# Blender Batch Render

#### Put multiple .blend files in a render queue and render them in one go as a background job. It is also possible to make multiple machines render the same queue together.

### Install instructions for use on a single machine

Install Blender (blender.org) in the **default** location (C:\Program Files\Blender Foundation\Blender\blender.exe). Install Atom (atom.io). Download *addon_batch_render_windows.py* and copy it to a folder, eg *P:/_blender_batch_render*. Look for the following line in the file  and edit it so that it points to that folder.
```python
batch_file = 'P:/_blender_batch_render/batch_render.bat'
```
Start Blender and install *add-on_batch_render_windows.py* as a Blender Add-on. A new tab called *Batch Render* should show up in the Tools region (toggled on and off with the shortcut 't'). 


### Install instructions for use on multiple machines on a network

Install Blender (blender.org) in the **default** location (C:\Program Files\Blender Foundation\Blender\blender.exe).
Install Python 3 and add it to the Windows PATH. Download *addon_batch_render_windows.py*, *zombie.py* and *start_zombie.bat* and copy them to a network folder, eg *P:/_blender_batch_render*. Look for the following line in *addon_batch_render_windows.py*  and edit it so that it points to that network folder.
```python
batch_file = 'P:/_blender_batch_render/batch_render.bat'
```
On at least one machine start Blender and install *add-on_batch_render_windows.py* as a Blender Add-on. A new tab called *Batch Render* should show up in the Tools region (toggled on and off with the shortcut 't'). On this machine Atom (atom.io) should also be installed.

### Use a single machine to make, edit and render the queue

The Add-on is pretty straightforward. You can add .blend files to the queue, clear the queue, edit the queue in Atom and open the folder where the *.bat* and *.py* files are stored. If you double click on *batch_render.bat* Blender starts rendering all the files in the queue as a background job.  

### Use multiple machines to render the queue together

navigate to the network folder with *start_zombie.bat* and double click to start rendering the queue in the background. Repeat this for as many machines as you like. Together the machines will render all the files in the queue.
