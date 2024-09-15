# RSA Encryption and Decryption Script

## Overview

This project contains Python scripts for RSA encryption and decryption. The `rsa_algorithm.py` script generates RSA key pairs and calculates RSA parameters, while `main.py` provides a command-line interface for encrypting and decrypting messages using RSA.

## Files

- `rsa_algorithm.py`: Contains functions and classes for RSA key generation, modular arithmetic, and encryption/decryption operations.
- `main.py`: Provides a user interface for selecting encryption or decryption, entering parameters, and processing messages.

## Features

- RSA Key Generation: Generates public and private keys, including modulus \(n\), public exponent \(e\), and private exponent \(d\).
- Encryption: Encrypts a message using the RSA public key.
- Decryption: Decrypts an encrypted message using the RSA private key.

## Prerequisites

- Python 3.x
- No external libraries are required for basic functionality.

## Usage

1. **Key Generation:**
   Run `rsa_algorithm.py` to generate RSA keys and save them to `rsa_info.txt`. This file contains the generated primes, modulus, public exponent, and private exponent.

   ```bash
   python rsa_algorithm.py
   ```
2. **Encryption and Decryption:**
   Run `main.py` to encrypt or decrypt messages.
   Follow the prompts to:

   Choose encryption (C) or decryption (D).
   Enter the message, public/private key parameters (e.g., 𝑒, 𝑑, 𝑛).
