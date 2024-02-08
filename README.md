# A Cookiecutter Streamlit Template
Welcome to my first cookiecutter template.
This cookiecutter template will create the basic structure for an organised Streamlit app.

# Project Template Structure

```
streamlit_app/
├── assets/
│ ├── css/
│ │ └── custom_style.css
│ └── images/
│ ├── logo.png
│ └── header.png
├── data/
│ ├── data1.csv
│ └── random_data_file.csv
├── output/
│ └── output.csv
├── pages/
│ ├── Page_1.py
│ └── Page_2.py
├── src/
│ ├── components/
│ │ ├── sidebar.py
│ │ └── special_graph_widget.py
│ └── calculations/
│ ├── simple_maths.py
│ └── trig_functions.py
├── tests/
│ ├── test_simple_maths.py
│ └── test_trig_functions
└── app.py
```

# Using the Template with cookiecutter
To use this template you can use the following command in your terminal:

```
cookiecutter https://github.com/andymcdgeo/cookiecutter-streamlit.git
```

You will then be presented with a series of prompts to choose which components to include in your application.

```
  [1/9] project_name (streamlit_app): andy_test
  [2/9] author_name (Andy McDonald): 
  [3/9] project_slug (andy_test): 
  [4/9] project_description (This is my awesome streamlit app.): 
  [5/9] include_streamlit_config (y): y
  [6/9] include_streamlit_secrets (y): y
  [7/9] include_pages_folder_for_multi_page_app (y): n
  [8/9] include_tests (y): n
  [9/9] include_src_directory (y): n
```

# Running the Streamlit App
