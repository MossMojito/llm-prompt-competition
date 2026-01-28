"""
Example Student Submission - Alice Johnson
==========================================

This is an example submission showing best practices.
Strategy: Few-shot learning with balanced examples.
"""

# ============================================================================
# STUDENT INFORMATION
# ============================================================================

STUDENT_NAME = "Alice Johnson (Example)"
STUDENT_ID = "alice_example_001"

STRATEGY_DESCRIPTION = """
Few-shot learning approach with 4 balanced examples (2 positive, 2 negative).
Uses clear instructions and explicit output format specification.
Emphasizes the importance of looking at overall sentiment rather than individual words.
"""

EXPECTED_ACCURACY = 0.87  # Based on local testing


# ============================================================================
# PROMPT FUNCTION
# ============================================================================

def get_prompt(review_text):
    """
    Generate few-shot prompt with balanced examples.
    
    Design decisions:
    - 4 examples total (2 pos, 2 neg) - enough to show pattern without being too long
    - Clear and diverse examples covering different sentiment expressions
    - Explicit instruction to output ONLY the classification
    - Consistent formatting throughout
    
    Args:
        review_text: The movie review to classify
        
    Returns:
        Complete prompt string
    """
    
    prompt = f"""Classify the following movie reviews as either Positive or Negative based on the overall sentiment.

Example 1:
Review: "This film was absolutely brilliant! The acting was superb and the storyline kept me engaged throughout. Highly recommended!"
Classification: Positive

Example 2:
Review: "Complete waste of time. The plot was confusing, the characters were unlikeable, and I regretted watching it."
Classification: Negative

Example 3:
Review: "A masterpiece! Beautiful cinematography combined with powerful performances. One of the best films I've seen this year."
Classification: Positive

Example 4:
Review: "Disappointing and dull. The pacing was painfully slow and the ending felt rushed. Not worth your time or money."
Classification: Negative

Now classify this review. Respond with ONLY one word - either "Positive" or "Negative":

Review: {review_text}

Classification:"""
    
    return prompt


# ============================================================================
# OUTPUT PARSING
# ============================================================================

def parse_output(llm_output):
    """
    Parse LLM output to extract classification.
    
    Handles common variations:
    - Direct: "Positive" or "Negative"
    - With punctuation: "Positive." or "Negative!"
    - In sentence: "The sentiment is Positive"
    
    Args:
        llm_output: Raw output from the LLM
        
    Returns:
        Either "Positive" or "Negative"
    """
    # Clean the output
    output = llm_output.strip()
    
    # Check for positive
    if "Positive" in output or "positive" in output:
        return "Positive"
    
    # Check for negative
    if "Negative" in output or "negative" in output:
        return "Negative"
    
    # Default fallback (should rarely happen with good prompts)
    # Could also raise an error instead
    return "Positive"


# ============================================================================
# LOCAL TESTING
# ============================================================================

def test_locally():
    """
    Test the prompt with example reviews to verify it works as expected.
    """
    test_cases = [
        {
            "text": "Amazing movie! Loved every second of it. The best film this year!",
            "expected": "Positive",
            "difficulty": "Easy"
        },
        {
            "text": "Terrible. Don't waste your money on this garbage.",
            "expected": "Negative",
            "difficulty": "Easy"
        },
        {
            "text": "Not bad, but could have been better. Some good moments mixed with boring scenes.",
            "expected": "Positive",  # Borderline - mostly neutral but leans slightly positive
            "difficulty": "Hard"
        },
        {
            "text": "I expected more from this director. While it had potential, it ultimately disappointed.",
            "expected": "Negative",
            "difficulty": "Medium"
        }
    ]
    
    print("=" * 70)
    print(f"Testing: {STUDENT_NAME}")
    print(f"Strategy: {STRATEGY_DESCRIPTION[:100]}...")
    print("=" * 70)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i} ({test['difficulty']}):")
        print(f"Review: {test['text'][:80]}...")
        print(f"Expected: {test['expected']}")
        
        # Generate prompt (just show preview)
        prompt = get_prompt(test['text'])
        print(f"\nPrompt length: {len(prompt)} characters")
        print("Prompt preview (first 200 chars):")
        print(prompt[:200] + "...")
        print("-" * 70)


# ============================================================================
# NOTES & LESSONS LEARNED
# ============================================================================

"""
Development Process:
-------------------
1. Started with zero-shot - got ~75% accuracy
2. Added 2 examples - improved to ~82%
3. Increased to 4 balanced examples - reached ~87%
4. Tried 6 examples - no improvement, just longer prompts
5. Settled on 4 examples as optimal balance

Key Insights:
------------
- Balance is crucial: equal positive and negative examples
- Clear output format specification reduces parsing errors
- Diverse examples help cover different sentiment expressions
- More examples ≠ always better (diminishing returns after 4-5)

What Didn't Work:
----------------
- Very long prompts with detailed instructions (confused the model)
- Unbalanced examples (3 positive, 1 negative - created bias)
- Vague output format (got responses like "I think it's positive because...")

Future Improvements:
------------------
- Could try chain-of-thought for borderline cases
- Could experiment with different example selections
- Could add explicit handling of mixed reviews
"""


if __name__ == "__main__":
    test_locally()
