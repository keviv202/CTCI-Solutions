class ch1q7:
        def matrot(self):
            Matrix = [[0 for x in range(4)] for y in range(4)]
            Matrix1 = [[0 for x in range(4)] for y in range(4)]
            k = 1
            #for (i, j) in [(i, j) for i in range(x) for j in range(y)]
            for (i,m) in zip(reversed (range(0,4)) , range(0,4)):
                for (j,l) in zip((range(0,4)) , range(0,4)):
                    Matrix[j][i] = k
                    Matrix1[m][l] = k
                    k = k + 1
            print (Matrix)
            print(Matrix1)

c = ch1q7()
c.matrot()
