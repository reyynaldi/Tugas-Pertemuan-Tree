class PohonBiner:
    def __init__(self,A,L,R):
        self.A = A
        self.L = L
        self.R = R
    def __repr__(self):
        return "((%s, %s, %s))" % (repr(self.A), repr(self.L), repr(self.R))
def Akar(P):
    return P.A
def Left(P):
    return P.L
def Right(P):
    return P.R
def MakePB(A,L,R):
    return PohonBiner(A,L,R)
def IsTreeEmpty(P):
    if P == MakePB(None, None, None) or P == None:
        return True
    else :
        return False
def IsOneElmtPB(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
        return True
    else :
        return False
def IsUnerLeftPB(P):
    if (not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P))):
        return True
    else :
        return False
def IsUnerRightPB(P):
    if (not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))):
        return True
    else :
        return False
def IsBinerPB(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and not IsTreeEmpty(P)):
        return True
    else :
        return False
def NbElmt(P):
    if IsTreeEmpty(P):
        return 0
    else :
        return NbElmt(Left(P)) + 1 + NbElmt(Right(P))
def NbDaunPB(P):
    if IsOneElmtPB(P):
        return 1
    elif IsBinerPB(P):
        return NbDaunPB(Left(P)) + NbDaunPB(Right(P))
    elif IsUnerLeftPB(P):
        return NbDaunPB(Left(P))
    elif IsUnerRightPB(P):
        return NbDaunPB(Right(P))

#Fungsi IsMember
def BSearchX(P, a):
    if IsOneElmtPB(P):
        return Akar(P) == a
    elif IsBinerPB(P):
        return Akar(P) == a or BSearchX(Right(P), a) or BSearchX(Left(P), a)
    elif IsUnerLeftPB(P):
        return Akar(P) == a or BSearchX(Left(P),a)
    elif IsUnerRightPB(P):
        return Akar(P) == a or BSearchX(Right(P),a)

#Fungsi Size
def TreeLevel(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmtPB(P):
        return 1
    else:
        if NbElmt(Left(P))>NbElmt(Right(P)):
            return 1+TreeLevel(Left(P))
        else:
            return 1+TreeLevel(Right(P))

#Fungsi Condong Kiri
def IsSkewLeft(P):
    if IsUnerLeftPB(P):
        if IsOneElmtPB(Left(P)):
            return True
        else:
            return IsSkewLeft(Left(P))
    else:
        return False

#Fungsi Condong Kanan
def IsSkewRight(P):
    if IsUnerRightPB(P):
        if IsOneElmtPB(Right(P)):
            return True
        else:
            return IsSkewRight(Right(P))
    else:
        return False

P = MakePB(2,MakePB(3,MakePB(1,None,None),MakePB(5, MakePB(7, None, None), None)),MakePB(4 ,MakePB(2,None,None),MakePB(4,None,None)))
P1 = MakePB(4, MakePB(9, None, None), None)
P2 = MakePB(8, None, MakePB(4, None, MakePB(5, None, None)))


#Aplikasi
print(IsSkewLeft(P2))
print(IsSkewRight(P2))
print(BSearchX(P, 10))
print(TreeLevel(P))