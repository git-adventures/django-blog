import sys
from django.core.mail.backends.base import BaseEmailBackend


class ReadableConsoleEmailBackend(BaseEmailBackend):
    """Console email backend that outputs plain text instead of quoted-printable."""

    def __init__(self, *args, **kwargs):
        self.stream = kwargs.pop('stream', sys.stdout)
        super().__init__(*args, **kwargs)

    def send_messages(self, email_messages):
        count = 0
        for message in email_messages:
            self.stream.write('-' * 79 + '\n')
            self.stream.write(f'Subject: {message.subject}\n')
            self.stream.write(f'From: {message.from_email}\n')
            self.stream.write(f'To: {", ".join(message.to)}\n\n')
            self.stream.write(message.body)
            self.stream.write('\n' + '-' * 79 + '\n')
            self.stream.flush()
            count += 1
        return count
