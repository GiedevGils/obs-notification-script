import obspython as obs
from notifypy import Notify

print("Replay Buffer With Notification initialized")

# Send a notification
def send_notification(content):
  notification = Notify()
  notification.title = "OBS Script - Replay Buffer Save"
  notification.message = content
  notification.send()


# Description displayed in the Scripts dialog window
def script_description():
    return """Replay Buffer Save
    This saves the replay buffer with a notification"""

# Listen for the callback when the registered hotkey is pressed
def save_buffer(pressed):

  if pressed:
    # Send a notification when the replay buffer is not active
    if not obs.obs_frontend_replay_buffer_active():
      send_notification('Replay buffer is not active')

    else:
      # When the replay buffer is active, and the button is pressed down
      # Save the replay buffer, and then send a notification that it has been saved
      print('Sending notification...')
      obs.obs_frontend_replay_buffer_save()
      send_notification('Replay buffer saved')
      print('Notification sent.')

# Register the hotkey on script load
def script_load(settings):
  global hotkey_id
  hotkey_id = obs.obs_hotkey_register_frontend(script_path(), "Replay Buffer With Notification", save_buffer)
  hotkey_save_array = obs.obs_data_get_array(settings, "notification_hotkey")
  obs.obs_hotkey_load(hotkey_id, hotkey_save_array)
  obs.obs_data_array_release(hotkey_save_array)

# Called before data settings are saved
def script_save(settings):
  obs.obs_save_sources()

  # Hotkey save
  hotkey_save_array = obs.obs_hotkey_save(hotkey_id)
  obs.obs_data_set_array(settings, "notification_hotkey", hotkey_save_array)
  obs.obs_data_array_release(hotkey_save_array)