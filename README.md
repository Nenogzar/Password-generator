# Password-generator

<img scr="https://github.com/Nenogzar/Password-generator/blob/main/gen.jpg" alt="Password" width="300">

make a strong password that will be automatically copied to the clipboard


> If you need a strong password, just run and you'll have a ready password copied to the clipboard

```Python 
Usage:
  generate-password [-u] [-m] [-n] [-s] [-l <length>] [-c] [options]

Options:
  -u, --no-uppercase             Exclude uppercase letters. (default: false)
  -m, --no-minuscule             Exclude miniscule/lowercase letters. (default: false)
  --no-lowercase                 Another name for -m or --no-minuscule. (default: false)
  --no-miniscule                 Common typo for --no-minuscule. (default: false)
  -n, --no-numbers               Exclude numbers. (default: false)
  -s, --no-symbols               Exclude special symbols. (default: false)
  -l <length>, --len <length>    Password length (default: 12).
  -c, --dont-copy                Don't copy the password to the clipboard. (default: false)
  -h, --help                     Show this help message and exit.

Examples:
  $ generate-password
  TEm{m3{;Csvm

  $ generate-password -s -l 4
  Va9U

  $ generate-password -s -l 8 -c
  BxSuSL14  # copied to the clipboard
```