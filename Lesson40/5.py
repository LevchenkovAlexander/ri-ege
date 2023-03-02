def km_to_miles(kms):
    kms = int(kms) if "." not in kms else float(kms)
    return kms * 0.6214


while 1: print(km_to_miles(input()))