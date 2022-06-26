import os, subprocess

from helpers import color_print
from settings import Paths


def fetch_media():
    ''' fetch media from android to the local destination with adb pull '''
    color_print('იწყება გადმოტანა', 'blue')

    subprocess.run([
        Paths.ADB_SHELL_PATH, 'pull', Paths.ANDROID_TARGET_MEDIA_PATH, Paths.LOCAL_TARGET_MEDIA_PATH
        ])

    color_print('გადმოტანა დასრულებულია', 'green')


def transfer_media():
    ''' fetch media from android to the local destination with adb pull '''
    color_print('იწყება ფაილების გადატანა', 'blue')

    # Create directory if needed
    subprocess.run([
        Paths.ADB_SHELL_PATH, 'shell', 'mkdir', Paths.ANDROID_PROCESSED_MEDIA_PATH
    ])

    # Transfer media with platform dependant way
    if os.name == 'nt':
        # * wildcard not working on windows, so special Powershell command is used
        command = r"get-childitem ./Processed/ -Filter * | % {.\resources\platform-tools\adb push $_.FullName storage/self/primary/DCIM/Processed}"

        # run command in powershell
        subprocess.run(f'Powershell -Command {command}')
    else:
        # linux command
        subprocess.run(
            f'{Paths.ADB_SHELL_PATH} push {Paths.LOCAL_PROCESSED_MEDIA_PATH} {Paths.ANDROID_PROCESSED_MEDIA_PATH}', 
            shell=True
        )

    # kill adb server
    subprocess.run(f'"{Paths.ADB_SHELL_PATH}" kill-server', shell=True)

    color_print('გადატანა დასრულებულია', 'green')