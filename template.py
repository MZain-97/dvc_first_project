import os


dirs = [

    os.path.join('data','raw'),
    os.path.join('data','processed'),
    'notebooks',
    'saved_models',
    'src'
]

for dirs_ in dirs:
    os.makedirs(dirs_,exist_ok=True)
    with open(os.path.join(dirs_,'.gitkeep') ,"w") as f:
        pass

files_ = [
    'dvc.yaml',
    'params.yaml',
    '.gitignore',
    os.path.join('src','__init__.py')
]

for file_ in files_:
    with open(file_,'w') as f:
        pass

 






