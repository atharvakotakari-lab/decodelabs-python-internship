# Project 4: The General Knowledge Quiz
# Powered by DecodeLabs

def run_quiz():
    # State Initialization: Persistent score tracker vault
    score = 0
    total_questions = 3

    print("=== DecodeLabs General Knowledge Quiz ===")
    print("Answer the following 3 questions. Good luck!\n")

    # Question 1
    q1_answer = input("1. What is the capital of France? ").strip().lower()
    if q1_answer == "paris":
        print("✓ Correct! +1 point.\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is Paris.\n")

    # Question 2
    q2_answer = input("2. What is 5 + 5? ").strip().lower()
    if q2_answer == "10":
        print("✓ Correct! +1 point.\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 10.\n")

    # Question 3
    q3_answer = input("3ures Which programming language is this training kit for? ").strip().lower()
    if q3_answer == "python":
        print("✓ Correct! +1 point.\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is Python.\n")

    # Output / Final Display
    print("========================================")
    print(f"QUIZ COMPLETED!")
    print(f"FINAL SCORE: {score:>2} / {total_questions}")
    print("========================================")
    print("System Status: Evaluation Finished.")

if __name__ == "__main__":
    run_quiz()