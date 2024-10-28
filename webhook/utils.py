import hmac
import hashlib

def verify_signature(payload, received_signature, secret_key):
    """
    Verifies the HMAC SHA256 signature of the payload.
    """
    payload_str = ''.join(str(value) for value in payload.values())
    print("payload_str: " + payload_str)
    signed_payload = payload_str.encode("utf-8")
    print("signed_payload: " + str(signed_payload))
    expected_signature = hmac.new(
        key=secret_key.encode(),
        msg=signed_payload,
        digestmod=hashlib.sha256
    ).hexdigest()
    print("expected_signature: " + expected_signature)
    print("received_signature: " + received_signature)
    return hmac.compare_digest(received_signature, expected_signature)

