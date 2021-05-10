import obspython as obs
from notifypy import Notify

print("Replay Buffer initialized")


# Description displayed in the Scripts dialog window
def script_description():
    return """Replay Buffer Save
  This script sends a native desktop notification when the replay buffer is saved"""


def send_notification():
  print('Sending notification...')
  notification = Notify()

  notification.title = "OBS - Script (Replay Buffer Save)"
  notification.message = "Replay buffer saved"

  notification.send()

  print('Notification sent.')