import os
import glob
import shutil # Шутил шутил, дошутился бля
import zipfile

def main(*args) -> None:
    ROOT_FOLDER: str = os.path.dirname(os.path.realpath(__file__))

    """ project_files[project][project_file] """
    
    project_files: list = list(glob.glob(f'{project}/*.als') for project in glob.glob(f'{ROOT_FOLDER}/*Project'))

    for proj in project_files:
        for file in proj:
            print(file[len(ROOT_FOLDER):])
        print('-'*79)

    #xmlify(project_files)
    print(shutil.get_unpack_formats())

    


def xmlify(prj_fls: list) -> None:
    """ Function changes actual files!! """
    raise NotImplementedError

    for proj in prj_fls:
        for file in proj:
            shutil.copy(file, file[:-3]+'zip')
            target_folder = '/'.join(file.split('/')[:-1]) + '/' # SHIT
            """
            extract_dir is the name of the target directory where the archive is unpacked. 
            If not provided, the current working directory is used.
            """
            shutil.unpack_archive(file[:-3]+'zip', target_folder)
    
    


    

if __name__ == '__main__':
    main()