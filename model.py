import sqlite3

class Targets:
    def __init__(self, db):
        CRCursor = db.cursor()
        CRCursor.execute("SELECT * from crtable")

        rows = CRCursor.fetchall()
        i = 0
        self.CR = [float(grabber[0]) for grabber in rows]
        self.ProfBon = [int(grabber[1]) for grabber in rows]
        self.ACBon = [int(grabber[2]) for grabber in rows]
        self.HPLB = [int(grabber[3]) for grabber in rows]
        self.HPUB = [int(grabber[4]) for grabber in rows]
        self.AtkBon = [int(grabber[5]) for grabber in rows]
        self.DPRLB = [int(grabber[6]) for grabber in rows]
        self.DPRHB = [int(grabber[7]) for grabber in rows]
        self.SavDC = [int(grabber[8]) for grabber in rows]

    def getSet(self, CR):
        index = self.CR.index(CR)
        tempdict = {
            "targProf": self.ProfBon[index],
            "targAC": self.ACBon[index],
            "targHPLB": self.HPLB[index],
            "targHPUB": self.HPUB[index],
            "targATK": self.AtkBon[index],
            "targDPRLB": self.DPRLB[index],
            "targDPRHB": self.DPRHB[index],
            "targDC": self.SavDC[index]
        }
        return tempdict


class Creature:
    def __init__(self, db):
        self.targetCR = 0
        self.name = ""
        self.ProfBon = 0
        self.ACBon = 0
        self.HPLB = 0
        self.HPUB = 0
        self.AtkBon = 0
        self.DPRLB = 0
        self.DPRHB = 0
        self.SavDC = 0
        self.targList = Targets(db)
        self.targTable = {}

    def fetchTarget(self, chosenCR):
        self.targTable = self.targList.getSet(chosenCR)
        for x, y, in self.targTable.items():
            print(x, y)





