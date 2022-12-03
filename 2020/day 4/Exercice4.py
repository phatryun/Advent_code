import os
import re

passport_list = []
passport = {}
nb_passport = 0
#read and construct all passport
with open('day 4/input.txt') as f:
    for line in f :
        clean_line = line.rstrip()
        if clean_line == '' :
            passport_list.append(passport)
            passport = {}
            nb_passport += 1
        else :
            fields = clean_line.split(' ')
            for field in fields :
                key, val = field.split(':')
                passport[key] = val


print(len(passport_list))
print(f'nb_passport : {nb_passport}')
print(passport_list[-1])

#part 1
cpt_valid_password = 0
for passport in passport_list :
    if (len(passport) == 8) | ((len(passport) == 7) & (not 'cid' in passport.keys())) :
        cpt_valid_password += 1

#print(cpt_valid_password)
#part 2

def checkYears(str_to_test, year_min, year_max) :
    res = True
    if bool(re.match("^\d{4}$", str_to_test)) :
        int_to_test = int(str_to_test)
        if (int_to_test < year_min) | (int_to_test > year_max) :
            res = False
    else :
        res = False
    return res

cpt_valid_password = 0
i = 0
for passport in passport_list :
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if 'byr' in passport.keys() :
        if not checkYears(passport['byr'], 1920, 2002) :
            #print('byr')
            #print(passport['byr'])
            continue
    else :
        #print('byr missing')
        continue

    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if 'iyr' in passport.keys() :
        if not checkYears(passport['iyr'], 2010, 2020) :
            #print('iyr')
            #print(passport['iyr'])
            continue
    else :
        #print('iyr missing')
        continue

    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030
    if 'eyr' in passport.keys() :
        if not checkYears(passport['eyr'], 2020, 2030) :
            #print('eyr')
            #print(passport['eyr'])
            continue
    else :
        #print('eyr missing')
        continue

    #hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76.

    if 'hgt' in passport.keys() :
        hgt = passport['hgt']
        if (hgt[-2:] == 'cm') & (hgt[:-2].isdigit()) :
            int_hgt = int(hgt[:-2])
            if (int_hgt < 150) | (int_hgt > 193) :
                #print('hgt cm')
                #print(hgt)
                continue
        elif (hgt[-2:] == 'in') & (hgt[:-2].isdigit()) :
            int_hgt = int(hgt[:-2])
            if (int_hgt < 59) | (int_hgt > 76) :
                #print('hgt in')
                #print(hgt)
                continue
        else :
            #print('hgt dont match')
            #print(hgt)
            continue
    else :
        #print('hgt missing')
        continue

    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if 'hcl' in passport.keys() :
        hcl = passport['hcl']
        if not bool(re.match("^#[0-9a-f]{6}", hcl)) :
            #print('hcl dont match')
            #print(hcl)
            continue
    else :
        #print('hcl missing')
        continue

    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
    if 'ecl' in passport.keys() :
        ecl = passport['ecl']
        if not ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] :
            #print('ecl dont match')
            #print(ecl)
            continue
    else :
        #print('ecl missing')
        continue

    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    if 'pid' in passport.keys() :
        pid = passport['pid']
        if not bool(re.match("[0-9]{9}", pid)) :
            #print('pid dont match')
            #print(pid)
            continue
    else :
        #print('pid missing')
        continue
    #cid (Country ID) - ignored, missing or not

    cpt_valid_password += 1

print(F'cpt_valid_password : {cpt_valid_password}')
