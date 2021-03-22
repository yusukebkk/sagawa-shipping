import eel
import desktop
import get_status
import file_test

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def start(path_to_excel):
    get_status.main(path_to_excel)
    return 1

@ eel.expose
def get_path():
    file_test.get_file_path()
    return 1
    
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)