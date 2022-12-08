class User:
    def __init__(self):
        self.access_token = None
        self.device_id = None
        self.account = None
        self.first_name = None
        self.last_name = None
        self.glucose_unit = None

    def set_user_default(self, access_token, device_id, account):
        self.access_token = access_token
        self.device_id = device_id
        self.account = account

    def set_user_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_user_glucose_unit(self, glucose_unit):
        self.glucose_unit = glucose_unit

    def reset_user(self):
        self.access_token = None
        self.device_id = None
        self.account = None
        self.first_name = None
        self.last_name = None
        self.glucose_unit = None


user = User()
