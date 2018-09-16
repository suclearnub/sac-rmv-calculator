import discord
import shlex
from modules.botModule import BotModule


class SACRMV(BotModule):
    name = 'sacrmv'

    description = 'Calculation of SAC and RMV given dive times.'

    help_text = 'Calculates SAC (Surface Air Consumption) and RMV (Respiratory Mean Volume) given dive times. \n' \
                '`!air [start_pressure BAR] [end_pressure BAR] [bottom_time MINUTE] [average_depth METRE] ' \
                '[tank_service_pressure BAR] [tank_capacity LITRE]`'

    trigger_string = 'air'

    module_version = '1.0.0'

    @staticmethod
    def is_number(li):
        for i in li:
            try:
                int(i)
            except ValueError:
                return False
        return True

    async def parse_command(self, message, client):
        msg = shlex.split(message.content)
        if len(msg) != 7:
            send_message = "[!] Missing arguments."
            await client.send_message(message.channel, send_message)
            return 0
        if not self.is_number(msg[1:]):
            send_message = "[!] Invalid arguments."
            await client.send_message(message.channel, send_message)
            return 0
        start_bar = int(msg[1])
        end_bar = int(msg[2])
        bar = start_bar-end_bar
        bottom_time = int(msg[3])

        msw = int(msg[4])

        pressure = (msw*0.099376) + 1

        sac = bar/bottom_time/pressure

        service_pressure = int(msg[5])
        tank_capacity = int(msg[6])
        rmv = (tank_capacity/service_pressure)*sac

        send_message = "SAC: " + str(sac) + " bar/min" + "\n" \
                       "RMV: " + str(rmv) + " litres/min"

        await client.send_message(message.channel, send_message)
