ESP_MEM = 500 #Global

# ATRIBUTOS DE LOS LIMITES
# Limites globales
limIntGLB = ESP_MEM
limFltGLB = ESP_MEM + limIntGLB
limStrGLB = ESP_MEM + limFltGLB

# Limites Locales
limIntLC = ESP_MEM + limStrGLB
limFltLC = ESP_MEM + limIntLC
limStrLC = ESP_MEM + limFltLC

#Limites temporales
limIntTMP = ESP_MEM + limStrLC
limFltTMP = ESP_MEM + limIntTMP
limStrTMP = ESP_MEM + limFltTMP
limBoolTMP = ESP_MEM + limStrTMP

#Limites constantes
limIntCNS = ESP_MEM + limBoolTMP
limFltCNS = ESP_MEM + limIntCNS
limStrCNS = ESP_MEM + limFltCNS

# ATRIBUTOS DE LOS INICIOS
# Inicios globales
iniIntGLB = 0
iniFltGLB = limIntGLB
iniStrGLB = limFltGLB

# Inicios Locales
iniIntLC = limStrGLB
iniFltLC = limIntLC
iniStrLC = limFltLC

# Inicios Temporales
iniIntTMP = limStrLC
iniFltTMP = limIntTMP
iniStrTMP = limFltTMP
iniBoolTMP = limStrTMP

# Inicios Constantes
iniIntCNS = limBoolTMP
iniFltCNS = limIntCNS
iniStrCNS = limFltCNS

class MemVirtual:
    def temporales(tipo):
        if tipo == "entero":
            if iniIntTMP < limIntTMP:
                temp = iniIntTMP
                iniIntTMP += 1
            else :
                print("Error: ya no hay memoria")
        elif tipo == "float":
            if iniFltTMP < limFltTMP:
                temp = iniFltTMP
                iniFltTMP +=1
            else :
                print("Error: ya no hay memoria")
        elif tipo == "bool":
            if iniBoolTMP < limBoolTMP:
                temp = iniBoolTMP
                iniBoolTMP +=1
            else :
                print("Error: ya no hay memoria")

        return temp

    def memoria(tipo, espMem):
        if espMem == "global":
            if tipo == "entero" :
                if iniIntGLB < limIntGLB:
                    temp = iniIntGLB
                    iniIntGLB += 1
                else :
                    print("Error: ya no hay memoria")
            elif tipo == "float" :
                if iniFltGLB < limFltGLB:
                    temp = iniFltGLB
                    iniFltGLB += 1
                else :
                    print("Error: ya no hay memoria")
            elif tipo == "string" :
                if iniStrGLB < limStrGLB:
                    temp = iniStrGLB
                    iniStrGLB += 1
                else :
                    print("Error: ya no hay memoria")

        else:
            if tipo == "entero" :
                if iniIntLC < limIntLC:
                    temp = iniIntLC
                    iniIntLC += 1
                else :
                    print("Error: ya no hay memoria")
            elif tipo == "float" :
                if iniFltLC < limFltLC:
                    temp = iniFltLC
                    iniFltLC += 1
                else :
                    print("Error: ya no hay memoria")
            elif tipo == "string" :
                if iniStrLC < limStrLC:
                    temp = iniStrLC
                    iniStrLC += 1
                else :
                    print("Error: ya no hay memoria")

    def eliminar():
        iniIntLC = limStrGLB
        iniFltLC = limIntLC
        iniStrLC = limFltLC
    
        iniIntTMP = limStrLC
        iniFltTMP = limIntTMP
        iniStrTMP = limFltTMP
        iniBoolTMP = limStrTMP

#        elif espMem == "constante":
#           if tipo == "entero" :
#                if iniIntCNS < limIntCNS:
#                    temp = iniIntCNS
#                    iniIntCNS += 1
#                else :
#                    print("Error: ya no hay memoria")
#            elif tipo == "float" :
#                if iniFltCNS < limFltCNS:
#                    temp = iniFltCNS
#                    iniFltCNS += 1
#                else :
#                    print("Error: ya no hay memoria")
#            elif tipo == "string" :
#                if iniStrCNS < limStrCNS:
#                    temp = iniStrCNS
#                    iniStrCNS += 1
#                else :
#                    print("Error: ya no hay memoria")
#        
#        return temp
