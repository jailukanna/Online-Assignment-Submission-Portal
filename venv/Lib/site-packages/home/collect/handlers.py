from logging import getLogger

from home.ts import Session, get_series, get_device, record


class BaseHandler:

    def __init__(self):

        self.log = getLogger('home.collect.%s' % self.__class__.__name__)

    def format_packet(self, pkt):

        return " ".join("0x{0:02x}".format(x) for x in pkt)


class LoggingHandler(BaseHandler):

    def __call__(self, packet):

        self.log.warning("Ignoring packet: " % self.format_packet(packet.raw))


class RecordingHander(BaseHandler):

    def __init__(self, mapping):

        super().__init__()
        self.mapping = mapping

    def __call__(self, packet):

        session = Session()

        device = get_device(session, packet.data['packet_type'],
                            packet.data['sub_type'], packet.data['id'])

        for series_name, value_name in self.mapping.items():

            series = get_series(session, series_name)
            try:
                val = packet.data[value_name]
            except KeyError:
                self.log.error("Failed to find %s in %r" % (value_name,
                                                            packet.data))
                return

            id_ = packet.data.get('id')
            self.log.info("ID=%s, %s=%s" % (id_, series_name, val))
            record(session, series, device, val)
