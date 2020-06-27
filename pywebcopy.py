from pywebcopy import save_website

kwargs = {'project_name': 'leilaolocalliza.com'}

save_website(
    url='http://leilaolocalliza.com/',
    project_folder='/home/ernani/paginas_salvas',
    **kwargs
)