lines = open( '/Users/DaanRaven/Desktop/Project Visualization/Alle Files voor lines/Quirrell.txt', "r")
listlines = lines.readlines()

harry = 0
hermione = 0
ron = 0
vernon = 0
petunia = 0
dudley = 0
lily = 0
james = 0
voldemort = 0
albus = 0
minerva = 0
dedalus = 0
poppy = 0
hagrid = 0
sirius = 0
marge = 0
arabella = 0
piers = 0
cornelius = 0
miranda = 0
bathilda = 0
adalbert = 0
emeric = 0
phyllida = 0
arsenus = 0
scamander = 0
quentin = 0
doris = 0
quirrell = 0
griphook = 0
malkin = 0
draco = 0
vindictus = 0
hedwig = 0
ollivander = 0
ginny = 0
molly = 0
percy = 0
fred = 0
george = 0
neville = 0
augusta = 0
lee = 0
bill = 0
charlie = 0
arthur = 0
peter = 0
cornelius_agrippa = 0
claudius = 0
grindelwald = 0
flamel = 0
crabbe = 0
goyle = 0
friar = 0
peeves = 0
abbott = 0
susan = 0
terry = 0
mandy = 0
lavender = 0
millicent = 0
justin = 0
seamus = 0
morag = 0
moon = 0
nott = 0
pansy = 0
padma = 0
parvati = 0
sally = 0
dean = 0
lisa = 0
zabini = 0
nick = 0
baron = 0
snape = 0
filch = 0
hooch = 0
fatty = 0
norris = 0
sprout = 0
binns = 0
emeric = 0
uric = 0
filius = 0
oliver = 0
helena = 0
smarmy = 0
angelina = 0
flint = 0
alicia = 0
katie = 0
bletchley = 0
adrian = 0
terence = 0
pince = 0
perenelle = 0
ronan = 0
bane = 0
firenze = 0
elfric = 0 

