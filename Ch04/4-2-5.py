def main():
    ## Demonstrate the passing of values.
    print("Balance:")
    print("${0:,.2f}".format(balance(1000, 5)))
    print("${0:,.2f}".format(balance(1000, 5, 0.04)))
    print("${0:,.2f}".format(balance(1000, intRate=0.04, numYears=5)))
    print("${0:,.2f}".format(balance(numYears=5, prin=1000)))
    print()
    print("${0:,.2f}".format(balance(1000, 5, 0.03)))
    print("${0:,.2f}".format(balance(1000, intRate=0.03, numYears=5)))
    print("${0:,.2f}".format(balance(intRate=0.03, numYears=5, prin=1000)))
    print("${0:,.2f}".format(balance(numYears=5, intRate=0.03, prin=1000)))


def balance(prin, numYears, intRate=0.04):
    return prin * ((1 + intRate) ** numYears)


main()
