import numpy as np
def DFS(start,cur,gra,max,n):
    niv=[]
    if(start==cur and max):
        max=max+1
        # print(max)
        niv.append(cur)
        return max,niv
        
    m=0

    for i in range(1,n):
        if(gra[cur][i]):
            st=[]
            a=gra.copy()
            l=gra[cur][i]
            # print(cur,i)
            le=gra[cur][i]
            a[cur][i]=0
            a[i][cur]=0
            l,st=DFS(start,i,a,l,n)
            # print(l)
            if (l!=le):
                # print(987979)
                if(l>m):
                    m=l
                    niv=st
    
    max=max+m
    niv.append(cur)
    return max,niv
    # print(max)




if __name__ == '__main__':
    n=37
    a=np.zeros((n,n))
    start=1
    max_len=0
    graph = [[] for i in range(n)]
    # graph[1].append([2,100])
    # graph[2].append([1,100])
    # graph[2].append([3,200])
    # graph[3].append([2,200])
    # graph[3].append([1,300])
    # graph[1].append([3,300])
    
    graph[1].append([2, 700])
    graph[1].append([8, 400])
    graph[8].append([9, 50])
    graph[9].append([3, 100])
    graph[3].append([2, 200])
    graph[2].append([6, 400])
    graph[5].append([6, 280])
    graph[2].append([5, 130])
    graph[4].append([5, 150])
    graph[3].append([4, 130])
    graph[4].append([7, 300])
    graph[6].append([12, 300])
    graph[12].append([14, 500])
    graph[12].append([7, 80])
    graph[7].append([11, 200])
    graph[11].append([17, 125])
    graph[8].append([10, 120])
    graph[11].append([14, 270])
    graph[11].append([13, 100])
    graph[13].append([14, 170])
    graph[15].append([36, 130])
    graph[34].append([36, 50])
    graph[34].append([35, 240])
    graph[16].append([35, 20])
    graph[33].append([34, 270])
    graph[31].append([33, 60])
    graph[16].append([31, 220])
    graph[16].append([18, 160])
    graph[18].append([30, 130])
    graph[18].append([20, 50])
    graph[19].append([20, 170])
    graph[18].append([19, 80])
    graph[20].append([21, 150])
    graph[21].append([23, 50])
    graph[21].append([29, 57])
    graph[29].append([24, 100])
    graph[23].append([24, 20])
    graph[24].append([25, 130])
    graph[25].append([28, 76])
    graph[28].append([29, 120])
    graph[29].append([30, 80])
    graph[27].append([28, 170])
    graph[26].append([27, 270])
    graph[25].append([26, 250])
    graph[22].append([27, 80])
    graph[22].append([32, 100])
    graph[22].append([30, 220])
    graph[30].append([31, 120])
    graph[32].append([33, 230])
    graph[16].append([17, 400])
    graph[10].append([19, 150])
    graph[15].append([35, 200])
    graph[34].append([36, 50])
    graph[12].append([15, 700])
    graph[1].append([23,860])


    graph[23].append([1,860])
    graph[2].append([1, 700])
    graph[8].append([1, 400])
    graph[9].append([8, 50])
    graph[3].append([9, 100])
    graph[2].append([3, 200])
    graph[6].append([2, 400])
    graph[6].append([5, 280])
    graph[5].append([2, 130])
    graph[5].append([4, 150])
    graph[4].append([3, 130])
    graph[7].append([4, 300])
    graph[12].append([6, 300])
    graph[14].append([12, 500])
    graph[7].append([12, 80])
    graph[11].append([7, 200])
    graph[17].append([11, 125])
    graph[10].append([8, 120])
    graph[14].append([11, 270])
    graph[13].append([11, 100])
    graph[14].append([13, 170])
    graph[36].append([15, 130])
    graph[36].append([34, 50])
    graph[35].append([34, 240])
    graph[35].append([16, 20])
    graph[34].append([33, 270])
    graph[33].append([31, 60])
    graph[31].append([16, 220])
    graph[18].append([16, 160])
    graph[30].append([18, 130])
    graph[20].append([18, 50])
    graph[20].append([19, 170])
    graph[19].append([18, 80])
    graph[21].append([20, 150])
    graph[23].append([21, 50])
    graph[29].append([21, 57])
    graph[24].append([29, 100])
    graph[24].append([23, 20])
    graph[25].append([24, 130])
    graph[28].append([25, 76])
    graph[29].append([28, 120])
    graph[30].append([29, 80])
    graph[28].append([27, 170])
    graph[27].append([26, 270])
    graph[26].append([25, 250])
    graph[27].append([22, 80])
    graph[32].append([22, 100])
    graph[30].append([22, 220])
    graph[31].append([30, 120])
    graph[33].append([32, 230])
    graph[17].append([16, 400])
    graph[19].append([10, 150])
    graph[35].append([15, 200])
    graph[36].append([34, 50])
    graph[15].append([12, 700])

    # a=0
    for i in range(1,n):
        for j in range(len(graph[i])):
            a[i][graph[i][j][0]]=graph[i][j][1]
            a[graph[i][j][0]][i]=graph[i][j][1]
    # print(list(a))
    len=0
    for i in range(1,n):
        for j in range(1,n):
            len+=a[i][j]
    
    max_len,b=DFS(start,start,a,max_len,n)
    print(max_len)
    print(b)
    print(len/2)

    # nivesh=1
    # print("Maximum length of cable =",ongestCable(graph, n,nivesh))