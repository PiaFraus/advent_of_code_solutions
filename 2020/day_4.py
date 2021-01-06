def solve(data, *args, **kwargs):
    x, result = 0, 0
    password = {}
    for line in data:
        if not line:
            try:
                assert set(password.keys()).issubset({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}), '1'
                assert set(password.keys()).issuperset({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}), '2'
                assert 1920 <= int(password.get('byr', 0)) <= 2002, 'byr'
                assert 2010 <= int(password.get('iyr', 0)) <= 2020, 'iyr'
                assert 2020 <= int(password.get('eyr', 0)) <= 2030, 'eyr'
                hgt = password.get('hgt', '0cm')
                if hgt[-2:] == 'cm':
                    assert 150 <= int(hgt[:-2]) <= 193, 'cm'
                elif hgt[-2:] == 'in':
                    assert 59 <= int(hgt[:-2]) <= 76, 'in'
                else:
                    assert False
                hcl = password.get('hcl', '#12')
                assert hcl.startswith('#'), 'hcl'
                assert len(hcl) == 7, 'hcl'
                int(hcl[1:], 16), 'hcl'
                assert password.get('ecl') in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}, 'ecl'
                assert len(password.get('pid', 0)) == 9
                int(password.get('pid', 0)), 'pid'
                result += 1
            except Exception as e:
                pass
            password = {}
            continue
        d = dict(pair.split(':') for pair in line.split(' '))
        password.update(d)
    return result

def solve_part2(data, *args, **kwargs):
    x, result = 0, 0
    password = {}
    for line in data:
        if not line:
            try:
                assert set(password.keys()).issubset({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}), '1'
                assert set(password.keys()).issuperset({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}), '2'
                assert 1920 <= int(password.get('byr', 0)) <= 2002, 'byr'
                assert 2010 <= int(password.get('iyr', 0)) <= 2020, 'iyr'
                assert 2020 <= int(password.get('eyr', 0)) <= 2030, 'eyr'
                hgt = password.get('hgt', '0cm')
                if hgt[-2:] == 'cm':
                    assert 150 <= int(hgt[:-2]) <= 193, 'cm'
                elif hgt[-2:] == 'in':
                    assert 59 <= int(hgt[:-2]) <= 76, 'in'
                else:
                    assert False
                hcl = password.get('hcl', '#12')
                assert hcl.startswith('#'), 'hcl'
                assert len(hcl) == 7, 'hcl'
                int(hcl[1:], 16), 'hcl'
                assert password.get('ecl') in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}, 'ecl'
                assert len(password.get('pid', 0)) == 9
                int(password.get('pid', 0)), 'pid'
                result += 1
            except Exception as e:
                pass
            password = {}
            continue
        d = dict(pair.split(':') for pair in line.split(' '))
        password.update(d)
    return result

test_data = '''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

with open('input/day_4.txt') as f:
    data = [line.rstrip() for line in f]
# results = solve(test_data)
results = solve(data)
print(results)


def mul(*args):
    r = 1
    for a in args:
        r *= 1
    return r
