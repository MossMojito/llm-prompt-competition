# 🎨 Prompt Engineering Guide

**Master the Art of Talking to LLMs**

---

## 📚 Table of Contents

1. [What is Prompt Engineering?](#what-is-prompt-engineering)
2. [Core Principles](#core-principles)
3. [Prompting Techniques](#prompting-techniques)
4. [Common Patterns](#common-patterns)
5. [Best Practices](#best-practices)
6. [Common Mistakes](#common-mistakes)
7. [Advanced Techniques](#advanced-techniques)

---

## What is Prompt Engineering?

**Prompt Engineering** is the practice of designing inputs (prompts) to guide Large Language Models (LLMs) to produce desired outputs.

Think of it like giving instructions to a very smart but literal assistant:
- ❌ Vague: "Tell me about the review"
- ✅ Clear: "Classify this review as Positive or Negative"

### Why It Matters

The same model can give vastly different results based on HOW you ask:

```python
# Same review, different prompts, different results

Review: "This movie was okay, not great but watchable."

❌ Bad prompt: "sentiment?"
→ Output: "The sentiment is mixed..."

✅ Good prompt: "Classify as Positive or Negative: This movie was okay..."
→ Output: "Positive"
```

---

## Core Principles

### 1. **Be Specific**

❌ Vague: "What's the sentiment?"
✅ Specific: "Classify sentiment as exactly 'Positive' or 'Negative'"

### 2. **Be Clear**

❌ Confusing: "Is this good or bad? Tell me what you think about it."
✅ Clear: "Classify this movie review sentiment as Positive or Negative."

### 3. **Be Concise**

❌ Wordy: "I would like you to please analyze this review and tell me whether the person who wrote it liked the movie or not..."
✅ Concise: "Classify this review as Positive or Negative."

### 4. **Specify Output Format**

❌ No format: "Tell me the sentiment"
✅ With format: "Output ONLY one word: Positive or Negative"

### 5. **Give Examples (When Needed)**

❌ No examples: "Classify sentiment"
✅ With examples: "Example: 'Great film!' → Positive. Now classify: ..."

---

## Prompting Techniques

### 1. Zero-Shot Prompting

**Definition**: Give instructions without examples

**When to use**: Simple, clear tasks

**Example**:
```
Classify this movie review as Positive or Negative.

Review: {review_text}

Classification:
```

**Pros**: 
- Simple
- Fast
- No prompt engineering overhead

**Cons**:
- May be less accurate
- Requires very clear instructions

**Expected Accuracy**: 75-80%

---

### 2. Few-Shot Prompting

**Definition**: Provide examples before the task

**When to use**: When zero-shot doesn't work well

**Example**:
```
Classify movie reviews as Positive or Negative.

Examples:

Review: "Brilliant film! Loved every minute."
Classification: Positive

Review: "Boring and poorly acted."
Classification: Negative

Review: "Masterpiece! Best movie this year."
Classification: Positive

Now classify:

Review: {review_text}
Classification:
```

**Best Practices**:
- Use 2-5 examples (sweet spot)
- Balance positive and negative examples
- Pick diverse examples
- Make examples clear and unambiguous

**Expected Accuracy**: 82-88%

---

### 3. Chain-of-Thought (CoT)

**Definition**: Ask model to reason step-by-step

**When to use**: Complex or ambiguous cases

**Example**:
```
Analyze this movie review step by step.

Review: {review_text}

Analysis:
1. What positive aspects are mentioned?
2. What negative aspects are mentioned?
3. What is the overall tone?
4. Final classification: Positive or Negative

Classification:
```

**Why it works**: 
- Forces systematic analysis
- Reduces errors on edge cases
- More transparent reasoning

**Expected Accuracy**: 85-90%

---

### 4. Role Prompting

**Definition**: Give the model a role or persona

**When to use**: When domain expertise helps

**Example**:
```
You are a professional movie critic with 20 years of experience.

Classify this review as Positive or Negative based on audience sentiment.

Review: {review_text}

Classification:
```

**Pros**:
- Can improve domain understanding
- Sets context

**Cons**:
- May not always help
- Can add unnecessary length

**Expected Accuracy**: 80-85%

---

### 5. Instruction Following

**Definition**: Clear, structured instructions

**When to use**: When output format is critical

**Example**:
```
TASK: Sentiment classification
INPUT: Movie review
OUTPUT: Exactly one word - either "Positive" or "Negative"
RULES: No explanation, no additional text

Review: {review_text}

Output:
```

**Expected Accuracy**: 78-83%

---

## Common Patterns

### Pattern 1: The Sandwich

**Structure**: Instruction → Example → Task → Output Format

```
[INSTRUCTION]
Classify movie review sentiment.

[EXAMPLE]
Review: "Amazing!" → Positive

[TASK]
Review: {review_text}

[OUTPUT FORMAT]
Answer:
```

### Pattern 2: The Template

**Structure**: Fixed template with variable slots

```
Sentiment Analysis

Review: {review_text}
Positive words: ___
Negative words: ___
Overall sentiment: ___

Classification: [Positive/Negative]
```

### Pattern 3: The Comparator

**Structure**: Show contrasting examples

```
Positive example: "Brilliant film!"
Negative example: "Terrible waste of time."

Classify this:
Review: {review_text}
Classification:
```

---

## Best Practices

### ✅ DO's

1. **Test iteratively**
   - Start simple
   - Add complexity only if needed
   - A/B test different approaches

2. **Use consistent formatting**
   - Keep format the same for all reviews
   - Makes parsing easier

3. **Specify output clearly**
   - "Output ONLY 'Positive' or 'Negative'"
   - Reduces parsing errors

4. **Balance examples**
   - Equal positive and negative examples
   - Prevents bias

5. **Keep it simple**
   - Shortest prompt that works
   - Reduces tokens and cost

### ❌ DON'Ts

1. **Don't overcomplicate**
   - More words ≠ better results
   - Often makes things worse

2. **Don't use ambiguous language**
   - Avoid "maybe", "possibly", "could be"
   - Be definitive

3. **Don't forget edge cases**
   - Test on mixed/neutral reviews
   - Handle unexpected inputs

4. **Don't skip testing**
   - Always test before submitting
   - Use sample data

5. **Don't ignore output format**
   - Must match expected format exactly
   - "positive" ≠ "Positive"

---

## Common Mistakes

### Mistake 1: Too Vague

❌ **Bad**:
```
{review_text}

What do you think?
```

**Problem**: Model doesn't know what to output

✅ **Good**:
```
Classify as Positive or Negative: {review_text}

Answer:
```

### Mistake 2: Too Complicated

❌ **Bad**:
```
As an expert in computational linguistics and sentiment analysis,
leveraging state-of-the-art natural language processing techniques,
please perform a comprehensive multi-dimensional analysis...
[300 more words]

Review: {review_text}
```

**Problem**: Confuses the model, wastes tokens

✅ **Good**:
```
Classify this review as Positive or Negative.

Review: {review_text}

Classification:
```

### Mistake 3: Inconsistent Format

❌ **Bad**:
```
# Sometimes:
Review: {review_text}
Answer:

# Other times:
{review_text}
Classification:
```

**Problem**: Inconsistent results

✅ **Good**:
```
# Always the same:
Review: {review_text}

Classification:
```

### Mistake 4: Biased Examples

❌ **Bad**:
```
Examples:
- "Great!" → Positive
- "Loved it!" → Positive  
- "Amazing!" → Positive
- "Terrible." → Negative

Review: {review_text}
```

**Problem**: 3 positive, 1 negative → biased

✅ **Good**:
```
Examples:
- "Great!" → Positive
- "Loved it!" → Positive  
- "Terrible." → Negative
- "Waste of time." → Negative

Review: {review_text}
```

### Mistake 5: No Output Control

❌ **Bad**:
```
{review_text}

Sentiment?
```

**Output might be**: 
- "positive"
- "Positive!"
- "The sentiment is positive"
- "I think it's positive because..."

✅ **Good**:
```
{review_text}

Output ONLY "Positive" or "Negative":
```

---

## Advanced Techniques

### 1. Self-Consistency

Run the same prompt multiple times and take the majority vote.

```python
results = []
for _ in range(5):
    output = model.generate(prompt)
    results.append(parse(output))

# Majority vote
final_answer = most_common(results)
```

**Pros**: More robust, reduces random errors
**Cons**: 5x slower, 5x more expensive

### 2. Prompt Chaining

Break complex task into steps.

```
Step 1: Extract sentiment words
Step 2: Categorize as positive/negative
Step 3: Make final decision
```

### 3. Temperature Tuning

Lower temperature (0.1) → More consistent
Higher temperature (0.9) → More creative

For classification: Use temperature = 0 for consistency

### 4. Delimiters

Use clear separators:

```
### Review ###
{review_text}

### Classification ###
```

Helps model understand structure.

---

## Example Comparison

Let's compare different prompts on the same review:

**Review**: "Not bad, but I expected more from this director."

### Prompt 1: Minimal (Zero-Shot)

```
{review_text}

Positive or Negative?
```

**Likely Output**: "Negative" (56% confidence)

### Prompt 2: Clear Instruction

```
Classify this movie review as Positive or Negative.

Review: {review_text}

Classification:
```

**Likely Output**: "Negative" (72% confidence)

### Prompt 3: Few-Shot

```
Examples:
"Great film!" → Positive
"Terrible movie." → Negative

Review: {review_text}

Classification:
```

**Likely Output**: "Negative" (81% confidence)

### Prompt 4: Chain-of-Thought

```
Analyze this review:

Review: {review_text}

1. Positive words: [none significant]
2. Negative words: disappointed, expected more
3. Tone: Disappointed

Classification: Negative
```

**Likely Output**: "Negative" (89% confidence)

---

## Your Prompt Engineering Workflow

1. **Start Simple**
   - Basic zero-shot prompt
   - Test on 5-10 examples
   - Measure accuracy

2. **Identify Failures**
   - Where does it fail?
   - What patterns cause errors?
   - Analyze mistakes

3. **Iterate**
   - Add few-shot examples?
   - Use chain-of-thought?
   - Clarify instructions?

4. **Test Again**
   - Measure improvement
   - Find new failures
   - Repeat

5. **Optimize**
   - Remove unnecessary words
   - Simplify when possible
   - Keep what works

---

## Quick Reference Card

### For High Accuracy:
- Use few-shot with 3-5 examples
- Add chain-of-thought for hard cases
- Specify exact output format

### For Speed:
- Zero-shot with clear instructions
- Keep prompts short
- Use consistent format

### For Robustness:
- Test on edge cases
- Use balanced examples
- Add explicit rules

### For Debugging:
- Print generated prompts
- Test on known examples
- Check output parsing

---

## Resources

### Learn More
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)

### Tools
- Test prompts on sample data
- Use evaluation metrics
- Compare approaches systematically

---

**Remember**: Prompt engineering is as much art as science. Experiment, measure, and iterate! 🚀

**The best prompt is the one that works for YOUR specific task and data.**

Good luck! 🎯
