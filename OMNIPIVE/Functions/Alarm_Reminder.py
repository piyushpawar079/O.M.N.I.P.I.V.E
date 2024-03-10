from datetime import datetime

import re
import dateparser

from OMNIPIVE.Functions.input_output_functions import say


class AlarmTiming:

    time_regex = '(^|[^a-z])(0?[1-9])(:[0-5][0-9]){1,2}([^a-z]|$)'
    day_night_regex = '(^|[^0-9])([AP]M|[AP][.]M[.]|Noon|Midnight)([^0-9a-z]|$)'
    days_regex = '(^|[^0-9a-z])(monday|tuesday|wednesday|thursday|friday|saturday|sunday)([^0-9a-z]|$)'
    date_regex = '(^|[^0-9a-z])([0-9][0-9])([^0-9a-z]|$)'
    period_regex = '(^|[^0-9a-z])(today|yesterday|tomorrow)([^0-9a-z]|$)'

    def __init__(self, text):
        self.text = text

    @staticmethod
    def match(string, regex):
        compiled = re.compile(regex)
        result = compiled.search(string)
        if result:
            return result.group()
        else:
            return ''

    def get_expected_time(self):

        date_time_str = ''
        flag = False
        m = ['minutes', 'seconds', 'minute', 'second']
        for i in m:
            if i in self.text:
                flag = True
                new_text = self.text.split(i)[0][-3:].strip()
                now = datetime.now().strftime('%H:%M:%S')
                hour = int(str(now).split(':')[0])
                minute = int(str(now).split(':')[1])
                second = int(str(now).split(':')[2])

                if 'min' in i:
                    minute += int(new_text)
                elif 'sec' in i:
                    second += int(new_text)
                elif 'hour' in i:
                    hour += int(new_text)
                minute = str(minute)
                second = str(second)
                hour = str(hour)

                l = [hour, minute, second]
                date_time_str = ':'.join(l)

        if not flag:
            time = AlarmTiming.match(self.text, self.time_regex)
            if 'p.m.' in self.text:
                full_time = time
                time = time[:2]
                time = int(time)
                time += 12
                time = str(time) + full_time[-4:]
            date_time_str += time

            day_night = AlarmTiming.match(self.text, self.day_night_regex)
            date_time_str += day_night

            day = AlarmTiming.match(self.text, self.days_regex)
            date_time_str += day

            # date = AlarmTiming.match(self.text, self.date_regex)
            # date_time_str += date

            period = AlarmTiming.match(self.text, self.period_regex)
            date_time_str += period

        value = dateparser.parse(date_time_str)

        return value


class Alarm:

    run = True
    voice_input = ''

    def initialize(self, voice_input):
        self.voice_input = voice_input

    def check_and_alarm(self):
        new = AlarmTiming(self.voice_input).get_expected_time().strftime('%H:%M:%S')
        while self.run:
            now = datetime.now().strftime('%H:%M:%S')
            if now == new:
                say('Sir, You need to wake up now.')
                break

