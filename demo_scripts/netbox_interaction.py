import pynetbox # Import the python module so we can use it

nb = pynetbox.api(
    'http://192.168.0.16:32768', # Your Netbox Host URL
    token='838e37d04d68a2a3eeb3a08904b27ac1d52004b0' # Your Netbox API Token generated in the Admin view
)

devices = nb.dcim.devices.all() # Returns a list of all the devices in our Netbox instance
for device in devices: # Loops through each interaction of the list
    print(device.name) # Prints the name assigned to the device in Netbox. Our device class is handled by the pynetbox module and creates a python object to make it programmatically easier to interact with...
