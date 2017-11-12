# Blender Batch Render

#### Put multiple .blend files in a render queue and render them in one go as a background job. It's also possible to make multiple machines render the same queue together.

### For this to work you'll need
- [Blender](https://www.blender.org) 
- [Python 3](https://www.python.org)
- [Atom](https://atom.io)

### Install instructions for use on a single machine

Install Blender in the **default location** *(C:\Program Files\Blender Foundation\Blender\blender.exe)*. Install Atom. Download *add-on_batch_render_windows.py* and copy it to a folder. Look for the following line in the file  and edit it so that it points to that folder.
```python
batch_file = 'P:/_blender_batch_render/batch_render.bat'
```
Start Blender and install *add-on_batch_render_windows.py* as a Blender Add-on. A new tab called *Batch Render* should show up in the Tools region (toggled on and off with the shortcut 't'). 

### Install instructions for use on multiple machines on a network

Install Blender in the **default location** (C:\Program Files\Blender Foundation\Blender\blender.exe).
Install Python 3 and add it to the Windows PATH. Download *add-on_batch_render_windows.py*, *zombie.py* and *start_zombie.bat* and copy them to a network folder that can be reached by all machines. Look for the following line in *add-on_batch_render_windows.py*  and edit it so that it points to that network folder.
```python
batch_file = 'P:/_blender_batch_render/batch_render.bat'
```
On at least one machine start Blender and install *add-on_batch_render_windows.py* as a Blender Add-on. A new tab called *Batch Render* should show up in the Tools region (toggled on and off with the shortcut 't'). On this machine Atom should also be installed.

### Use a single machine to make, edit and render the queue

The Add-on is pretty straightforward. You can add .blend files to the queue, clear the queue, and edit the queue in Atom. You can't start rendering from the Add-on directly because Blender would freeze until all the files are rendered. Instead, click on *Open Folder* and then double click on *batch_render.bat*. Blender then starts rendering all the files in the queue as a background job.  

### Use multiple machines to render the queue together

navigate to the network folder with *start_zombie.bat* and double click to start rendering the queue in the background. Repeat this for as many machines as you like. Together the machines will render all the files in the queue.
