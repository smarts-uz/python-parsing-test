
import os
import shutil
from rich import print
def remove_git():
    path = input("Enter the path of your git repository: ")
    print(path)
    for root, subFolder, files in os.walk(path):
        for folder in subFolder:
            if folder == '.git':
                subfolder_path = os.path.join(root)
                git_folder_path = os.path.join(root,folder)
                print(f'[cyan]folder found: {git_folder_path}')
                shutil.rmtree(subfolder_path, ignore_errors=True)
                print(f'[red]Removed {subfolder_path}')
    print('[green]Done[/green]')
    print('[green]Done[/green]')
    input('Press Enter to continue')




if __name__ == '__main__':
    remove_git()