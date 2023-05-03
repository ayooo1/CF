def Special_Pythagorean_triplet():
    for i in range(1,1001):
        for j in range(i,1001):
            for k in range(j,1001):
                if i**2 + j **2 == k**2:
                    if i + j + k == 1000:
                        return i*j*k

print(Special_Pythagorean_triplet())