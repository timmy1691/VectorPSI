import tenseal as ts
from time import time


def KeyGeneration():
    context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
    )

    # public data
    public_bytes = context.serialize(
    save_public_key=True,
    save_secret_key=False
    )

    # Private context (contains secret key)
    private_bytes = context.serialize(
        save_public_key=True,
        save_secret_key=True
    )

    return public_bytes, private_bytes



def encrypt(Set, public_context):
    encrypted = ts.ckks_vector(public_context, Set)
    return encrypted



def decrypt(encSet, private_context):
    encrypted_received = ts.ckks_vector_from(
    private_context,
    encSet
    )

    decrypted = encrypted_received.decrypt()
    return decrypted


def computeComparison(vec1, vec2):
    """
    Comparison for dot product
    """

    dist = vec1.dot(vec2)

    return dist


def computeComparison(vec1, vec2):
    """
    Comparison for l1 approx
    """

    dist = vec1 - vec2

    return dist.sum()