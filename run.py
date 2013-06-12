from provinciasapp import app

from pync import Notifier
Notifier.notify('Restarting...',open='http://localhost:8080/provincias',title='weeeee',group='restart')
try:
    import nose
    result = nose.run()
    if result:
        Notifier.notify("All dangly and awesome",title='Yay!',group='ok')
    else:
        Notifier.notify("Test didn't pass :(",activate='com.kodowa.LightTable',title='#FAIL!',group='tests')
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, app, use_reloader=True,use_debugger=True, use_evalex=True)
except Exception as e:#catch all
    Notifier.notify('Broken pipe :(',activate='com.googlecode.iterm2',title='plop',group='broken')
    #generate original exception
    print type(e)
    raise
