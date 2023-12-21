from string import hexdigits
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    passports = input_data.split("\n\n")

    yield sum(map(has_required_fields, passports))
    yield sum(map(all_fields_valid, passports))


required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
optional = {"cid"}


def has_required_fields(passport: str) -> bool:
    keys = {entry.split(":")[0] for entry in passport.split()}
    return keys - optional == required


def all_fields_valid(passport: str) -> bool:
    if not has_required_fields(passport):
        return False

    fields = dict([entry.split(":") for entry in passport.split()])

    return (
        1920 <= int(fields["byr"]) <= 2002
        and 2010 <= int(fields["iyr"]) <= 2020 <= int(fields["eyr"]) <= 2030
        and (
            fields["hgt"][-2:] in ["cm", "in"]
            and (
                150 <= int(fields["hgt"][:-2]) <= 193
                if fields["hgt"].endswith("cm")
                else 59 <= int(fields["hgt"][:-2]) <= 76
            )
        )
        and (
            fields["hcl"].startswith("#")
            and all(char in hexdigits for char in fields["hcl"][1:])
        )
        and fields["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        and (fields["pid"].isnumeric() and len(fields["pid"]) == 9)
    )


run(solve)
