class ch1q8:

    def zeromat(self):
        import random
        matrix1 = [[0 for x in range(100)] for y in range(100)]
        matrix2 = [[0 for x in range(100)] for y in range(100)]

        for i in range(100):
            for j in range(100):
                matrix1[i][j] = random.randrange(0,100)
        print (matrix1)

        for i in range(100):
            for j in range(100):
                if matrix1[i][j]==0:
                    for k in range(100):
                        matrix1[i][k] = 'a'
                    for l in range(100):
                        matrix1[l][j] = 'a'


        print(matrix1)

c = ch1q8()
c.zeromat()