import os
import shutil

project_slug = "{{ cookiecutter.project_slug }}"
base_path = os.path.join(os.getcwd())

def remove_folder(folder_path):
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)

def remove_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)


if "{{ cookiecutter.include_streamlit_config }}" != 'y':
    remove_file(os.path.join(base_path, '.streamlit', 'config.toml'))

if "{{ cookiecutter.include_streamlit_secrets }}" != 'y':
    remove_file(os.path.join(base_path, '.streamlit', '.secrets.toml'))

if "{{ cookiecutter.include_pages_folder_for_multi_page_app }}" != 'y':
    remove_folder(os.path.join(base_path, 'pages'))

if "{{ cookiecutter.include_tests }}" != 'y':
    remove_folder(os.path.join(base_path, 'tests'))

if "{{ cookiecutter.include_src_directory }}" != 'y':
    remove_folder(os.path.join(base_path, 'src'))

if __name__ == '__main__':
    print(os.path.join(base_path, '.streamlit', 'config.toml'))