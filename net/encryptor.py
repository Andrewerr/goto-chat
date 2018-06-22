import nacl
import nacl.secret
import nacl.utils

def encryption(msg):
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
    box = nacl.secret.SecretBox(key)
    message = msg
    encrypted = box.encrypt(message)
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
    encrypted = box.encrypt(message, nonce)
    return encrypted
