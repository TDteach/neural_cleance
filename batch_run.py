import os

home = os.environ['HOME']
folder_root = os.path.join(home,'data/obtained_models/tf2.2-py3/GTSRB/walk_cover')
dirs = os.listdir(folder_root)

for d in dirs:
  cmmd = 'python3 gtsrb_visualize_example.py '+folder_root+' '+d+'/saved_model '+'logs/'+d
  print(cmmd)
  os.system(cmmd)


