"""
######################################################################
  РџСЂРѕРіСЂР°РјРјР° РґР»СЏ СЂРµС€РµРЅРёСЏ Р·Р°РґР°С‡ С‚РёРїР° Рђ10, Р°РЅР°Р»РѕРіРёС‡РЅС‹С… РґРµРјРѕ-РІР°СЂРёР°РЅС‚Сѓ
  Р•Р“Р­ РїРѕ РёРЅС„РѕСЂРјР°С‚РёРєРµ 2013 РіРѕРґР°
  (C) Рљ.Р®. РџРѕР»СЏРєРѕРІ, 2012
  Web:    http://kpolyakov.narod.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-------------------------------------------------------
# Р”РµРјРѕ-РІР°СЂРёР°РЅС‚ Р¤РРџР
#-------------------------------------------------------
# РќРµРёР·РІРµСЃС‚РЅР°СЏ РїРµСЂРµРјРµРЅРЅР°СЏ - Рђ, РґР»СЏ РѕСЃС‚Р°Р»СЊРЅС‹С… РёРјРµРЅ РѕС‚СЂРµР·РєРѕРІ
# РґРѕР»Р¶РЅС‹ Р±С‹С‚СЊ Р·Р°РґР°РЅС‹ РЅР°С‡Р°Р»СЊРЅС‹Рµ Рё РєРѕРЅРµС‡РЅС‹Рµ РіСЂР°РЅРёС†С‹
# РІ С„РѕСЂРјРµ РєРѕСЂС‚РµР¶РµР№.
#-------------------------------------------------------
intervals = {'P': (2,10), 'Q': (6,14) }
#-------------------------------------------------------
# Р Р°Р·СЂРµС€РµРЅРЅС‹Рµ РѕРїРµСЂР°С†РёРё:
#    ! - РќР•, РѕС‚СЂРёС†Р°РЅРёРµ
#    * - Р, Р»РѕРіРёС‡РµСЃРєРѕРµ СѓРјРЅРѕР¶РµРЅРёРµ
#    + - РР›Р, Р»РѕРіРёС‡РµСЃРєРѕРµ СЃР»РѕР¶РµРЅРёРµ
#    -> РёР»Рё ^ - РёРјРїР»РёРєР°С†РёСЏ
#    = - СЌРєРІРёРІР°Р»РµРЅС‚РЅРѕСЃС‚СЊ 
#-------------------------------------------------------
expr = '(A->P)+Q'

#-------------------------------------------------------
# Р•С‰С‘ РїСЂРёРјРµСЂС‹
#-------------------------------------------------------
# РЎ РѕРїРµСЂР°С†РёРµР№ "РЅРµ РїСЂРёРЅР°РґР»РµР¶РёС‚"
#-------------------------------------------------------
#intervals = {'P': (2,20), 'Q': (15,25) }
#expr = '(!A->!P)+Q'
#-------------------------------------------------------
# Р”РІРµ РёРјРїР»РёРєР°С†РёРё
#-------------------------------------------------------
#intervals = {'P': (0,40), 'Q': (20,45), 'R': (10,50) }
#expr = '(P->Q)+(!A->!R)'
#-------------------------------------------------------
# Р’С‹СЂР°Р¶РµРЅРёРµ РґРѕР»Р¶РЅРѕ Р±С‹С‚СЊ С‚РѕР¶РґРµСЃС‚РІРµРЅРЅРѕ Р»РѕР¶РЅРѕ
# (Р·Р°РїРёСЃС‹РІР°РµРј РІ expr РѕР±СЂР°С‚РЅРѕРµ)
#-------------------------------------------------------
#intervals = {'P': (10,25), 'Q': (15,30), 'R': (25, 40) }
#expr = '!(A*!P*(Q->!R))'
#-------------------------------------------------------
# Р”РІР° РІС‹СЂР°Р¶РµРЅРёСЏ РґРѕР»Р¶РЅС‹ Р±С‹С‚СЊ С‚РѕР¶РґРµСЃС‚РІРµРЅРЅРѕ СЂР°РІРЅС‹
# (Р·Р°РїРёСЃС‹РІР°РµРј РІ expr РёС… СЌРєРІРёРІР°Р»РµРЅС‚РЅРѕСЃС‚СЊ)
#-------------------------------------------------------
#intervals = {'P': (5,10), 'Q': (10,20), 'R': (25, 40) }
#expr = '(A->P)=(Q->R)'
#-------------------------------------------------------
# Р”РІР° РІС‹СЂР°Р¶РµРЅРёСЏ РґРѕР»Р¶РЅС‹ Р±С‹С‚СЊ СЂР°Р·Р»РёС‡РЅС‹ РґР»СЏ РІСЃРµС… x
# (Р·Р°РїРёСЃС‹РІР°РµРј РІ expr РѕС‚СЂРёС†Р°РЅРёРµ РёС… СЌРєРІРёРІР°Р»РµРЅС‚РЅРѕСЃС‚Рё)
#-------------------------------------------------------
#intervals = {'P': (10,15), 'Q': (5,20), 'R': (15, 25) }
#expr = '!((!A->P)=(Q->R))'

#-------------------------------------------------------
#  TOTAL RANGE - РѕРїСЂРµРґРµР»РёС‚СЊ РїРѕР»РЅС‹Р№ РёРЅС‚РµСЂРІР°Р», Р·Р°С…РІР°С‚С‹РІР°РµРјС‹Р№
#    Р·Р°РґР°РЅРЅС‹РјРё РѕС‚СЂРµР·РєР°РјРё   
#-------------------------------------------------------
def TotalRange(intervals):
    first = True
    for (a,intv) in intervals.items():
        if first or intv[0] < xMin: xMin = intv[0]
        if first or intv[1] > xMax: xMax = intv[1]
        first = False
    return (xMin-1, xMax+1)    

#-------------------------------------------------------
#  AREA - РєР»Р°СЃСЃ, РѕРїРёСЃС‹РІР°СЋС‰РёР№ Р»РѕРіРёС‡РµСЃРєСѓСЋ С„СѓРЅРєС†РёСЋ,
#    Р·Р°РґР°РЅРЅСѓСЋ РѕС‚СЂРµР·РєР°РјРё СЃ С†РµР»РѕС‡РёСЃР»РµРЅРЅС‹РјРё РіСЂР°РЅРёС†Р°РјРё
#-------------------------------------------------------
class area:
    def __init__(self, rangex, truthIntv = (0,0)):
        self.xMin = rangex[0]
        self.xMax = rangex[1]
        if type(truthIntv[0]) == str:
            self.vals = ['A']*(self.xMax - self.xMin)
        else:
            self.vals = [False]*(self.xMax - self.xMin)
            self.setRange(truthIntv, True)
    def setVal(self, x, val):
        self.vals[x-self.xMin] = val
    def getVal(self, x):
        return self.vals[x-self.xMin]
    def setRange(self, intv, val):
        for x in range(*intv):
            self.setVal(x, val)
    def getRange(self):
        return (self.xMin, self.xMax)
    def printVals(self):
        for x in range(self.xMin,self.xMax):
            y = self.getVal(x)
            if type(y) == str:
                print(str(x)+':', y)
            else:
                print(str(x)+':', int(y))
    def notOp(self):
        res = area((self.xMin,self.xMax))
        for x in range(*self.getRange()):
            if self.getVal(x) == 'A':
                res.setVal(x, '!A')
            elif self.getVal(x) == '!A':
                res.setVal(x, 'A')    
            else:
                res.setVal(x, not self.getVal(x))
        return res
    def orOp(self,other):
        res = area((self.xMin,self.xMax))
        for x in range(*self.getRange()):
            y1 = self.getVal(x)
            y2 = other.getVal(x)
            if type(y1) == bool:
                if type(y2) == bool:
                    y = y1 or y2
                else:
                    if y1: y = True
                    else:  y = y2
            elif type(y2) == bool:
                if y2: y = True
                else:  y = y1
            elif y1 == y2:
                  y = y1
            else: y = True                     
            res.setVal(x, y)
        return res
    def andOp(self,other):
        res = area((self.xMin,self.xMax))
        for x in range(*self.getRange()):
            y1 = self.getVal(x)
            y2 = other.getVal(x)
            if type(y1) == bool:
                if type(y2) == bool:
                    y = y1 and y2
                else:
                    if not y1: y = False
                    else:      y = y2
            elif type(y2) == bool:
                if not y2: y = False
                else:      y = y1
            elif y1 == y2:
                  y = y1
            else: y = False                     
            res.setVal(x, y)
        return res
    def __add__(self, other):
        return self.orOp(other)
    def __mul__(self, other):
        return self.andOp(other)
    def inv(self):
        return self.notOp()
    def imp(self, other):
        return self.notOp() + other
    def eqv(self, other):
        return self*other + self.notOp()*other.notOp()
                 
#-------------------------------------------------------
#  PRIORITY - РѕРїСЂРµРґРµР»РµРЅРёРµ РїСЂРёРѕСЂРёС‚РµС‚Р° Р»РѕРіРёС‡РµСЃРєРёС… РѕРїРµСЂР°С†РёР№
#-------------------------------------------------------
def priority(op):
    if   op == '=': return 1
    elif op == '^': return 2
    elif op == '+': return 3
    elif op == '*': return 4
    elif op == '!': return 5
    else: return 100
#-------------------------------------------------------
#  LAST PERFORMED OP - РІРѕР·РІСЂР°С‰Р°РµС‚ РЅРѕРјРµСЂ СЃРёРјРІРѕР»Р°, РєРѕС‚РѕСЂС‹Р№
#    СЃРѕРґРµСЂР¶РёС‚ РїРѕСЃР»РµРґРЅСЋСЋ РІС‹РїРѕР»РЅСЏРµРјСѓСЋ РѕРїРµСЂР°С†РёСЋ 
#-------------------------------------------------------
def lastPerformedOp(s):
    minPrt = 50
    lastOp = -1
    nest = 0
    for i in range(len(s)):
        if s[i] == '(':
            nest += 1
        elif s[i] == ')':
            nest -= 1
            if nest < 0:
                raise SyntaxError()
        elif nest == 0   and  priority(s[i]) <= minPrt:
            minPrt = priority(s[i])
            lastOp = i
    assert(nest==0)
    return lastOp
   
#-------------------------------------------------------
#  COMPUTE EXPR - РІС‹С‡РёСЃР»РµРЅРёРµ Р»РѕРіРёС‡РµСЃРєРѕРіРѕ РІС‹СЂР°Р¶РµРЅРёСЏ
#    СЃ РЅРµРёР·РІРµСЃС‚РЅРѕР№ РїРµСЂРµРјРµРЅРЅРѕР№ A
#-------------------------------------------------------
def computeExpr(s):
    if len(s) == 0: return 0
    k = lastPerformedOp(s)
    if k < 0:
        if s[0] == '('  and  s[-1] == ')':
            return computeExpr(s[1:-1])
        elif len(s) == 1:
            return vars[s]
        else: raise SyntaxError("РќРµРІРµСЂРЅРѕРµ Р»РѕРіРёС‡РµСЃРєРѕРµ РІС‹СЂР°Р¶РµРЅРёРµ '" + s + "'")
    else:
        res1 = computeExpr(s[0:k])
        res2 = computeExpr(s[k+1:])
        op = s[k]
        if   op == '*': res = res1 * res2
        elif op == '+': res = res1 + res2
        elif op == '!': res = res2.inv()
        elif op == '^': res = res1.imp(res2)
        elif op == '=': res = res1.eqv(res2)
        return res
#-------------------------------------------------------
#  SHOW INTERVALS - РІС‹РІРµСЃС‚Рё РЅР° СЌРєСЂР°РЅ РёРЅС‚РµСЂРІР°Р»С‹, РіРґРµ
#    С„СѓРЅРєС†РёСЏ РёРјРµРµС‚ Р·Р°РґР°РЅРЅРѕРµ Р·РЅР°С‡РµРЅРёРµ
#-------------------------------------------------------
def showIntervals(R, value):
    (xMin, xMax) = R.getRange()
    x = xMin
    found = False
    while x < xMax:
      if R.getVal(x) == value:
        if x == xMin:
              xLeft = '-inf'
        else: xLeft = x
        while x < xMax and R.getVal(x) == value:
            x += 1
        if x >= xMax:
              xRight = 'inf'
        else: xRight = x
        print('    ('+str(xLeft)+', '+str(xRight)+')')
        found = True
      else:
        x += 1
    if not found:
        print('    РЅРµС‚')
#-------------------------------------------------------
# РћСЃРЅРѕРІРЅР°СЏ РїСЂРѕРіСЂР°РјРјР°
#-------------------------------------------------------
print("-------------------------------------------------------")
print("    Р РµС€РµРЅРёРµ Р·Р°РґР°С‡Рё Рђ10 РёР· РґРµРјРѕ-РІР°СЂРёР°РЅС‚Р° Р•Р“Р­-2013       ")
print("-------------------------------------------------------")
print('РР·РІРµСЃС‚РЅС‹Рµ РёРЅС‚РµСЂРІР°Р»С‹:')
for (k,v) in sorted(intervals.items()):
    print('    '+str(k)+': ' + str(v))
print('Р’С‹СЂР°Р¶РµРЅРёРµ:', expr)
print("")
RangeX = TotalRange(intervals)
vars = {}
for (k,v) in intervals.items():
    vars[k] = area(RangeX, v)
vars['A'] = area(RangeX, ('A','A'))         

expr = expr.replace('->','^')
R = computeExpr(expr)
print('Р“РґРµ РІСЃРµРіРґР° 0 Рё A РЅРёРєР°Рє РЅРµ РјРѕР¶РµС‚ РІР»РёСЏС‚СЊ:')
showIntervals(R, False)
print('Р“РґРµ РІСЃРµРіРґР° 1 Рё A РјРѕР¶РµС‚ Р±С‹С‚СЊ Р»СЋР±С‹Рј:')
showIntervals(R, True)
print('Р“РґРµ A РѕР±СЏР·Р°С‚РµР»СЊРЅРѕ РёСЃС‚РёРЅРЅРѕ:')
showIntervals(R, 'A')
print('Р“РґРµ A РѕР±СЏР·Р°С‚РµР»СЊРЅРѕ Р»РѕР¶РЅРѕ:')
showIntervals(R, '!A')
