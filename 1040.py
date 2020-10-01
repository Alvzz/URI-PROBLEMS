x = input().split()
n1 = float(x[0])
n2 = float(x[1])
n3 = float(x[2])
n4 = float(x[3])
m = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/10
print('Media: {:.1f}'.format(m))
if m >= 7.0:
    print('Aluno aprovado.')
if m < 5.0:
    print('Aluno reprovado.')
if 5.0 <= m <= 6.9:
    print('Aluno em exame.')
    y = float(input())
    print('Nota do exame: {}'.format(y))
    mf = (y + m) / 2
    if mf >=5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(mf))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(mf))
        