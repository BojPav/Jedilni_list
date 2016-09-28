print " FastFood 'BURGER Crew' - Jedilni list"
print "...program za vnos jedi v jedilni list..."
dnevni_meni = {}

while True:

    jed = raw_input("Vnesite jed: ")
    cena_jedi = raw_input("Vnesite ceno jedi: ")
    dnevni_meni[jed] = cena_jedi
    print "Shranjeno--> " + jed + " " + str(cena_jedi)+"eur"

    dnevni_meni_file = open("menu.txt", "w+")

    vprasanje = raw_input("Ali zelite vnesti novo jed ?(Da/Ne)")
    vprasanje_low = vprasanje.lower()

    if vprasanje_low == "ne":
        print "Vnesli ste skupaj: %d jedi v menu.txt datoteko." % len(dnevni_meni)
        print dnevni_meni
        break

dnevni_meni_file.write("FastFood 'BURGER Crew' - Jedilni list: \n")  # write into the TXT file

print "Dnevni meni:"
for jed, cena_jedi in dnevni_meni.iteritems():
    print "- %s : %s"  % (jed, cena_jedi) + " eur"
    dnevni_meni_file.write("- " + jed + " : " + str(cena_jedi) + " eur" + "\n")

print "END..."
dnevni_meni_file.close()  # close the TXT file