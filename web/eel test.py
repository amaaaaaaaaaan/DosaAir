import eel

# Initialize Eel
eel.init('public')

# Expose a Python function to JavaScript
@eel.expose
def get_message():
    return "Hello from Python!"

# Start the Eel application
eel.start('login.html', size=(400, 200) , )
