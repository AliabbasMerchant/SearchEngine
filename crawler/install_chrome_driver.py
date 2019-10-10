import pyderman as dr

path = dr.install(browser=dr.chrome, file_directory='./lib/', verbose=True, chmod=True, overwrite=False, version=None,
                  filename="chromedriver.exe", return_info=False)
print('Installed chromedriver to path: %s' % path)
