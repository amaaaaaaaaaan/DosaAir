import eel

# Initialize Eel
eel.init('web')

# Expose a Python function to JavaScript
@eel.expose
def get_message():
    return "Hello from Python!"

# Start the Eel application
eel.start('index.html', size=(400, 200))
