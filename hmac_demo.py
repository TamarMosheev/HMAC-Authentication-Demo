import hmac
import hashlib

def create_hmac(message: bytes, key: bytes) -> str:
    return hmac.new(key, message, hashlib.sha256).hexdigest()

def is_message_authentic(message: bytes, received_mac: str, key: bytes) -> bool:
    expected_mac = create_hmac(message, key)
    return hmac.compare_digest(received_mac, expected_mac)

if __name__ == "__main__":
    # -----------------------------
    # Step 1: Sender creates message and authentication code
    # -----------------------------

    # Shared secret key
    secret_key = b'supersecretkey'

    # The message to be sent
    message = b'This is a very important message.'

    # Compute HMAC using SHA-256 & Generated authentication code
    mac = create_hmac(message,secret_key)



    print("\n🔐 Sender side:")
    print("Message:", message)
    print("HMAC:", mac)

    # -----------------------------
    # Step 2: Receiver verifies authenticity (original message)
    # -----------------------------
    print("\n📥 Receiver side: ")
    print("Message:", message)

    # Assume the message and HMAC were received
    received_message = message
    received_mac = mac

    # Receiver recomputes the HMAC
    isAuthentic = is_message_authentic(received_message,received_mac,secret_key)

    # Compare received HMAC to recomputed HMAC
    if isAuthentic:
        print("\n✅ Message is authentic and intact.")
    else:
        print("\n❌ Message is NOT authentic or was tampered with.")

    # -----------------------------
    # Step 3: Receiver checks a modified message
    # -----------------------------
    
    # 🔧 The message was modified along the way!
    received_message = b'This is a very modified message.'  # <--- Intentional modification!

    print("\n📥 Receiver side: ")
    print("Message:", received_message)
    
    # Receiver recomputes the HMAC
    isAuthentic = is_message_authentic(received_message,received_mac,secret_key)

    # Compare received HMAC to recomputed HMAC
    if isAuthentic:
        print("\n✅ Message is authentic and intact.\n")
    else:
        print("\n❌ Message is NOT authentic or was tampered with.\n")

