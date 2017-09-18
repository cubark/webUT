import subprocess

def latenza(indirizzo):

    risultato = str(subprocess.run(["ping", "-n", "1", "-l", "1", indirizzo], stdout=subprocess.PIPE))

    returncodePosizione = risultato.find('returncode=') + 11

    #se returncode=1 allora sito non raggiungibile, se =0 allora sito raggiungibile

    if (risultato[returncodePosizione]) == 0:
        pos = (risultato.find('durata')) + 7
        test = risultato[pos:(pos+20)].split()
        return test[0];
    else:
        print(indirizzo, "non raggiungibile")
        return;