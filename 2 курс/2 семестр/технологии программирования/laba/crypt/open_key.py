def input_private_key():
    private_key = list(map(int, input('Input private key\n').split()))
    s = 0
    for n in private_key:
        if n > s:
            s += n
        else:
            break
    if s < sum(private_key):
        print('Private key is not correct')
        return input_private_key()
    else:
        with open('private_key.txt', 'w') as file:
            file.write(' '.join(map(str, private_key)))
        return private_key


private_key = input_private_key()
n = 7

m = sum(private_key) + 10

def gcdExtended(a, b):
    if a == 0 :
        return b, 0, 1
    gcd1, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd1, x, y

gcd1, x, y = gcdExtended(n, m)

mn = (x % m + m) % m

def generate_key_based_on_private_key(private_key = []):
    public_key = []
    for number in private_key:
        public_key.append(number * n % m)
    with open('public_key', 'w') as file:
        file.write(' '.join(map(str, public_key)))
    return public_key

def myltiplication(message = '', key = []):
    s = 0
    for i in range(len(message)):
        if message[i] == '1':
            s += key[i]
    return s

def encryption(message_for_encryption = '', public_key = []):
    l = len(public_key)
    message_partials = [message_for_encryption[x:x + l] for x in range(0, len(message_for_encryption), l)]
    encrypted_value = []
    for partial in message_partials:
        encrypted_value.append(myltiplication(partial, public_key))
    return encrypted_value

def decryption(message_for_decryption = [], private_key = []):

    partial_values = []
    for part in message_for_decryption:
        partial_values.append(part * mn % m)
    result = ''
    reversed_private_key = private_key[::-1]
    for partial in partial_values:
        r = ''
        s = 0
        for value in reversed_private_key:
            if value + s <= partial:
                s += value
                r += '1'
            else:
                r += '0'
        result += r[::-1]
    return result

public_key = generate_key_based_on_private_key(private_key)

message_for_encryption = input('Input phrase for encryption\n')# 100100111100101110'

encrypted_value = encryption(message_for_encryption, public_key)
with open('encrypted_value.txt', 'w') as file:
    file.write(' '.join(map(str, encrypted_value)))

decrypted_value = decryption(encrypted_value, private_key)
with open('decrypted_value.txt', 'w') as file:
    file.write(decrypted_value)
