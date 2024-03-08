<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="background-color: #0d1117; color: white;">

# Password-generator

<div id="badges" align="center">
<img src="https://github.com/Nenogzar/Password-generator/blob/main/gen.jpg" alt="Password" height="300"  >
</div>

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
  -l <length>, --len <length>    Password length (default: 8).
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
> #### Options
> 

`-u`-> Exclude uppercase letters. Default uppercase included.<br>
`-m`->  Exclude lowercase letters. Default lowercase included.<br>
`-n`->  Exclude numbers. Default numbers included.<br>
`-s`->  Exclude special symbols. Default symbols included.<br>
`-c`->  Don't copy the password to the clipboard. Default password copied.<br>
`-l`->  Password length. Default 12.<br>

> For each character set included, at least one character from the generated password is used. For example, if executed with `-u` to exclude uppercase letters

> #### the generated password will then include at least one symbol, at least one lowercase letter and at least one number .

</body>
</html>