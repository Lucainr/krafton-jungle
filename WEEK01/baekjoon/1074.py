def z(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1) # 2의 n-1승 n이 2라면 2^2 * 2^2의 크기의 사분면에서의 절반이니까 2*2사이즈의 사분면이 4개가 생김
    if r < half and c < half:
        return z(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + z(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + z(n - 1, r - half, c)
    else:  # r >= half and c >= half
        return 3 * half * half + z(n - 1, r - half, c - half)

N, r, c = map(int, input().split())
print(z(N, r, c))