# 🔐 HMAC Authentication Demo

This is a simple Python script demonstrating how to use **HMAC (Hash-based Message Authentication Code)** with the built-in `hmac` and `hashlib` libraries to verify the **authenticity** and **integrity** of a message.

## 📄 Files

* `hmac_demo.py` — Main script that simulates sender and receiver sides using HMAC with SHA-256.
* `test_hmac_demo.py` — Unit tests to verify the HMAC functionality.

## 🛠 Requirements

* Python 3.6 or higher
* No external packages required — all used modules are part of the Python Standard Library.
* Optional for testing: `pytest` (install via `pip install pytest`)

## ▶️ How to Run the Demo

1. Save this folder to your computer.
2. Open a terminal or command prompt.
3. Navigate to the folder using the `cd` command.
4. Run the script using:

   ```bash
   python hmac_demo.py
   ```

## ✅ Expected Output

```
🔐 Sender side:
Message: b'This is a very important message.'
HMAC: <generated_hash>

📥 Receiver side: 
Message: b'This is a very important message.'

✅ Message is authentic and intact.

📥 Receiver side: 
Message: b'This is a very modified message.'

❌ Message is NOT authentic or was tampered with.
```

---

## 🧪 Running the Tests

If you want to verify the correctness of the HMAC logic using automated tests:

1. Make sure `pytest` is installed:

```bash
pip install pytest
```

2. In the terminal, run:

```bash
pytest
```

This will execute all the tests and print a summary of the results.