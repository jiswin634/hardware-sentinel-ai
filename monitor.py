import time
import os

while True:
    print("Starting monitoring cycle...")

    os.system("python collector.py")
    os.system("python scorer.py")
    os.system("python history.py")
    os.system("python predictor.py")
    os.system("python verify_identity.py")
    os.system("python ai_analyzer.py")

    print("\nCycle complete.")
    print("Waiting 15 seconds...\n")

    time.sleep(15)