class TVBase(object):
    """Абстрактный телевизор"""
    def tune_channel(self, channel):
        raise NotImplementedError()


class LGTV(TVBase):
    """Телевизор LG"""
    def tune_channel(self, channel):
        print('LG TV: выбран %d канал' % channel)


class SamsungTV(TVBase):
    """Телевизор Samsung"""
    def tune_channel(self, channel):
        print('Samsung TV: выбран %d канал' % channel)


class RemoteControlBase(object):
    """Абстрактный пульт управления"""
    def __init__(self):
        self._tv = self.get_tv()

    def get_tv(self):
        raise NotImplementedError()

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    """Пульт управления"""
    def __init__(self):
        super(RemoteControl, self).__init__()
        self._channel = 0  # текущий канал

    def get_tv(self):
        return SamsungTV()

    def tune_channel(self, channel):
        super(RemoteControl, self).tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def previous_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)


remote_control = RemoteControl()
remote_control.tune_channel(3)  
remote_control.next_channel()  
