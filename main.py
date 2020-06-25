from pywebcopy import save_website

project_name = 'Teste de caso'

kwargs = {'project_name': project_name}

url = 'https://pythonprodjangoernani.herokuapp.com/'

save_website(
    url = url,
    project_folder='/home/ernani/paginas_salvas',
    **kwargs
)