import os
cwd = os.getcwd()

def move(current, destination):
    try:
        exists = os.path.isfile(destination)
        if exists:
            os.remove(current)
        else:
            os.rename(current, destination)
    except:
        pass

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

def main():
    # init folders
    dir_names = []
    dir_names.append(os.path.join(cwd, "[Maid]-Pictures"))
    dir_names.append(os.path.join(cwd, "[Maid]-Videos"))
    dir_names.append(os.path.join(cwd, "[Maid]-Documents"))
    dir_names.append(os.path.join(cwd, "[Maid]-Compressed"))
    dir_names.append(os.path.join(cwd, "[Maid]-Programs"))
    for dir_name in dir_names:
        create_dir(dir_name)
        
    # moving files
    for filename in os.listdir(cwd):    
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".webp"):
            current = os.path.join(cwd, filename)
            destination = os.path.join(cwd, "[Maid]-Pictures", filename)
            move(current, destination)
        elif filename.endswith(".mp4") or filename.endswith(".mkv"):
            current = os.path.join(cwd, filename)
            destination = os.path.join(cwd, "[Maid]-Videos", filename)
            move(current, destination)
        elif filename.endswith(".docx") or filename.endswith(".xlsx") or filename.endswith(".dotx") or filename.endswith(".pptx") or filename.endswith(".pdf") or filename.endswith(".xls") or filename.endswith(".doc") or filename.endswith(".ppt"):
            current = os.path.join(cwd, filename)
            destination = os.path.join(cwd, "[Maid]-Documents", filename)
            move(current, destination)
        elif filename.endswith(".zip") or filename.endswith(".rar") or filename.endswith(".tgz"):
            current = os.path.join(cwd, filename)
            destination = os.path.join(cwd, "[Maid]-Compressed", filename)
            move(current, destination)
        elif filename.endswith(".exe") or filename.endswith(".msi"):
            current = os.path.join(cwd, filename)
            destination = os.path.join(cwd, "[Maid]-Programs", filename)
            move(current, destination)
    
if __name__=="__main__":
    main()
