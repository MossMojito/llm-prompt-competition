"""
Student Prompt Template
========================

INSTRUCTIONS:
1. Copy this file and rename it to your_name.py
2. Fill in your information below
3. Implement your prompt strategy in get_prompt()
4. Test locally before submitting
5. Submit via Pull Request

EXAMPLE:
    cp template.py john_doe.py
"""

# ============================================================================
# STUDENT INFORMATION (Required)
# ============================================================================

STUDENT_NAME = "Your Name"  # e.g., "John Doe"
STUDENT_ID = "your_id"  # e.g., "student123" or your email

STRATEGY_DESCRIPTION = """
Brief description of your prompt engineering strategy.

Examples:
- "Zero-shot with clear instructions"
- "Few-shot learning with 3 examples per class"
- "Chain-of-thought reasoning with sentiment analysis steps"
- "Role-playing as a movie critic"
"""

# Expected performance (optional, for your reference)
EXPECTED_ACCURACY = 0.0  # e.g., 0.85 for 85%


# ============================================================================
# PROMPT FUNCTION (Required)
# ============================================================================

def get_prompt(review_text):
    """
    Generate the complete prompt for sentiment classification.
    
    This function will be called by the evaluation system for each review.
    
    Args:
        review_text (str): The movie review to classify
        
    Returns:
        str: Complete prompt to send to the LLM
        
    IMPORTANT RULES:
    - Prompt must be under 1000 tokens
    - Output must be EXACTLY "Positive" or "Negative" (case-sensitive)
    - No additional text in the output
    - You can use few-shot examples, instructions, etc.
    
    EXAMPLE STRATEGIES:
    
    1. Zero-shot (simple instruction):
        prompt = f'''Classify this movie review as Positive or Negative.
        
        Review: {review_text}
        
        Classification:'''
        
    2. Few-shot (with examples):
        prompt = f'''Classify movie reviews as Positive or Negative.
        
        Example 1:
        Review: "Amazing film! Loved every minute."
        Classification: Positive
        
        Example 2:
        Review: "Boring and predictable plot."
        Classification: Negative
        
        Now classify this review:
        Review: {review_text}
        Classification:'''
        
    3. Chain-of-thought:
        prompt = f'''Analyze this movie review step by step:
        
        Review: {review_text}
        
        1. Identify key sentiment words
        2. Determine overall tone
        3. Classify as Positive or Negative
        
        Classification:'''
    """
    
    # ========================================
    # YOUR PROMPT STRATEGY HERE
    # ========================================
    
    prompt = f"""
    [Replace this with your prompt template]
    
    Review: {review_text}
    
    Classification:
    """
    
    return prompt


# ============================================================================
# POST-PROCESSING (Optional)
# ============================================================================

def parse_output(llm_output):
    """
    Parse the LLM's output to extract the classification.
    
    This is optional - you can implement custom parsing logic here.
    Default behavior extracts "Positive" or "Negative" from the output.
    
    Args:
        llm_output (str): Raw output from the LLM
        
    Returns:
        str: Either "Positive" or "Negative"
        
    EXAMPLES:
        llm_output = "The sentiment is Positive based on..."
        return "Positive"
        
        llm_output = "Negative"
        return "Negative"
    """
    output = llm_output.strip()
    
    # Simple extraction - customize if needed
    if "Positive" in output:
        return "Positive"
    elif "Negative" in output:
        return "Negative"
    else:
        # Default fallback
        return "Positive"  # or handle error differently


# ============================================================================
# TESTING (Optional - for local development)
# ============================================================================

def test_locally():
    """
    Test your prompt with a few examples locally.
    This won't be run during evaluation - just for your testing.
    """
    test_reviews = [
        {
            "text": "This movie was absolutely fantastic! Best film of the year.",
            "expected": "Positive"
        },
        {
            "text": "Terrible waste of time. Poor acting and boring plot.",
            "expected": "Negative"
        },
        {
            "text": "Not bad, but could have been better. Some good moments.",
            "expected": "Positive"  # or Negative - borderline case
        }
    ]
    
    print(f"Testing prompt for: {STUDENT_NAME}")
    print("=" * 60)
    
    for i, review in enumerate(test_reviews, 1):
        prompt = get_prompt(review["text"])
        print(f"\nTest {i}:")
        print(f"Review: {review['text'][:50]}...")
        print(f"Expected: {review['expected']}")
        print(f"\nGenerated Prompt Preview:")
        print(prompt[:200] + "..." if len(prompt) > 200 else prompt)
        print("-" * 60)


if __name__ == "__main__":
    # Run local tests
    test_locally()
