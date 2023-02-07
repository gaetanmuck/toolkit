from misc import percent, format_time, now

class Eta:
    """Object to follow execution advancement."""

    def __init__(self) -> None:
        self.begin_time = 0
        self.length = 0
        self.current_count = 0
        self.last_display_time = 0
        self.text = ''


    def begin(self, length, text) -> None:
        """Start a counter."""

        self.length = length
        self.current_count = 0
        self.text = text
        
        self.begin_time = now()

        print(self.text + ' - Elapsed: [00h00\'00] - ETA [??h??\'??] - ' + percent(0))
        self.last_display_time = self.begin_time


    def iter(self, force_print=False) -> None:
        """On an iteration."""

        self.current_count += 1
        currenttime = now()

        timeSinceLastDisplay = currenttime - self.last_display_time

        if (currenttime - timeSinceLastDisplay < 1) and not force_print: return

        time_spent = currenttime - self.begin_time
        percent_spent = self.current_count / self.length

        if(percent_spent != 0): time_left = (time_spent / percent_spent) - time_spent
        else: time_left = 0

        elapsed = format_time(time_spent)
        left = format_time(time_left)

        print('\033[1A\033[K' + self.text + f' - Elapsed: {elapsed} - ETA {left} - ' + percent(percent_spent))
        self.last_display_time = currenttime


    def end(self) -> None:
        """Finalize an ETA counting."""

        total = format_time(now() - self.begin_time)
        print('\033[1A\033[K' + self.text + f' is done - Elapsed: {total}')


    def log(self, string) -> None:
        """Print out a log, without messing with the ETA display."""

        print(string)
        self.iter(force_print=True)

