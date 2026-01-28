"""
Example Prompts - Learn from Good and Bad Approaches
=====================================================

These are example prompts to demonstrate different strategies.
Study these to understand what works and what doesn't!
"""


# ============================================================================
# ❌ BAD EXAMPLE 1: Too Vague
# ============================================================================

def bad_prompt_vague(review_text):
    """
    Why this is bad:
    - No clear output format specified
    - LLM might generate explanation instead of just label
    - Ambiguous instruction
    """
    prompt = f"Tell me about this review: {review_text}"
    return prompt


# ============================================================================
# ❌ BAD EXAMPLE 2: Overcomplicating
# ============================================================================

def bad_prompt_overcomplicated(review_text):
    """
    Why this is bad:
    - Too many instructions confuse the model
    - Unnecessary complexity
    - Might generate verbose output instead of simple label
    """
    prompt = f"""You are an expert sentiment analyst with 20 years of experience
    in natural language processing and computational linguistics. Your task is
    to perform a comprehensive sentiment analysis on the following movie review,
    considering various linguistic features including lexical choice, syntactic
    structure, pragmatic context, and semantic nuances. After your detailed
    analysis, provide a final classification based on your expert judgment.
    
    Review to analyze: {review_text}
    
    Please provide:
    1. Detailed linguistic analysis
    2. Sentiment indicators
    3. Confidence score
    4. Final classification
    5. Justification
    """
    return prompt


# ============================================================================
# ❌ BAD EXAMPLE 3: No Output Format Control
# ============================================================================

def bad_prompt_no_format(review_text):
    """
    Why this is bad:
    - Doesn't specify exact output format
    - Might get "positive", "POSITIVE", "pos", "good", etc.
    - Hard to parse consistently
    """
    prompt = f"Is this review positive or negative? {review_text}"
    return prompt


# ============================================================================
# ✅ GOOD EXAMPLE 1: Clear Zero-Shot
# ============================================================================

def good_prompt_zero_shot(review_text):
    """
    Why this works:
    - Clear, simple instruction
    - Explicit output format
    - No unnecessary complexity
    
    Expected Accuracy: ~75-80%
    """
    prompt = f"""Classify the sentiment of this movie review.

Review: {review_text}

Respond with ONLY one word - either "Positive" or "Negative".

Sentiment:"""
    return prompt


# ============================================================================
# ✅ GOOD EXAMPLE 2: Few-Shot Learning
# ============================================================================

def good_prompt_few_shot(review_text):
    """
    Why this works:
    - Provides clear examples
    - Shows the exact format expected
    - Balanced examples (positive and negative)
    
    Expected Accuracy: ~82-88%
    """
    prompt = f"""Classify movie reviews as Positive or Negative.

Examples:

Review: "This film was absolutely brilliant! The acting was superb and the plot kept me engaged throughout. Highly recommended!"
Sentiment: Positive

Review: "Complete waste of time. The story was boring and predictable. Poor acting and terrible direction."
Sentiment: Negative

Review: "A masterpiece! Beautiful cinematography and compelling characters. One of the best films I've seen this year."
Sentiment: Positive

Review: "Disappointing and dull. I expected much more from this director. The pacing was slow and the dialogue felt forced."
Sentiment: Negative

Now classify this review:

Review: {review_text}

Sentiment:"""
    return prompt


# ============================================================================
# ✅ GOOD EXAMPLE 3: Chain-of-Thought Reasoning
# ============================================================================

def good_prompt_chain_of_thought(review_text):
    """
    Why this works:
    - Encourages step-by-step reasoning
    - Can improve accuracy on difficult cases
    - Still maintains clear output format
    
    Expected Accuracy: ~85-90%
    """
    prompt = f"""Analyze this movie review and classify its sentiment.

Review: {review_text}

Think step-by-step:
1. What positive words or phrases are present?
2. What negative words or phrases are present?
3. What is the overall tone?

Based on your analysis, is the sentiment Positive or Negative?

Answer with ONLY one word:"""
    return prompt


# ============================================================================
# ✅ GOOD EXAMPLE 4: Role-Playing
# ============================================================================

def good_prompt_role_playing(review_text):
    """
    Why this works:
    - Gives context that helps the model
    - Role-playing can improve performance
    - Clear output specification
    
    Expected Accuracy: ~80-85%
    """
    prompt = f"""You are a professional movie critic analyzing audience reviews.

Your task: Determine if this review is Positive or Negative.

Review: {review_text}

Classification (respond with ONLY "Positive" or "Negative"):"""
    return prompt


# ============================================================================
# ✅ ADVANCED EXAMPLE: Structured Analysis
# ============================================================================

def advanced_prompt_structured(review_text):
    """
    Why this works:
    - Breaks down the task systematically
    - Considers multiple aspects
    - Clear final output requirement
    
    Expected Accuracy: ~88-92%
    Note: Longer prompts use more tokens
    """
    prompt = f"""Classify the sentiment of this movie review as Positive or Negative.

Review: {review_text}

Analysis approach:
- Identify sentiment-bearing words (great, awful, brilliant, terrible, etc.)
- Consider the overall message and recommendation
- Evaluate the tone (enthusiastic, disappointed, neutral)

Important: Your response must be EXACTLY one word - either "Positive" or "Negative".

Classification:"""
    return prompt


# ============================================================================
# COMPARISON SUMMARY
# ============================================================================

"""
Strategy Performance Comparison:
---------------------------------

❌ Bad Approaches (30-60% accuracy):
- Too vague: Model doesn't know what format to use
- Overcomplicated: Confuses the model with unnecessary details
- No format control: Inconsistent outputs, hard to parse

✅ Good Approaches (75-92% accuracy):
- Zero-shot clear: Simple but effective (~75-80%)
- Few-shot: Learn from examples (~82-88%)
- Chain-of-thought: Reason step-by-step (~85-90%)
- Role-playing: Context helps focus (~80-85%)
- Structured: Systematic analysis (~88-92%)

Key Takeaways:
1. Be specific about output format
2. Simpler is often better
3. Few-shot examples help significantly
4. Chain-of-thought can boost accuracy
5. Balance prompt length vs. performance
6. Test and iterate!

Your Task:
- Study these examples
- Understand what makes them work
- Create your own unique strategy
- Test and refine
- Beat the leaderboard! 🏆
"""


# ============================================================================
# TESTING HELPER
# ============================================================================

def compare_prompts(review_text="This movie was amazing! I loved it."):
    """
    Compare all example prompts on a sample review.
    Use this to see the difference in prompt construction.
    """
    prompts = {
        "❌ Vague": bad_prompt_vague,
        "❌ Overcomplicated": bad_prompt_overcomplicated,
        "❌ No Format": bad_prompt_no_format,
        "✅ Zero-shot": good_prompt_zero_shot,
        "✅ Few-shot": good_prompt_few_shot,
        "✅ Chain-of-thought": good_prompt_chain_of_thought,
        "✅ Role-playing": good_prompt_role_playing,
        "✅ Advanced": advanced_prompt_structured,
    }
    
    print("=" * 80)
    print("COMPARING PROMPT STRATEGIES")
    print("=" * 80)
    print(f"\nSample Review: {review_text}\n")
    
    for name, prompt_func in prompts.items():
        print(f"\n{name}")
        print("-" * 80)
        prompt = prompt_func(review_text)
        # Show first 300 chars
        preview = prompt[:300] + "..." if len(prompt) > 300 else prompt
        print(preview)
        print(f"\nPrompt Length: {len(prompt)} characters")


if __name__ == "__main__":
    compare_prompts()
