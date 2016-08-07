def build_shift_dict(self, shift):
    import string
    alpha=string.ascii_lowercase
    beta=string.ascii_uppercase
    gamma={}
    phi={}
    shift=4
    j=0
    for i in range(len(alpha)):
        if (i+shift)<len(alpha):
            gamma[alpha[i]]=alpha[i+shift] 
        else:
            gamma[alpha[i]]=alpha[j]
            j+=1
    k=0
    for i in range(len(beta)):
        if (i+shift)<len(beta):
            phi[beta[i]]=beta[i+shift] 
        else:
            phi[beta[i]]=alpha[k]
            k+=1
    z = phi.copy()
    z.update(gamma)
    return z
def apply_shift(self, shift):
    alpha=''
    z=self.build_shift_dict(shift)
    for i in self.message_text:
        if i in z:
            alpha[iz[i])
        else:
            alpha.append(i)
    return alpha