from typing import Dict, Optional
import sys

class Passport:
    def __init__(self, byr: str, iyr: str, eyr: str, hgt: str, hcl: str, ecl: str, pid: str, cid: Optional[str] = None):
        self.byr = int(byr)
        self.iyr = int(iyr)
        self.eyr = int(eyr)
        self.hgt = int(hgt[0:-2])
        self.hgt_unit = hgt[-2:]  # cm or in
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

def validate(passport: Dict[str, str]) -> bool:
    try:
        Passport(**passport)  # try unpacking the passport dictionary
    except TypeError:
        return False
    return True

def validate_v2(passport: Dict[str, str]) -> bool:
    try:
        passport = Passport(**passport)  # try unpacking the passport dictionary
    except TypeError:
        return False

    if not 1920 <= passport.byr <= 2002:
        return False
    if not 2010 <= passport.iyr <= 2020:
        return False
    if not 2020 <= passport.eyr <= 2030:
        return False
    if passport.hgt_unit == 'cm':
        if not 150 <= passport.hgt <= 193:
            return False
    else:
        if not 59 <= passport.hgt <= 76:
            return False
    if not len(passport.hcl) == 7 or passport.hcl[0] != '#':
        return False
    else:
        hex = passport.hcl

    return True

entries = sys.stdin.read().split('\n\n')
valid = 0
for entry in entries:
    fields = entry.split()
    passport = {field[:3] : field[5:] for field in fields}
    valid += validate(passport)
print(valid)
