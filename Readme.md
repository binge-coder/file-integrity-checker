I made this python script because I wanted to be able to check the integrity of linux isos, virtual box, etc that I downloaded from the internet. This still comes in handy sometimes.

- you have a file (binary, txt, iso, etc...) whose hash this python script will calculate. the python script also helps in comparing the computed hash with the hash you have on you.
- these are the algorithms my script supports: {'sha512_224', 'sha256', 'sha3_384', 'shake_128', 'shake_256', 'ripemd160', 'sha3_512', 'sha1', 'blake2b', 'whirlpool', 'sha3_256', 'sha512', 'sha3_224', 'md5-sha1', 'mdc2', 'md5', 'sm3', 'md4', 'sha512_256', 'sha384', 'blake2s', 'sha224'}
