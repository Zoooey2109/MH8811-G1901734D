# Zhou Yuying_G1901734D

def caesar_decrypt(m, k):
    str_list = list(m)
    str_list_decry = str_list
    i = 0
    while i < len(str_list):
        if ord(str_list[i]) >= ord('a'):
            str_list_decry[i] = chr((ord(str_list[i])-ord('a') + k)%26 +ord('a'))
        else:
            str_list_decry[i] = str_list[i]
        i = i+1
    return str_list_decry

def vigenere_decrypt(m,k):
    str_list_1 = list(k*(int(len(m)//len(k))+1))
    str_list_decry_1 = [0]*len(m)
    for i in range(len(m)):
        if m[i].isalpha():
            str_list_decry_1[i] = chr((ord(m[i])- ord(str_list_1[i])) % 26 + ord('a'))
        else:
            str_list_decry_1[i] = m[i]
    return str_list_decry_1   


key_lst=["blink","nose","rabbit","thunder","match","heavenly","stereotype","bake"]

def decipher(m):
    klen=len(key_lst)
# Message was encrpted by V(m) or V(C(m))
    for v in range(klen):      
        k_1=key_lst[v]
        d_v =vigenere_decrypt(m,k_1)  
        if d_v[:20]==list("root@hackernetwork$>"):
            return (True,"".join(d_v)) 
        for vc in range(1,26):# V >>> C
            d_vc=caesar_decrypt(d_v,vc)
            if d_vc[:20]==list("root@hackernetwork$>"):
                return (True,"".join(d_vc))
            
# Message was encrpted by C(m) or C(V(m))  
    for c in range(1,26):
        d_c =caesar_decrypt(m,c)
        if d_c[:20]==list("root@hackernetwork$>"):
            return (True,"".join(d_c))
        for cv in range(klen):# C >>> V
            k_1=key_lst[cv]
            d_cv = vigenere_decrypt(d_c,k_1)  
            if d_cv[:20]==list("root@hackernetwork$>"):
                return (True,"".join(d_cv))
    return (False,'')


# Main program

if __name__ == "__main__":
    file = open("intercepted.txt", "r")
    m = file.readlines()
    for m in m:
        print(decipher(m.strip()))
