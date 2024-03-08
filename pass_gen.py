import random
import string
import pyperclip
from docopt import docopt
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


def generatePassword(
        uppercase=True, lowercase=True, numbers=True, symbols=False, length=12):
    password = ''
    alphabet = ''

    if uppercase:
        alphabet += string.ascii_uppercase
        password += random.choice(string.ascii_uppercase)
    if lowercase:
        alphabet += string.ascii_lowercase
        password += random.choice(string.ascii_lowercase)
    if numbers:
        alphabet += string.digits
        password += random.choice(string.digits)
    if symbols:
        alphabet += string.punctuation
        password += random.choice(string.punctuation)

    if not alphabet:
        raise ValueError('You must enable at least one character set.')

    remainingLength = length - len(password)
    if remainingLength <= 0:
        return password

    password += ''.join(random.choice(alphabet) for _ in range(remainingLength))
    password = ''.join(random.sample(password, len(password)))  # shuffle

    return password


if __name__ == '__main__':
    args = docopt(__doc__)

    uppercase = not args['--no-uppercase']
    lowercase = not any(
        args[k] for k in ['--no-lowercase', '--no-minuscule', '--no-miniscule'])
    numbers = not args['--no-numbers']
    symbols = not args['--no-symbols']
    length = int(args.get('--len') or 12)
    copyToClipboard = not args['--dont-copy']

    password = generatePassword(uppercase, lowercase, numbers, symbols, length)
    print(password)

    if copyToClipboard:
        pyperclip.copy(password)