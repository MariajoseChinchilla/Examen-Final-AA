#Tipo 1 de silla sera menor, tipo 2 sera mayor.
def files(list,N):
    F = [i for i in range(N**2)]  #lista para filas
    for i in range(N):    #revisamos si la entrada es punto silla en su fila
        for j in range(1,N-1):  #revisar el interior de la fila
            if list[i][j] <= list[i][j-1] and list[i][j] <= list[i][j+1]:
                F[N*i+j] = ((i,j),1)
            elif list[i][j] >= list[i][j - 1] and list[i][j] >= list[i][j + 1]:
                F[N*i+j] = ((i,j),2)
            else:
                F[N*i+j] = ((i,j),0)
    #chequeo para las orillas
        if list[i][0] <= list[i][1]:
            F[N*i] = ((i,0),1)
        if list[i][0] >= list[i][1]:
            F[N*i] = ((i,0),2)
        if list[i][N-1] <= list[i][N-2]:
            F[N*(i+1)-1] = ((i,N-1),1)
        if list[i][N-1] >= list[i][N-2]:
            F[N*(i+1)-1] = ((i,N-1),2)
    return F

def columns(list, N):
    C = [i for i in range(N**2)]  #lista para columnas
    for i in range(N):    #revisamos si la entrada es punto silla en su columna
        for j in range(1,N-1):  #revisar el interior de la columna
            if list[j][i] <= list[j-1][i] and list[j][i] <= list[j+1][i]:
                C[N*i+j] = ((j,i),1)      #guardar en el mismo orden, como si fuese fila
            elif list[j][i] >= list[j-1][i] and list[j][i] >= list[j+1][i]:
                C[N*i+j] = ((j,i),2)
            else:
                C[N*i+j] = ((j,i),0)
    #chequeo para las orillas
        if list[0][i] <= list[1][i]:
            C[N*i] = ((0,i),1)
        if list[i][0] >= list[i][1]:
            C[N*i] = ((i,0),2)
        if list[N-1][i] <= list[N-2][i]:
            C[N*i+N-1] = ((N-1,i),1)
        if list[N-1][i] >= list[N-2][i]:
            C[N*i+N-1] = ((N-1,i),2)
    return sorted(C)

def chair(list):
    N = len(list)
    filas = sorted(files(list, N))
    columnas = columns(list,N)
    for i in range(N**2):
        if filas[i][1] + columnas[i][1] == 3:       #significa que es punto silla de diferente tipo
            print('({},{})'.format(filas[i][0][0]+1,filas[i][0][1]+1))

chair([[1,-10,3,2,5],[-1,1,4,3,7],[0,2,3,6,3],[1,8,4,6,2],[0,4,-1,5,1]])