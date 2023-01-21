import os, time
from zipfile import ZipFile

ascii_art = """
      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,    ___________________  
  \_| |`-._/||          ,'|    |                  |
    |  `-, / |         /  /    |  W E L C O M E   |
    |     || |        /  /     |       T O        |
     `r-._||/   __   /  /      |  P Y C K I N G   |
 __,-<_     )`-/  `./  /       |__________________|
'  \   `---'   \   /  /         
    |           |./  /         <-- Press any key to pack a folder into a zip. 
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()
"""

def zip_files(directory):
    with ZipFile('files.zip', 'w') as zip:
        for root, dirs, files in os.walk(directory):
            for file in files:
                zip.write(os.path.join(root, file))

def main():
    print(ascii_art)
    zipfile_name = input("| Zip name | ")
    folders = []
    creating = True
    with ZipFile(f"{zipfile_name}.zip", 'a') as archive:
        while creating:
            folder_name = input("| Folder(s) to pack (Write 'n' if none or done) | ")
            if folder_name != 'n':
                for folder_name, sub_folders, file_names in os.walk(folder_name):
                    for filename in file_names:
                        file_path = os.path.join(folder_name, filename)
                        print("█", end="")
                        archive.write(file_path, f'{folder_name}\\{filename}')
                        
                folders.append(folder_name)
                
            else: 
                creating = False

    print(f"Name: {zipfile_name}")
    folders = ' '.join(folders)
    folders = folders.replace("[", "").replace("]", "").replace("'", "")
    print(f"Folder(s): {folders}")
    ask_continue = str(input("| Confirm ? y/n | "))
    if ask_continue.lower() == 'y':
        archive.close()
        if os.path.exists(f'{zipfile_name}.zip'):
            print("ZIP file created")
        else:
            print("ZIP file not created")
    else:
        main()


    



if __name__ == "__main__":
    main()