from pywebcopy import Crawler, config

target_site = 'Localiza_Fake"'
target_url = 'http://leilaolocalliza.com/'
destination = '/home/ernani/paginas_salvas/'

config.setup_config(project_url= target_url,
                    project_folder=destination,
                    project_name=target_site)

crawler = Crawler()
crawler.crawl()
