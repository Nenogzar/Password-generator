"""
Usage:
  generate-password [-u] [-m] [-n] [-s] [-l <length>] [-c] [options]

Options:
  -u, --no-uppercase             Exclude uppercase letters. (default: false)
  -m, --no-minuscule             Exclude miniscule/lowercase letters. (default: false)
  --no-lowercase                 Another name for -m or --no-minuscule. (default: false)
  --no-miniscule                 Common typo for --no-minuscule. (default: false)
  -n, --no-numbers               Exclude numbers. (default: false)
  -s, --no-symbols               Exclude special symbols. (default: false)
  -l <length>, --len <length>    Password length (default: 8).
  -c, --dont-copy                Don't copy the password to the clipboard. (default: false)
  -h, --help                     Show this help message and exit.
"""

import random
import string
import pyperclip
from docopt import docopt
# from icecream import ic


def generatePassword(
        uppercase=True, lowercase=True, numbers=True, symbols=False, length=8):
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

    # ic(alphabet)
    # ic(password)

    remainingLength = length - len(password)
    if remainingLength <= 0:
        return password

    password += ''.join(random.choice(alphabet) for _ in range(remainingLength))
    password = ''.join(random.sample(password, len(password)))  # shuffle
    # ic(password)
    return password


if __name__ == '__main__':
    args = docopt(__doc__)

    uppercase = not args['--no-uppercase']
    lowercase = not any(
        args[k] for k in ['--no-lowercase', '--no-minuscule', '--no-miniscule'])
    numbers = not args['--no-numbers']
    symbols = not args['--no-symbols']
    length = int(args.get('--len') or 8)
    copyToClipboard = not args['--dont-copy']

    # ic(uppercase, lowercase, numbers, symbols, length)



    password = generatePassword(uppercase, lowercase, numbers, symbols, length)
    print(password)

    if copyToClipboard:
        pyperclip.copy(password)