#Check if a name is in range of the name in question.
for i in listlines:
    j = str(i)
    if "Harry" in j or "Potter" in j:
        harry += 1
    if "Hermione" in j or "Granger" in j:
        hermione += 1
    if "Ron" in j or "Ron Weasley" in j:
        ron += 1
    if "Vernon" in j or "Mr. Dursley" in j:
        vernon += 1
    if "Petunia" in j or "Mrs. Dursley" in j:
        petunia += 1
    if "Dudley" in j:
        dudley += 1
    if "Lily" in j:
        lily += 1
    if "James" in j:
        james += 1
    if "Voldemort" in j or "You-Know-Who" in j or "Who-Must-Not-Be-Named" in j or "Master":
        voldemort += 1
    if "Albus" in j or "Dumbledore" in j:
        albus += 1
    if "Minerva" in j or "McGonagall" in j:
        minerva += 1
    if "Dedalus" in j or "Diggle" in j:
        dedalus += 1
    if "Poppy" in j or "Pomfrey" in j:
        poppy += 1
    if "Rubeus" in j or "Hagrid" in j:
        hagrid += 1
    if "Sirius" in j or "Sirius Black" in j:
        sirius += 1
    if "Marge" in j:
        marge += 1
    if "Arabella" in j or "Figg" in j:
        arabella += 1
    if "Piers" in j or "Polkiss" in j:
        piers += 1
    if "Cornelius" in j or "Fudge" in j:
        cornelius += 1
    if "Miranda" in j or "Goshawk" in j:
        miranda += 1
    if "Bathilda" in j or "Bagshot" in j:
        bathilda += 1
    if "Adalbert" in j or "Waffling" in j:
        adalbert += 1
    if "Emeric" in j or "Switch" in j:
        emeric += 1
    if "Phyllida" in j or "Spore" in j:
        phyllida += 1
    if "Arsenus" in j or "Jigger" in j:
        arsenus += 1
    if "Scamander" in j:
        scamander += 1
    if "Quentin" in j or "Trimble" in j:
        quentin += 1
    if "Doris" in j or "Crockford" in j:
        doris += 1
    if "Quirrell" in j:
        quirrell += 1
    if "Griphook" in j:
        griphook += 1
    if "Malkin" in j:
        malkin += 1
    if "Draco" in j or "Malfoy" in j:
        draco += 1
    if "Vindictus" in j or "Viridian" in j:
        vindictus += 1
    if "Hedwig" in j:
        hedwig += 1
    if "Ollivander" in j:
        ollivander += 1
    if "Ginny" in j:
        ginny += 1
    if "Molly" in j or "Mrs. Weasley" in j:
        molly += 1
    if "Percy" in j:
        percy += 1
    if "Fred" in j:
        fred += 1
    if "George" in j:
        george += 1
    if "Neville" in j or "Longbottom" in j:
        neville += 1
    if "Augusta" in j:
        augusta += 1
    if "Lee" in j or "Jordan" in j:
        lee += 1
    if "Bill" in j:
        bill += 1
    if "Charlie" in j:
        charlie += 1
    if "Arthur" in j or "Mr. Weasley" in j:
        arthur += 1
    if "Peter" in j or "Pettigrew" in j:
        peter += 1
    if "Cornelius Agrippa" in j:
        cornelius_agrippa += 1
    if "Claudius" in j:
        claudius += 1
    if "Grindelwald" in j:
        grindelwald = 0
    if "Nicolas" in j or "Flamel" in j:
        flamel += 1
    if "Vincent" in j or "Crabbe" in j:
        crabbe += 1
    if "Gregory" in j or "Goyle" in j:
        goyle += 1
    if "Fat Friar" in j:
        friar += 1
    if "Peeves" in j:
        peeves += 1
    if "Hannah" in j or "Abbott" in j:
        abbott += 1
    if "Susan" in j or "Bones" in j:
        susan += 1
    if "Terry" in j or "Boot" in j:
        terry += 1
    if "Brocklehurst" in j or "Mandy" in j:
        mandy += 1
    if "Lavender" in j:
        lavender += 1
    if "Millicent" in j or "Bulstrode" in j:
        millicent += 1
    if "Justin" in j:
        justin += 1
    if "Seamus" in j or "Finnigan" in j:
        seamus += 1
    if "Morag MacDougal" in j:
        morag += 1
    if "Lily Moon" in j:
        moon += 1
    if "Theodore Nott" in j:
        nott += 1
    if "Pansy" in j or "Parkinson" in j:
        pansy += 1
    if "Padma" in j:
        padma += 1
    if "Parvati" in j:
        parvati += 1
    if "Sally-Anne Perks" in j:
        sally += 1
    if "Dean" in j or "Thomas" in j:
        dean += 1
    if "Lisa" in j or "Turpin" in j:
        lisa += 1
    if "Blaise" in j or "Zabini" in j:
        zabini += 1
    if "Nearly-Headless Nick" in j or "Nick" in j:
        nick += 1
    if "Bloody Baron" in j:
        baron += 1
    if "Severus" in j or "Snape" in j:
        snape += 1
    if "Filch" in j or "Argus" in j:
        filch += 1
    if "Rolanda" in j or "Hooch" in j:
        hooch += 1
    if "Fat Lady" in j:
        fatty += 1
    if "Mrs Norris" in j:
        norris += 1
    if "Pomona" in j or "Sprout" in j:
        sprout += 1
    if "Cuthbert Binns" in j:
        binns += 1
    if "Emeric the Evil" in j:
        emeric += 1
    if "Uric the Oddball" in j:
        uric += 1
    if "Flitwick" in j or "Filius" in j:
        filius += 1
    if "Oliver" in j or "Wood" in j:
        oliver += 1
    if "Helena" in j or "Grey Lady" in j:
        helena += 1
    if "Gregory" in j or "Smarmy" in j:
        smarmy += 1
    if "Angelina" in j or "Johnson" in j:
        angelina += 1
    if "Marcus Flint" in j or "Flint" in j:
        flint += 1
    if "Alicia" in j or "Spinnet" in j:
        alicia += 1
    if "Katie" in j or "Bell" in j:
        katie += 1
    if "Miles" in j or "Bletchley" in j:
        bletchley += 1
    if "Adrian" in j or "Pucey" in j:
        adrian += 1
    if "Terence" in j or "Higgs" in j:
        terence += 1
    if "Irma" in j or "Pince" in j:
        pince += 1
    if "Perenelle" in j:
        perenelle += 1
    if "Ronan" in j:
        ronan += 1
    if "Bane" in j:
        bane += 1
    if "Firenze" in j:
        firenze += 1
    if "Elfric the Eager" in j:
        elfric += 1

for name, value in globals().items():
    if name != "lines" or name != "listlines":
        if type(value) is int:
            print "Quirrell, "+str(name)+", "+str(value)


