def main():
    nheac = 0.004
    mwrdc = 0.406
    pmab = 0.006
    cpd = 0.362
    bec = 3.726
    cccd = 0.169
    csbif = 0.128
    clf = 0.122
    city = 1.630
    ccfpd = 0.063
    cook = 0.316
    ccps = 0.130
    cchf = 0.087

    misc_tax = nheac + mwrdc + pmab + cpd
    school_tax = bec + cccd
    city_tax = csbif + clf + city
    cook_county_tax = ccfpd + cook + ccps + cchf

    total_tax_rate = misc_tax + school_tax + city_tax + cook_county_tax

    print('Property Tax Rate is:', total_tax_rate)
main()
def main():
    property_value = float(input('Enter value of property: '))

    local_tax_rate = float(input('Enter local tax rate: '))

    state_equalizer_rate = float(input('Enter state equalizer rate: '))

    assessed_value = property_value * 0.1  
    equalized_value = assessed_value * state_equalizer_rate
    property_tax_before = equalized_value * local_tax_rate

    homeowner_exemption = 500.43
    senior_citizen_exemption = 357.45

    total_property_tax = property_tax_before - homeowner_exemption - senior_citizen_exemption

    print('Property tax due:', total_property_tax)

if __name__ == "__main__":
    main()

