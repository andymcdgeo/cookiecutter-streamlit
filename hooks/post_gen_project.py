import os
import shutil

project_slug = "{{ cookiecutter.project_slug }}"
base_path = os.path.join(os.getcwd())

def remove(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)




if "{{ cookiecutter.include_streamlit_config }}" != 'y':
    remove(os.path.join(base_path, '.streamlit', 'config.toml'))

if "{{ cookiecutter.include_streamlit_secrets }}" != 'y':
    remove(os.path.join(base_path, '.streamlit', '.secrets.toml'))

if "{{ cookiecutter.include_pages_folder_for_multi_page_app }}" != 'y':
    remove(os.path.join(base_path, 'pages'))

if "{{ cookiecutter.include_tests }}" != 'y':
    remove(os.path.join(base_path, 'tests'))

if "{{ cookiecutter.include_src_directory }}" != 'y':
    remove(os.path.join(base_path, 'src'))

if __name__ == '__main__':
    print(f'Streamlit App successfully created at: {os.path.join(base_path)}')
    