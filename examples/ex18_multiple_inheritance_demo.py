class Phone:
    def __init__(self):
        super().__init__()  # better practice
        print('Phone.__init__() called')

    def dial(self):
        print('dialing...')


class MobilePhone(Phone):
    def __init__(self):
        super().__init__()
        print('MobilePhone.__init__() called')

    def send_sms(self):
        print('sending sms...')


class Camera:
    def __init__(self):
        super().__init__()  # better practice
        print('Camera.__init__() called')

    def take_picture(self):
        print('smile please...')


class SmartPhone( MobilePhone, Camera ):
    def __init__(self):
        super().__init__()
        print('SmartPhone.__init__() called')

    def run_app(self, app_name='music'):
        print(f'running {app_name} app...')


if __name__ == '__main__':
    sp = SmartPhone()
    sp.dial()
    sp.send_sms()
    sp.run_app()
