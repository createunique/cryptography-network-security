
# Initial Permutation  [ IP Table ]
ip = [58, 50, 42, 34, 26, 18, 10, 2, 
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 
      63, 55, 47, 39, 31, 23, 15, 7]


# permuted choice - 1
pc1 = [57, 49, 41, 33, 25, 17, 9, 
      1, 58, 50, 42, 34, 26, 18,
      10, 2, 59, 51, 43, 35, 27, 
      19, 11, 3, 60, 52, 44, 36,
      63, 55, 47, 39, 31, 23, 15, 
      7, 62, 54, 46, 38, 30, 22,
      14, 6, 61, 53, 45, 37, 29, 
      21, 13, 5, 28, 20, 12, 4]

# permuted choice - 2
pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
      23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
      41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33,
      48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]



# Expansion Function
efunc = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11,
      12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19,
      20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27,
      28, 29, 28, 29, 30, 31, 32, 1]


# round function permutation
rpc = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26,
      5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9,
      19, 13, 30, 6, 22, 11, 4, 25]

# S-box Table
sbox = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

# IP^-1 Table
ipinv = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


# Shift Table
st = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]



# Hexadecimal to binary conversion
def h2b(s):
    return bin(int(s, 16))[2:].zfill(len(s) * 4)

# Binary to hexadecimal conversion
def b2h(s):
    return hex(int(s, 2))[2:].upper()

# Binary to decimal conversion
def b2d(b):
    return int(b, 2)

# Decimal to binary conversion
def d2b(n):
    return bin(n)[2:].zfill((len(bin(n)[2:]) + 3) // 4 * 4)

# Permute function to rearrange the bits
def p(k, a, n):
    return ''.join(k[a[i] - 1] for i in range(n))

# Shifting the bits towards left by nth shifts
def sl(k, n):
    return k[n:] + k[:n]

# Calculating XOR of two binary strings
def xr(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))


def encrypt(pl, kb, kh):
    th2b= h2b(pl)

    # Initial Permutation
    pl = p(th2b, ip, 64)
    print(f"Initial Permutation : {b2h(pl)}")

    l = pl[:32]
    r= pl[32:]
    print()
    for k in range(16):
        
        #expansion function expanding 32 bits to 48 bits
        er = p(r, efunc, 48)
        
        #XOR operation : round key and expanded right half
        kx = xr(er, kb[k])
        
        sf = ''#s-box value

        #s-box operation 6 bits to 4 bits
        for m in range(8):
            br = kx[m*6 :m*6 + 6]
            row = b2d(br[0] + br[-1])
            col = b2d(br[1:-1])
            sf += d2b(sbox[m][row][col])
        
        sf = p(sf, rpc, 32) #permutation inside round function
        
        l, r = r, xr(l, sf)#swapping left and right half of 64 bits

        if k == 15: #last round no swapping of left and right half
            l, r = l, r
        
        print(f"Round {k + 1:2} {b2h(l)} {b2h(r)} {kh[k]}")
    
    tcomblr=r+l
    return p(tcomblr, ipinv, 64)

def main():
    pl = "A12ab5e221dcc389"
    print("\nPlain Text : ", pl)
    
    ky = "0231ab3c4de55ac4"
    
    kb = []
    kh = []

    tth2b = h2b(ky)
    ky = p(tth2b,pc1, 56)
    l, r = ky[:28], ky[28:]
    
    for i in range(16):
        l, r = sl(l, st[i]), sl(r, st[i])
        kb.append(p(l+r, pc2, 48))
        kh.append(b2h(kb[-1]))
    
    

    print("\n------------ Encryption ------------")
    ct = b2h(encrypt(pl, kb, kh))
    print("\nEncrypted Cipher Text : ", ct)
    

    print("\n------------ Decryption ------------")
    kb = kb[::-1]
    kh = kh[::-1]
    pt = b2h(encrypt(ct, kb, kh))
    
    print("\nDecrypted Plain Text :", pt)

if __name__ == "__main__":
    main()
