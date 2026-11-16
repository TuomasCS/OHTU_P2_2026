Kokemukseni tekoälynkäytöstä.

1. Tiedosto jonka agentti loi oli .github/copilot-instructions.md
agentti generoi suhteellisen hyvän ohjetiedoston itselleen. Siinä oli vähän hassumpia osuuksia, ja pyysin agenttia muokkaamaan sitä "paremmaksi", jonka jälkeen se onnistui siinä. Tässä tuli tehtyä oma moka, koska ensin tein /init kun minulla oli koko repositorio auki, eikä vain workspace (minulla oli siis sekä workspace että koko repositorio auki, ja kun katsoin ohjeita meni alt tabattua väärälle vscode ikkunalle, mutta kun vaihdoin ns. workspaceen niin toimi paremmin.)

Agentti ei noudattanut pyyntöjä niin, kuin tahdoin. Oli hyvin hankala saada se jättämään tekemättä asioita. Piti vääntää jonkin aikaa siitä, että se oikeasti ei tekisi koko user storya kerralla. Lopulta sain sen toimimaan, mutta lähes vei hermot.

Agenttia ei tarvinnut ohjata lähes ollenkaan alun jälkeen. Toimi lähes moitteetta, ainoa hassumpi juttu oli se, että se ensin koitti lisätä kaikki dependencies jne... mutta toisella uusyrityksellä tajusi skannata projektin tietoja varten ennen kuin loi copilot-instructions.md

Testit hajosivat, kun rikoin ne tahallaan. Varsinkin "salasanan pitää matchata confirm password kohtaa", testi ei mennyt läpi kun rikoin osan koodista.

Uutta jota opin oli käytännössä se, että nää agentit on kehittyneet kyllä, siis oma muistikuva oli vähän hirveistä inline ehdotuksista aina kun koitti jotain kirjottaa, ja että chat tulee vaan tielle, mutta on kyllä kätevää kun agentilla on ns. konteksti ja projekti helposti luettavissa, jotta sitä voi jopa käyttää. 