# 80 cent per kilometer
pricePerKm = 0.8

# 60 cent per kilometer na 50KM
pricePerKmHighestRate = 0.6

# De prijs vanaf een x aantal kilometer
startPriceHighestRate = 15

# De max km voor het hoogste tarief
highestKMRate = 50

# De leeftijdsgroepen
lowerAgeSpecialGroup = 12
higherAgeSpecialGroup = 65

# De kortingen voor alle leeftijdsgroepen
ageDiscountSpecialGroup = 30
ageDiscountSpecialGroupWeekend = 35
ageDiscountNormalWeekend = 40

def standaardTarief(distanceInKM):
    if distanceInKM <= 0:
        return 0

    if distanceInKM <= highestKMRate:
        return distanceInKM * pricePerKm
    elif distanceInKM > highestKMRate:
        return startPriceHighestRate + (distanceInKM * pricePerKmHighestRate)

def ritPrijs(age, weekendTrip, distanceInKM):
    tripDiscount = 0
    hasAgeDiscount = age < lowerAgeSpecialGroup or age > higherAgeSpecialGroup

    if weekendTrip:
        if hasAgeDiscount:
            tripDiscount = ageDiscountSpecialGroupWeekend
        else:
            tripDiscount = ageDiscountNormalWeekend
    else:
        if hasAgeDiscount:
            tripDiscount = ageDiscountSpecialGroup

    standardPrice = standaardTarief(distanceInKM)
    return standardPrice - (standardPrice / 100 * tripDiscount)

print(ritPrijs(11, False, 12))